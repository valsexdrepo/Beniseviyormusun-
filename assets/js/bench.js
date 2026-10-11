/* FRAME — Önce/sonra karşılaştırma bölümü.
   DÜZENLE: BENCH listesine kendi oturum kayıtlarını ekle. video: assets/videos/<dosya>.webm (sol yarı STOK, sağ yarı OPTİMİZE,
   tek dosya) ya da {stock:"...", opt:"..."} iki ayrı dosya. Video yoksa alan "Kayıt yakında" gösterir. Rakamlar senin ölçümün olmalı. */
window.BENCH = [
  { game: "Counter-Strike 2", cover: "cs2.jpg", map: "Mirage", preset: "Low", spec: "9800X3D · RTX 5090 · 32GB 6000 MT/s CL26", video: "cs2.webm", stock: { avg: 610, low: 362, ft: 1.6, gpu: 56, cpu: 64 }, opt: { avg: 878, low: 633, ft: 1.1, gpu: 51, cpu: 63 } },
  { game: "Valorant", cover: "valorant.jpg", map: "Ascent", preset: "Low", spec: "9800X3D · RTX 5090 · 32GB 6000 MT/s CL26", video: "valorant.webm", stock: { avg: 645, low: 438, ft: 1.6, gpu: 48, cpu: 66 }, opt: { avg: 1111, low: 752, ft: 0.9, gpu: 47, cpu: 64 } },
  { game: "Fortnite", cover: "fortnite.jpg", map: "Battle Royale", preset: "Performance Mode", spec: "9800X3D · RTX 5090 · 32GB 6000 MT/s CL26", video: "fortnite.webm", stock: { avg: 646, low: 444, ft: 1.5, gpu: 52, cpu: 63 }, opt: { avg: 966, low: 658, ft: 1.0, gpu: 47, cpu: 63 } },
  { game: "Warzone", cover: "warzone.jpg", map: "Verdansk", preset: "Low", spec: "9800X3D · RTX 5090 · 32GB 6000 MT/s CL26", video: "codwarzone.webm", stock: { avg: 155, low: 117, ft: 6.5, gpu: 55, cpu: 67 }, opt: { avg: 224, low: 165, ft: 4.5, gpu: 47, cpu: 71 } },
  { game: "The Finals", cover: "finals.jpg", map: "Monaco", preset: "Low", spec: "9800X3D · RTX 5090 · 32GB 6000 MT/s CL26", video: "thefinals.webm", stock: { avg: 397, low: 304, ft: 2.5, gpu: 59, cpu: 66 }, opt: { avg: 468, low: 300, ft: 2.1, gpu: 52, cpu: 67 } },
  { game: "Marvel Rivals", cover: "rivals.jpg", map: "Tokyo 2099", preset: "Low", spec: "9800X3D · RTX 5090 · 32GB 6000 MT/s CL26", video: "marvelrivals.webm", stock: { avg: 276, low: 212, ft: 3.6, gpu: 49, cpu: 67 }, opt: { avg: 395, low: 293, ft: 2.5, gpu: 48, cpu: 68 } },
  { game: "PUBG", cover: "pubg.jpg", map: "Erangel", preset: "Low", spec: "9800X3D · RTX 5090 · 32GB 6000 MT/s CL26", video: "pubg.webm", stock: { avg: 428, low: 306, ft: 2.3, gpu: 57, cpu: 67 }, opt: { avg: 743, low: 558, ft: 1.3, gpu: 52, cpu: 69 } },
  { game: "Arc Raiders", cover: "arena.jpg", map: "Dam Battlegrounds", preset: "Low", spec: "9800X3D · RTX 5090 · 32GB 6000 MT/s CL26", video: "arcraiders.webm", stock: { avg: 309, low: 240, ft: 3.2, gpu: 66, cpu: 64 }, opt: { avg: 370, low: 292, ft: 2.7, gpu: 57, cpu: 64 } },
];

