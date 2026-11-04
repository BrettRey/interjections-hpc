# Read the existing model output without fitting or writing to the project.
# Run from the project root: Rscript --vanilla path/to/read_saved_fie.R
e <- new.env()
load('analysis/fie-confirmatory-results.RData', envir=e)
cat('Existing RData SHA-256 is recorded separately in findings.txt.\n')
for (label in c('syn', 'sem', 'int')) {
  x <- e[[paste0('tau_', label)]]
  cat(label, 'N:', length(x), 'median:', median(x),
      '95%:', quantile(x, c(.025, .975)), '\n')
}
cat('saved pr_ordered:', e$pr_ordered,
    'recomputed:', mean(e$tau_int < e$tau_sem & e$tau_sem < e$tau_syn), '\n')
cat('model input total:', sum(e$decade_bin$n), '\n')
print(e$decade_bin)
