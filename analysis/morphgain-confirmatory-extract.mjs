#!/usr/bin/env node

import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import process from "node:process";
import playwright from "/Users/brettreynolds/Documents/LLM-CLI-projects/tools/english-corpora/node_modules/playwright/index.js";

const { chromium } = playwright;
const ROOT = "https://www.english-corpora.org";
const FIXED_TERMS = [
  "wowed", "wowing", "wows",
  "booed", "booing", "boos",
  "oohed", "oohing", "oohs",
  "shooed", "shooing", "shoos",
];
const OUT_DIR = path.resolve("analysis", "morphgain-confirmatory");

async function loadEnvFile(filePath) {
  let data;
  try {
    data = await fs.readFile(filePath, "utf8");
  } catch (error) {
    if (error.code === "ENOENT") return;
    throw error;
  }

  for (const rawLine of data.split(/\r?\n/)) {
    const line = rawLine.trim();
    if (!line || line.startsWith("#")) continue;
    const match = line.match(/^([A-Za-z_][A-Za-z0-9_]*)=(.*)$/);
    if (!match) continue;
    let value = match[2].trim();
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }
    process.env[match[1]] = value;
  }
}

async function bodyText(frame) {
  try {
    return await frame.locator("body").innerText({ timeout: 5000 });
  } catch {
    return "";
  }
}

async function waitForFrame(page, name, urlPart, timeoutMs = 30000) {
  const started = Date.now();
  while (Date.now() - started < timeoutMs) {
    const frame = page.frames().find((f) => f.name() === name && (!urlPart || f.url().includes(urlPart)));
    if (frame) return frame;
    await page.waitForTimeout(250);
  }
  throw new Error(`Timed out waiting for frame ${name}`);
}

async function waitForResultFrame(page, name, previousUrl, timeoutMs = 150000) {
  const started = Date.now();
  let stableText = "";
  let stableSince = 0;
  while (Date.now() - started < timeoutMs) {
    const frame = page.frames().find((f) => f.name() === name);
    if (frame && frame.url() !== previousUrl && !/start2\.asp|about:blank$/i.test(frame.url())) {
      const ready = await frame.evaluate(() => document.readyState).catch(() => "");
      const text = await bodyText(frame);
      const trimmed = text.trim();
      if (ready && trimmed) {
        if (trimmed === stableText) {
          if (Date.now() - stableSince >= 2500) return frame;
        } else {
          stableText = trimmed;
          stableSince = Date.now();
        }
      }
    }
    await page.waitForTimeout(500);
  }
  throw new Error(`Timed out waiting for result frame ${name}`);
}

async function login(page) {
  if (!process.env.ENGLISH_CORPORA_EMAIL || !process.env.ENGLISH_CORPORA_PASSWORD) {
    throw new Error("Missing ENGLISH_CORPORA_EMAIL or ENGLISH_CORPORA_PASSWORD");
  }
  await page.goto(`${ROOT}/login.asp`, { waitUntil: "domcontentloaded", timeout: 30000 });
  await page.locator('input[name="email"]').fill(process.env.ENGLISH_CORPORA_EMAIL);
  await page.locator('input[name="password"]').fill(process.env.ENGLISH_CORPORA_PASSWORD);
  await Promise.all([
    page.waitForLoadState("domcontentloaded").catch(() => {}),
    page.locator('input[type="submit"]').first().click(),
  ]);
}

async function extractResult(frame) {
  return frame.evaluate(() => {
    const clean = (s) => String(s || "")
      .replace(/\u00a0/g, " ")
      .replace(/[ \t]+\n/g, "\n")
      .replace(/\n{3,}/g, "\n\n")
      .trim();
    const tables = Array.from(document.querySelectorAll("table")).map((table) => {
      return Array.from(table.rows).map((row) => {
        return Array.from(row.cells).map((cell) => clean(cell.innerText));
      }).filter((row) => row.some(Boolean));
    }).filter((table) => table.length);
    return {
      url: location.href,
      title: document.title || "",
      text: clean(document.body?.innerText || ""),
      tables,
    };
  });
}

async function prepareQueryPage(page) {
  await page.goto(`${ROOT}/coha/`, { waitUntil: "domcontentloaded", timeout: 30000 });
  const x1 = await waitForFrame(page, "x1", "x1.asp");
  await x1.waitForSelector("form#zabba input#p", { timeout: 30000 });
  return x1;
}

