
    (() => {
      const root = document.getElementById('rotating-bearers-demo');
      const svg = root.querySelector('svg');
      const plot = root.querySelector('.plot');
      const stateLine = root.querySelector('[data-state]');
      const controls = Array.from(root.querySelectorAll('[data-angle]'));
      const ns = 'http://www.w3.org/2000/svg';
      const points = [];
      let index = 0;
      for (const x of [-1, 1]) for (const y of [-1, 1]) for (const z of [-1, 1]) {
        points.push({
          label: 'ABCDEFGH'[index++],
          xyz: [x + .14 * y, y + .14 * x, .85 * z + .20 * x * y]
        });
      }
      const corners = [];
      for (const x of [-1.28, 1.28]) for (const y of [-1.28, 1.28]) for (const z of [-1.28, 1.28]) corners.push([x, y, z]);
      const edges = [];
      corners.forEach((p, i) => corners.forEach((q, j) => {
        if (j > i && p.filter((v, k) => v !== q[k]).length === 1) edges.push([p, q]);
      }));
      const saved = window.openai?.widgetState;
      let angle = Number.isFinite(saved?.privateContent?.angle) ? saved.privateContent.angle : 45;
      angle = Math.min(90, Math.max(0, angle));
      let animation = 0;
      const layer = document.createElementNS(ns, 'g');
      svg.appendChild(layer);

      function element(tag, attrs, text) {
        const node = document.createElementNS(ns, tag);
        for (const [k, v] of Object.entries(attrs)) node.setAttribute(k, String(v));
        if (text !== undefined) node.textContent = text;
        layer.appendChild(node);
        return node;
      }
      function draw() {
        const width = Math.max(280, plot.getBoundingClientRect().width);
        const height = Math.max(310, Math.min(450, width * .72));
        svg.setAttribute('viewBox', `0 0 ${width} ${height}`);
        svg.style.height = `${height}px`;
        layer.replaceChildren();
        const theta = angle * Math.PI / 180;
        const elevation = .27 * Math.sin(2 * theta);
        const scale = Math.min((width - 70) / 3.9, (height - 62) / 3.55);
        const cx = width / 2, cy = height / 2;
        function project(p) {
          const horizontal = p[0] * Math.cos(theta) + p[1] * Math.sin(theta);
          const depth = -p[0] * Math.sin(theta) + p[1] * Math.cos(theta);
          const vertical = p[2] * Math.cos(elevation) + depth * Math.sin(elevation);
          return [cx + scale * horizontal, cy - scale * vertical, depth];
        }
        for (const [a, b] of edges) {
          const p = project(a), q = project(b);
          element('line', {x1: p[0], y1: p[1], x2: q[0], y2: q[1], class: 'cube-edge'});
        }
        const origin = [-1.45, -1.45, -1.45];
        const axisData = [
          [[1.45, -1.45, -1.45], 'x'],
          [[-1.45, 1.45, -1.45], 'y'],
          [[-1.45, -1.45, 1.45], 'z']
        ];
        const start = project(origin);
        for (const [end, label] of axisData) {
          const q = project(end);
          if (Math.hypot(q[0] - start[0], q[1] - start[1]) < 22) continue;
          element('line', {x1: start[0], y1: start[1], x2: q[0], y2: q[1], class: 'axis'});
          const px = Math.min(width - 12, Math.max(12, q[0] + (label === 'z' ? -10 : 12)));
          const py = Math.min(height - 9, Math.max(14, q[1] + (label === 'z' ? -8 : 5)));
          element('text', {x: px, y: py, 'text-anchor': 'middle', class: 'axis-label'}, label);
        }
        const located = points.map(p => ({...p, screen: project(p.xyz)})).sort((a, b) => a.screen[2] - b.screen[2]);
        for (const p of located) {
          const [x, y] = p.screen;
          element('circle', {cx: x, cy: y, r: 11, class: 'bearer'});
          element('text', {x, y, 'text-anchor': 'middle', 'dominant-baseline': 'central'}, p.label);
        }
        controls.forEach(b => b.setAttribute('aria-pressed', Math.abs(Number(b.dataset.angle) - angle) < .1 ? 'true' : 'false'));
      }
      function describe() {
        if (angle < .1) stateLine.textContent = 'x–z view · differences along y recede';
        else if (angle > 89.9) stateLine.textContent = 'y–z view · differences along x recede';
        else stateLine.textContent = 'Oblique view · all three dimensions visible';
      }
      function persist() {
        window.openai?.setWidgetState?.({
          modelContent: {view: angle < .1 ? 'x-z' : angle > 89.9 ? 'y-z' : 'oblique'},
          privateContent: {angle}
        })?.catch(() => {});
      }
      function move(target) {
        cancelAnimationFrame(animation);
        const from = angle;
        if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
          angle = target; draw(); describe(); persist(); return;
        }
        const begin = performance.now();
        function frame(now) {
          const t = Math.min(1, (now - begin) / 1700);
          const eased = t * t * (3 - 2 * t);
          angle = from + (target - from) * eased;
          draw();
          if (t < 1) animation = requestAnimationFrame(frame);
          else { describe(); persist(); }
        }
        animation = requestAnimationFrame(frame);
      }
      controls.forEach(b => b.addEventListener('click', () => move(Number(b.dataset.angle))));
      new ResizeObserver(draw).observe(plot);
      window.addEventListener('openai:set_globals', e => {
        const restored = e.detail?.globals?.widgetState?.privateContent?.angle;
        if (Number.isFinite(restored)) {
          cancelAnimationFrame(animation);
          angle = Math.min(90, Math.max(0, restored)); draw(); describe();
        }
      });
      draw(); describe();
    })();
  