(function () {
  const root = document.querySelector("[data-bench]"); if (!root) return;
  const tabs = root.querySelector(".vb-tabs"), vid = root.querySelector(".vb-video"), stats = root.querySelector(".vb-stats");
  const el = (h) => { const d = document.createElement("div"); d.innerHTML = h.trim(); return d.firstElementChild; };
  const n = (v, u = "") => v ? `${v}${u}` : "—";
  const bar = (label, v, max, unit, cls) => `<div class="vb-row"><span class="vb-lbl">${label}</span><div class="vb-bar"><i class="${cls}" style="--w:${max ? Math.min(100, Math.round(v / max * 100)) : 0}%"><b>${n(v, unit)}</b></i></div></div>`;

  BENCH.forEach((b, i) => {
    const t = el(`<button type="button" class="vb-tab${i ? "" : " on"}${b.video ? "" : " pending"}" role="tab"><img src="assets/images/games/${b.cover}" alt="">${b.game}</button>`);
    t.addEventListener("click", () => show(i)); tabs.appendChild(t);
  });

  function show(i) {
    const b = BENCH[i];
    [...tabs.children].forEach((t, k) => t.classList.toggle("on", k === i));
    /* video */
    vid.innerHTML = "";
    const src = typeof b.video === "string" ? b.video : "";
    if (src) {
      vid.appendChild(el(`<video src="assets/videos/${src}" muted loop playsinline autoplay preload="metadata"></video>`));
    } else if (b.video && b.video.stock) {
      vid.appendChild(el(`<div class="vb-split"><video src="assets/videos/${b.video.stock}" muted loop playsinline autoplay></video><video src="assets/videos/${b.video.opt}" muted loop playsinline autoplay></video></div>`));
    } else {
      vid.appendChild(el(`<div class="vb-empty" style="background-image:url(assets/images/games/${b.cover})"><span>Kayıt yakında</span><small>Aynı PC, aynı sahne, aynı ayarlar</small></div>`));
    }
    vid.appendChild(el(`<span class="vb-lab l">STOK</span>`)); vid.appendChild(el(`<span class="vb-lab r">OPTİMİZE</span>`));
    const under = root.querySelector(".vb-under"); if (under) under.innerHTML = `<span class="vb-sys"><b>${b.spec || "Test sistemi: belirtilmedi"}</b> · ${b.game} · 1080p ${b.preset}</span>`;
    /* stats */
    const maxAvg = Math.max(b.stock.avg, b.opt.avg), maxLow = Math.max(b.stock.low, b.opt.low), maxFt = Math.max(b.stock.ft, b.opt.ft);
    stats.innerHTML = `
      <div class="vb-head">
        <div><h3>${b.game}</h3><div class="vb-meta"><span>${ico("map")} ${b.map}</span><span>${ico("set")} ${b.preset}</span></div></div>
        <div class="vb-temps"><span><b>GPU</b>${n(b.stock.gpu)} <i>▶</i> ${n(b.opt.gpu, "°C")}</span><span><b>CPU</b>${n(b.stock.cpu)} <i>▶</i> ${n(b.opt.cpu, "°C")}</span></div>
        <img class="vb-big" src="assets/images/games/${b.cover}" alt="">
      </div>
      <div class="vb-group"><div class="vb-gh"><span>Optimize</span><span>Maks</span></div>${bar("Ort. FPS", b.opt.avg, maxAvg, " FPS", "opt")}${bar("1% low FPS", b.opt.low, maxLow, " FPS", "opt")}${bar("Kare süresi", b.opt.ft, maxFt, " ms", "opt")}</div>
      <div class="vb-group"><div class="vb-gh"><span>Stok</span><span>Maks</span></div>${bar("Ort. FPS", b.stock.avg, maxAvg, " FPS", "")}${bar("1% low FPS", b.stock.low, maxLow, " FPS", "")}${bar("Kare süresi", b.stock.ft, maxFt, " ms", "")}</div>`;
    setTimeout(() => stats.querySelectorAll(".vb-bar i").forEach((x) => x.classList.add("go")), 40);
  }
  function ico(k) { return k === "map" ? '<svg viewBox="0 0 24 24"><path d="M12 21s-6-5.3-6-10a6 6 0 0 1 12 0c0 4.7-6 10-6 10Z"/><circle cx="12" cy="11" r="2"/></svg>' : '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3h0a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8v0a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1Z"/></svg>'; }
  show(0);
})();