async function queryChart(page, term) {
  const x1 = await prepareQueryPage(page);
  const x2 = page.frames().find((f) => f.name() === "x2");
  const previousUrl = x2?.url() || "";
  await x1.evaluate((query) => {
    const form = document.forms.zabba;
    document.getElementById("p").value = query;
    form.target = "x2";
    form.action = "x2.asp";
    form.chooser.value = "chart";
    form.chartx4.value = "n";
    if (form.showsec) form.showsec.checked = false;
    const submit = document.getElementById("submit1");
    if (submit) submit.value = "See frequency by section";
  }, term);
  await x1.locator("input#submit1").click();
  const resultFrame = await waitForResultFrame(page, "x2", previousUrl);
  return extractResult(resultFrame);
}

async function queryKwic(page, term) {
  const x1 = await prepareQueryPage(page);
  const x3 = page.frames().find((f) => f.name() === "x3");
  const previousUrl = x3?.url() || "";
  await x1.evaluate((query) => {
    const form = document.forms.zabba;
    document.getElementById("p").value = query;
    form.target = "x3";
    form.action = "x2.asp";
    form.chooser.value = "kwic";
    if (form.showsec) form.showsec.checked = false;
    if (form.sortBy && form.sortBy.options.length > 3) {
      for (const option of form.sortBy.options) option.selected = false;
      form.sortBy.options[3].selected = true;
    }
    if (form.kh) {
      for (const option of form.kh.options) option.selected = option.value === "1000";
    }
    const submit = document.getElementById("submit1");
    if (submit) submit.value = "Keyword in Context (KWIC)";
  }, term);
  await x1.locator("input#submit1").click();
  const resultFrame = await waitForResultFrame(page, "x3", previousUrl);
  return extractResult(resultFrame);
}

function totalRows(result) {
  return (result.tables || []).reduce((sum, table) => sum + table.length, 0);
}

async function writeJson(filePath, data) {
  await fs.mkdir(path.dirname(filePath), { recursive: true });
  await fs.writeFile(filePath, `${JSON.stringify(data, null, 2)}\n`);
}

async function main() {
  const mode = process.argv[2] || "all";
  if (!["charts", "kwic", "all"].includes(mode)) {
    throw new Error("Usage: node analysis/morphgain-confirmatory-extract.mjs [charts|kwic|all] [fixed preregistered terms...]");
  }
  const terms = process.argv.slice(3);
  const selectedTerms = terms.length ? terms : FIXED_TERMS;
  const invalid = selectedTerms.filter((term) => !FIXED_TERMS.includes(term));
  if (invalid.length) throw new Error(`Terms not in preregistered set: ${invalid.join(", ")}`);

  await loadEnvFile(path.join(os.homedir(), ".config", "english-corpora", "env"));
  await fs.mkdir(path.join(OUT_DIR, "raw"), { recursive: true });

  const runId = new Date().toISOString().replace(/[:.]/g, "-");
  const metadata = {
    preregistration_commit: "f1a2193",
    extraction_started_at: new Date().toISOString(),
    corpus: "COHA",
    fixed_target_terms: FIXED_TERMS,
    selected_terms: selectedTerms,
    mode,
  };
  await writeJson(path.join(OUT_DIR, "extraction-metadata.json"), metadata);
  await writeJson(path.join(OUT_DIR, "runs", `${runId}.json`), metadata);

  const context = await chromium.launchPersistentContext(`/private/tmp/ecorg-morphgain-confirmatory-${Date.now()}`, {
    headless: true,
    viewport: { width: 1200, height: 900 },
    locale: "en-US",
  });

  try {
    const page = context.pages()[0] || await context.newPage();
    await login(page);

    for (const term of selectedTerms) {
      if (mode === "charts" || mode === "all") {
        const chart = await queryChart(page, term);
        await writeJson(path.join(OUT_DIR, "raw", `${term}-chart.json`), chart);
        console.log(`${term}\tchart\t${totalRows(chart)} rows`);
        await page.waitForTimeout(750);
      }
      if (mode === "kwic" || mode === "all") {
        const kwic = await queryKwic(page, term);
        await writeJson(path.join(OUT_DIR, "raw", `${term}-kwic.json`), kwic);
        console.log(`${term}\tkwic\t${totalRows(kwic)} rows`);
        await page.waitForTimeout(750);
      }
    }
  } finally {
    await context.close();
  }
}

main().catch((error) => {
  console.error(error.stack || error.message);
  process.exit(1);
});
