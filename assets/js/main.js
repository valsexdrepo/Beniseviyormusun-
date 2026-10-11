/* FRAME — site davranışları */

/* DÜZENLE: Tüm Discord butonları bu adresi kullanır. Sunucu davet linkini buraya yaz. */
const FRAME_CONFIG = {
  discord: "https://discord.gg/",
  email: "" // İstersen "destek@ornek.com" gibi bir e-posta ekle; boşsa e-posta kartı gizlenir.
};

/* Discord linklerini tek noktadan ayarla */
document.querySelectorAll("[data-discord]").forEach((link) => {
  link.setAttribute("href", FRAME_CONFIG.discord);
  link.setAttribute("target", "_blank");
  link.setAttribute("rel", "noreferrer noopener");
});
document.querySelectorAll("[data-email]").forEach((el) => {
  if (FRAME_CONFIG.email) {
    el.hidden = false;
    el.querySelectorAll("a").forEach((a) => { a.href = `mailto:${FRAME_CONFIG.email}`; a.textContent = FRAME_CONFIG.email; });
  } else {
    el.hidden = true;
  }
});

/* Aktif sayfa vurgusu */
const page = document.body.dataset.page;
const navLinks = document.querySelector("#nav-links");
if (page && navLinks) {
  navLinks.querySelectorAll("a[href]").forEach((link) => {
    if (link.getAttribute("href") === `${page}.html` || (page === "home" && link.getAttribute("href") === "index.html")) {
      link.setAttribute("aria-current", "page");
    }
  });
}

/* Mobil menü */
const toggle = document.querySelector(".menu-toggle");
if (toggle && navLinks) {
  const setOpen = (open) => {
    navLinks.classList.toggle("open", open);
    toggle.setAttribute("aria-expanded", String(open));
    toggle.setAttribute("aria-label", open ? "Menüyü kapat" : "Menüyü aç");
  };
  toggle.addEventListener("click", () => setOpen(!navLinks.classList.contains("open")));
  navLinks.addEventListener("click", (e) => { if (e.target.closest("a")) setOpen(false); });
  document.addEventListener("keydown", (e) => { if (e.key === "Escape") setOpen(false); });
  window.addEventListener("resize", () => { if (window.innerWidth > 720) setOpen(false); }, { passive: true });
}

/* Kaydırınca yumuşak görünme */
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const targets = document.querySelectorAll(".card, .step, .price-card, .strip-item, .timeline li, .check-list li, .section-head, .cta, details, .helper .card");
if (!reduceMotion && "IntersectionObserver" in window) {
  targets.forEach((el) => {
    el.classList.add("reveal");
    const i = Array.from(el.parentElement.children).indexOf(el);
    el.style.setProperty("--d", `${Math.min(i * 60, 240)}ms`);
  });
  const io = new IntersectionObserver((entries, obs) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) { entry.target.classList.add("in"); obs.unobserve(entry.target); }
    });
  }, { threshold: .1, rootMargin: "0px 0px -30px 0px" });
  targets.forEach((el) => io.observe(el));
  /* Güvenlik: görünür alandakileri hemen göster; 3 sn sonra ne kalırsa hepsini göster */
  const vh = window.innerHeight;
  targets.forEach((el) => { if (el.getBoundingClientRect().top < vh) el.classList.add("in"); });
  setTimeout(() => targets.forEach((el) => el.classList.add("in")), 3000);
}

/* Sistem bilgisi şablonunu kopyala (iletişim sayfası) */
const copyBtn = document.querySelector("[data-copy]");
if (copyBtn) {
  const source = document.querySelector(copyBtn.dataset.copy);
  const status = document.querySelector("[data-copy-status]");
  const show = (msg) => { if (status) { status.textContent = msg; status.classList.add("show"); setTimeout(() => status.classList.remove("show"), 2200); } };
  const fallbackCopy = (text) => {
    const area = document.createElement("textarea");
    area.value = text; area.setAttribute("readonly", ""); area.style.position = "fixed"; area.style.opacity = "0";
    document.body.appendChild(area); area.select();
    let ok = false;
    try { ok = document.execCommand("copy"); } catch { ok = false; }
    area.remove();
    return ok;
  };
  copyBtn.addEventListener("click", async () => {
    const text = source.textContent.trim();
    try {
      await navigator.clipboard.writeText(text);
      show("Kopyalandı");
    } catch {
      if (fallbackCopy(text)) show("Kopyalandı");
      else {
        const range = document.createRange(); range.selectNodeContents(source);
        const sel = window.getSelection(); sel.removeAllRanges(); sel.addRange(range);
        show("Metin seçildi, Ctrl+C ile kopyala");
      }
    }
  });
}

/* SSS: yalnızca bir soru açık kalsın (aynı grupta) */
document.querySelectorAll(".faq").forEach((group) => {
  group.addEventListener("toggle", (e) => {
    if (e.target.open) group.querySelectorAll("details[open]").forEach((d) => { if (d !== e.target) d.open = false; });
  }, true);
});

/* Sayfa geçişi: View Transitions desteklemeyen tarayıcılar için yumuşak çıkış */
if (!("startViewTransition" in document) && !reduceMotion) {
  document.addEventListener("click", (e) => {
    const a = e.target.closest("a[href]");
    if (!a || a.target === "_blank" || a.hasAttribute("download") || e.metaKey || e.ctrlKey || e.shiftKey || e.button !== 0) return;
    const url = new URL(a.href, location.href);
    if (url.origin !== location.origin || url.pathname === location.pathname) return;
    e.preventDefault();
    document.body.classList.add("is-leaving");
    setTimeout(() => { location.href = url.href; }, 180);
  });
  window.addEventListener("pageshow", () => document.body.classList.remove("is-leaving"));
}

/* Üst bar: kaydırınca koyulaşır */
const header = document.querySelector(".header");
if (header) {
  const onScroll = () => header.classList.toggle("scrolled", window.scrollY > 24);
  window.addEventListener("scroll", onScroll, { passive: true }); onScroll();
}

/* Kartlarda imleci takip eden spot ışığı */
if (!reduceMotion && window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
  let raf = 0, target = null, px = 0, py = 0;
  document.addEventListener("pointermove", (e) => {
    const el = e.target.closest(".card, .feature, .step, .plan, .price-card, .module");
    if (!el) return;
    target = el; px = e.clientX; py = e.clientY;
    if (!raf) raf = requestAnimationFrame(() => {
      raf = 0; const r = target.getBoundingClientRect();
      target.style.setProperty("--mx", `${px - r.left}px`); target.style.setProperty("--my", `${py - r.top}px`);
    });
  }, { passive: true });
}

/* Rakamlar sayarak gelir */
document.querySelectorAll("[data-count]").forEach((el) => {
  const end = Number(el.dataset.count); if (!end || reduceMotion) return;
  const t0 = performance.now(), dur = 1100;
  const tick = (now) => { const p = Math.min(1, (now - t0) / dur); const e = 1 - Math.pow(1 - p, 3); el.textContent = Math.round(end * e); if (p < 1) requestAnimationFrame(tick); };
  requestAnimationFrame(tick);
});

/* Oyun kapakları: sonsuz döngü, her 0,5 sn'de tam bir kart ileri, sıçramasız */
document.querySelectorAll("[data-covers]").forEach((box) => {
  const track = box.querySelector(".covers-track");
  const originals = [...track.children];
  if (!originals.length) return;
  originals.forEach((el) => track.appendChild(el.cloneNode(true)));
  originals.forEach((el) => track.appendChild(el.cloneNode(true)));
  const tiles = [...track.children];
  const n = originals.length;
  const STEP_MS = 1000;     /* bir kartın kayma süresi */
  const HOLD_MS = 400;      /* kartlar arası bekleme */
  const PAUSE_MS = 4000;    /* kullanıcı dokununca bekleme */
  let cur = n + 2, setW = 0, anim = 0, pausedUntil = 0, raf = 0;

  const measure = () => { setW = tiles[n].offsetLeft - tiles[0].offsetLeft; };
  const targetFor = (i) => tiles[i].offsetLeft + tiles[i].offsetWidth / 2 - box.clientWidth / 2;
  const mark = () => { raf = 0; const cx = box.scrollLeft + box.clientWidth / 2; let best = 0, dist = Infinity;
    tiles.forEach((el, i) => { const d = Math.abs(el.offsetLeft + el.offsetWidth / 2 - cx); if (d < dist) { dist = d; best = i; } });
    tiles.forEach((el, i) => el.classList.toggle("active", i === best)); return best; };
  const normalize = () => {
    if (!setW) measure();
    if (cur >= 2 * n) { cur -= n; box.scrollLeft -= setW; }
    else if (cur < n) { cur += n; box.scrollLeft += setW; }
  };
  const ease = (p) => 1 - Math.pow(1 - p, 3);
  const animateTo = (left, ms, done) => {
    cancelAnimationFrame(anim);
    const from = box.scrollLeft, t0 = performance.now();
    const frame = (now) => {
      const p = Math.min(1, (now - t0) / ms);
      box.scrollLeft = from + (left - from) * ease(p);
      if (p < 1) anim = requestAnimationFrame(frame); else { anim = 0; done && done(); }
    };
    anim = requestAnimationFrame(frame);
  };
  const step = () => {
    if (Date.now() < pausedUntil) return setTimeout(step, 200);
    cur += 1;
    animateTo(targetFor(cur), STEP_MS, () => { normalize(); setTimeout(step, HOLD_MS); });
  };
  const touch = () => { pausedUntil = Date.now() + PAUSE_MS; cancelAnimationFrame(anim); anim = 0; };

  box.addEventListener("scroll", () => { if (!raf) raf = requestAnimationFrame(mark); }, { passive: true });
  box.addEventListener("wheel", touch, { passive: true });
  tiles.forEach((el, i) => el.addEventListener("click", () => { touch(); cur = i; animateTo(targetFor(cur), 400, normalize); }));
  let down = false, startX = 0, startLeft = 0, moved = false;
  box.addEventListener("pointerdown", (e) => { touch(); down = true; moved = false; startX = e.clientX; startLeft = box.scrollLeft; box.classList.add("dragging"); });
  window.addEventListener("pointermove", (e) => { if (!down) return; const dx = e.clientX - startX; if (Math.abs(dx) > 4) moved = true; box.scrollLeft = startLeft - dx; });
  window.addEventListener("pointerup", () => { if (!down) return; down = false; box.classList.remove("dragging"); cur = mark(); animateTo(targetFor(cur), 300, normalize); });
  box.addEventListener("click", (e) => { if (moved) e.stopPropagation(); }, true);
  window.addEventListener("resize", () => { measure(); box.scrollLeft = targetFor(cur); }, { passive: true });

  measure(); box.scrollLeft = targetFor(cur); mark();
  setTimeout(step, 800);
});

/* Üç adım: sekmeli sahne */
document.querySelectorAll(".howtab").forEach((box) => {
  const btns = [...box.querySelectorAll(".howtab-btn")], panels = [...box.querySelectorAll(".howtab-panel")];
  const activate = (idx) => {
    btns.forEach((b, i) => { b.classList.toggle("is-active", i === idx); b.setAttribute("aria-selected", i === idx ? "true" : "false"); });
    panels.forEach((p, i) => {
      const on = i === idx; p.classList.toggle("is-active", on);
      if (on) { p.removeAttribute("hidden"); const els = p.querySelectorAll(".howtab-title,.howtab-desc,.howtab-feats,.howtab-media"); els.forEach((e) => { e.style.animation = "none"; }); void p.offsetWidth; els.forEach((e) => { e.style.animation = ""; }); }
      else p.setAttribute("hidden", "");
    });
  };
  /* Otomatik akış: her sekme 9 sn, aktif sekmede ilerleme çizgisi; üzerine gelince durur, tıklayınca elle moda geçer */
  const AUTO = 9000; let timer = 0, auto = !reduceMotion, hover = false;
  const current = () => btns.findIndex((b) => b.classList.contains("is-active"));
  const schedule = () => { clearTimeout(timer); if (!auto) return; btns.forEach((b) => b.classList.remove("is-auto")); void box.offsetWidth; btns[current()].classList.add("is-auto"); timer = setTimeout(() => { if (!hover) activate((current() + 1) % btns.length); schedule(); }, AUTO); };
  box.addEventListener("pointerenter", () => { hover = true; btns.forEach((b) => b.style.setProperty("--paused", "paused")); box.classList.add("is-hover"); });
  box.addEventListener("pointerleave", () => { hover = false; box.classList.remove("is-hover"); });
  const io = new IntersectionObserver((en) => en.forEach((x) => { if (x.isIntersecting) schedule(); else clearTimeout(timer); }), { threshold: .35 });
  io.observe(box);
  { const r = box.getBoundingClientRect(); if (r.bottom > 0 && r.top < innerHeight) schedule(); }
  const hashTab = location.hash.match(/adim-(\d)/); if (hashTab) activate(Math.min(btns.length - 1, Math.max(0, Number(hashTab[1]) - 1)));
  btns.forEach((b, i) => {
    b.addEventListener("click", () => { auto = false; clearTimeout(timer); btns.forEach((x) => x.classList.remove("is-auto")); if (!b.classList.contains("is-active")) activate(i); });
    b.addEventListener("keydown", (e) => { const n = btns.length; if (e.key === "ArrowRight" || e.key === "ArrowDown") { e.preventDefault(); activate((i + 1) % n); btns[(i + 1) % n].focus(); } if (e.key === "ArrowLeft" || e.key === "ArrowUp") { e.preventDefault(); activate((i - 1 + n) % n); btns[(i - 1 + n) % n].focus(); } });
  });
});


/* Gösterge: FPS sayacı, ibre animasyonunun gerçek zamanına kilitli */
document.querySelectorAll(".s-gauge").forEach((scene) => {
  const el = scene.querySelector(".g-digit"), needle = scene.querySelector(".g-needle");
  if (!el || !needle) return;
  const keys = [[0,-220],[0.9,-190],[2.1,-110],[3.5,-30],[4.4,30],[5.6,31],[6.6,26],[7.8,29],[8.5,10],[9.2,-100],[9.9,-170],[10.6,-210],[11.3,-220]];
  const ease = (p) => p < .5 ? 2 * p * p : 1 - Math.pow(-2 * p + 2, 2) / 2;
  const ang = (tt) => { for (let i = 1; i < keys.length; i++) { if (tt <= keys[i][0]) { const [t0, a0] = keys[i - 1], [t1, a1] = keys[i]; return a0 + (a1 - a0) * ease((tt - t0) / (t1 - t0)); } } return -220; };
  if (reduceMotion) { el.textContent = "360"; return; }
  const tick = () => {
    const anim = needle.getAnimations ? needle.getAnimations()[0] : null;
    const tt = anim && anim.currentTime != null ? ((anim.currentTime % 11300) / 1000) : ((performance.now() % 11300) / 1000);
    el.textContent = Math.round((ang(tt) + 220) / 260 * 360);
  };
  tick(); setInterval(tick, 60);
});

/* shot-active-sync: görünmeyen çekimlerin iz animasyonlarını durdur (performans) */
document.querySelectorAll(".s-board").forEach((scene) => {
  const shots = [...scene.querySelectorAll(".shot")];
  setInterval(() => { shots.forEach((sh) => { const on = parseFloat(getComputedStyle(sh).opacity) > 0.01; sh.querySelectorAll(".b-glow path, .b-die").forEach((el) => { el.style.animationPlayState = on ? "running" : "paused"; }); }); }, 150);
});

/* Hareket katmanı: buton harfleri, hero kelimeleri, tablo tik gecikmeleri, ikon sıralı nefes */
document.querySelectorAll(".btn-primary, .btn-tier, .btn-light").forEach((btn) => {
  if (!btn.getAttribute("aria-label")) btn.setAttribute("aria-label", btn.textContent.replace(/\s+/g, " ").trim());
  [...btn.childNodes].forEach((node) => {
    if (node.nodeType !== 3 || !node.textContent.trim()) return;
    const wrap = document.createElement("span"); wrap.className = "txt";
    [...node.textContent.trim()].forEach((ch, i) => { const s = document.createElement("span"); s.className = "ltr"; s.textContent = ch; s.style.setProperty("--i", i); wrap.appendChild(s); });
    node.replaceWith(wrap);
  });
});
document.querySelectorAll(".hero h1").forEach((h) => {
  let i = 0;
  const wrap = (node) => {
    [...node.childNodes].forEach((n) => {
      if (n.nodeType === 3) { const frag = document.createDocumentFragment(); n.textContent.split(/(\s+)/).forEach((p) => { if (!p) return; if (/^\s+$/.test(p)) { frag.appendChild(document.createTextNode(" ")); return; } const s = document.createElement("span"); s.className = "w"; s.textContent = p; s.style.setProperty("--i", i++); frag.appendChild(s); }); n.replaceWith(frag); }
      else if (n.nodeType === 1 && n.tagName !== "BR") wrap(n);
    });
  };
  wrap(h);
});
document.querySelectorAll("td .icon").forEach((el, i) => el.style.setProperty("--d", i % 9));
document.querySelectorAll(".icon-box").forEach((el, i) => el.style.setProperty("--i", i % 6));

/* pauseHiddenScenes: ekran dışındaki ağır sahnelerin animasyonlarını durdur */
(() => {
  const heavy = document.querySelectorAll(".howtab-stage, .covers, .chip3d, .vb");
  if (!("IntersectionObserver" in window) || !heavy.length) return;
  const io = new IntersectionObserver((en) => en.forEach((x) => { x.target.style.animationPlayState = x.isIntersecting ? "" : "paused"; x.target.querySelectorAll("*").forEach((e) => { e.style.animationPlayState = x.isIntersecting ? "" : "paused"; }); }), { rootMargin: "200px" });
  heavy.forEach((el) => io.observe(el));
})();
