/* FRAME — Ücretsiz PC kontrolü. 7 adım, puan tarayıcıda hesaplanır, sunucu yok.
   DÜZENLE: metinler ve listeler dosyanın üst kısmında; puanlama score() içinde. */
(function () {
  const root = document.querySelector("[data-check]");
  if (!root) return;
  const CFG = window.FRAME_CONFIG || {};
  const icon = (n, cls = "icon") => `<svg class="${cls}" aria-hidden="true"><use href="#i-${n}"/></svg>`;
  const el = (html) => { const d = document.createElement("div"); d.innerHTML = html.trim(); return d.firstElementChild; };

  /* ---------------- VERİ ---------------- */
  const STEPS = ["Oyunun", "Sorunun", "FPS hedefin", "Parçaların", "Windows'un", "Denediklerin", "Sonuçların"];
  const GAMES = ["Fortnite", "Call of Duty / Black Ops", "Valorant", "Apex Legends", "Counter-Strike 2", "Diğer"];
  const PROBLEMS = ["Düşük FPS", "FPS düşüşleri", "Takılmalar", "Girdi gecikmesi", "Oyun ağır / yavaş hissediyor", "Çökme / kararsızlık", "Emin değilim"];
  const TARGETS = ["144 FPS, 1080p", "240 FPS, 1080p", "360+ FPS, 1080p"];
  const TARGETS_COD = ["144 FPS, 1080p", "240 FPS, 1080p", "360+ FPS, 1080p", "180 FPS, 1440p", "240 FPS, 1440p", "300+ FPS, 1440p"];
  const WINDOWS = ["Windows 10", "Windows 11"];
  const TRIED = ["Daha önce FRAME ile optimize ettirdim", "Ücretsiz listeyi uyguladım", "Windows'u sıfırdan kurdum", "GPU sürücülerini güncelledim", "NVIDIA / AMD panel ayarlarını değiştirdim", "BIOS ayarlarını değiştirdim", "Optimizer yazılımı kullandım", "YouTube rehberleri izledim", "Henüz hiçbir şey", "Diğer"];

  /* [etiket, tier, laptop?, soket] */
  const CPUS = {
    amd: [
      ["Ryzen 9000 Serisi (AM5)", [["Ryzen 7 9800X3D", "flagship", 0, "am5"], ["Ryzen 9 9950X3D", "flagship", 0, "am5"], ["Ryzen 9 9950X", "high", 0, "am5"], ["Ryzen 9 9900X", "high", 0, "am5"], ["Ryzen 7 9700X", "high", 0, "am5"], ["Ryzen 5 9600X", "mid", 0, "am5"]]],
      ["Ryzen 7000 Serisi (AM5)", [["Ryzen 7 7800X3D", "flagship", 0, "am5"], ["Ryzen 9 7950X3D", "flagship", 0, "am5"], ["Ryzen 9 7900X3D", "high", 0, "am5"], ["Ryzen 9 7950X / 7900X", "high", 0, "am5"], ["Ryzen 7 7700X / 7700", "high", 0, "am5"], ["Ryzen 5 7600X / 7600", "mid", 0, "am5"]]],
      ["Ryzen 5000 Serisi (AM4)", [["Ryzen 7 5800X3D", "high", 0, "am4"], ["Ryzen 7 5700X3D", "high", 0, "am4"], ["Ryzen 5 5600X3D", "mid", 0, "am4"], ["Ryzen 9 5950X / 5900X", "high", 0, "am4"], ["Ryzen 7 5800X / 5700X", "mid", 0, "am4"], ["Ryzen 5 5600X / 5600", "mid", 0, "am4"], ["Ryzen 5 5500 / 4500", "low", 0, "am4"]]],
      ["Ryzen 3000 ve Eski (AM4)", [["Ryzen 9 3900X / 3950X", "mid", 0, "am4"], ["Ryzen 7 3700X / 3800X", "mid", 0, "am4"], ["Ryzen 5 3600 / 3600X", "low", 0, "am4"], ["Eski Ryzen 1000/2000 veya FX", "low", 0, "am4"]]],
      ["AMD Dizüstü İşlemciler", [["Ryzen 9 / 7 oyuncu dizüstü (HX / HS)", "high", 1, "laptop"], ["Ryzen 5 oyuncu dizüstü (H / HS)", "mid", 1, "laptop"], ["Eski AMD dizüstü işlemci", "low", 1, "laptop"]]],
    ],
    intel: [
      ["Core Ultra Serisi (LGA 1851)", [["Core Ultra 9 285K", "flagship", 0, "1851"], ["Core Ultra 7 265K", "high", 0, "1851"], ["Core Ultra 5 245K", "high", 0, "1851"]]],
      ["14. Nesil Core (LGA 1700)", [["Core i9-14900K / KF / KS", "flagship", 0, "1700"], ["Core i7-14700K / KF", "high", 0, "1700"], ["Core i5-14600K / KF", "high", 0, "1700"], ["Core i5-14400 / F", "mid", 0, "1700"], ["Core i3-14100 / F", "low", 0, "1700"]]],
      ["13. Nesil Core (LGA 1700)", [["Core i9-13900K / KF / KS", "flagship", 0, "1700"], ["Core i7-13700K / KF", "high", 0, "1700"], ["Core i5-13600K / KF", "high", 0, "1700"], ["Core i5-13400 / F", "mid", 0, "1700"], ["Core i3-13100 / F", "low", 0, "1700"]]],
      ["12. Nesil Core (LGA 1700)", [["Core i9-12900K / KF", "high", 0, "1700"], ["Core i7-12700K / KF", "high", 0, "1700"], ["Core i5-12600K / KF", "mid", 0, "1700"], ["Core i5-12400 / F", "mid", 0, "1700"], ["Core i3-12100 / F", "low", 0, "1700"]]],
      ["10. ve 11. Nesil (LGA 1200)", [["Core i9-10900K / 11900K", "mid", 0, "1200"], ["Core i7-10700K / 11700K", "mid", 0, "1200"], ["Core i5 (10. / 11. nesil)", "low", 0, "1200"]]],
      ["9. Nesil ve Eski (LGA 1151)", [["Core i9-9900K / 9900KS", "mid", 0, "1151"], ["Core i7-9700K / 9700", "low", 0, "1151"], ["Core i5 (9. nesil)", "low", 0, "1151"], ["Intel 8. nesil veya eski (8700K, 7700K vb.)", "low", 0, "1151"]]],
      ["Intel Dizüstü İşlemciler", [["Core i9 / i7 oyuncu dizüstü (HX / H)", "high", 1, "laptop"], ["Core i5 oyuncu dizüstü (H / P)", "mid", 1, "laptop"], ["Eski Intel dizüstü işlemci", "low", 1, "laptop"]]],
    ],
  };
  const CHIPSETS = {
    am5: ["AM5 Soketi", "AM5 Yonga Setleri (Ryzen 7000 / 9000)", ["X870E / X870 (Üst seviye AM5)", "B850 (AM5)", "B650E / B650 (Popüler AM5)", "A620 (Giriş AM5)", "Hazır / OEM AM5 anakart"]],
    am4: ["AM4 Soketi", "AM4 Yonga Setleri (Ryzen 1000 – 5000)", ["X570 (Üst seviye AM4)", "B550 (Standart AM4)", "X470 / B450", "X370 / B350 / A320", "Hazır / OEM AM4 anakart"]],
    1851: ["LGA 1851 Soketi", "LGA 1851 Yonga Setleri (Core Ultra)", ["Z890 (Üst seviye)", "B860 (Ana akım)", "H810 (Giriş)", "Hazır / OEM anakart"]],
    1700: ["LGA 1700 Soketi", "LGA 1700 Yonga Setleri (12. – 14. nesil)", ["Z790 (Üst seviye)", "Z690", "B760 / B660 (Ana akım)", "H610 / H770 (Giriş)", "Hazır / OEM anakart (Dell, HP vb.)"]],
    1200: ["LGA 1200 Soketi", "LGA 1200 Yonga Setleri (10. / 11. nesil)", ["Z590 / Z490", "B560 / B460", "H510 / H410", "Hazır / OEM anakart"]],
    1151: ["LGA 1151 / Eski Soket", "LGA 1151 ve Eski Yonga Setleri", ["Z390 / Z370", "B365 / B360 / H310", "Eski Intel anakart (Z270, Z170, Z97, H81 vb.)", "Hazır / OEM anakart"]],
    laptop: ["Dizüstü", "Dizüstü anakartı", ["Oyuncu dizüstü anakartı"]],
  };
  const GPUS = {
    nvidia: [
      ["RTX 50 Serisi", [["RTX 5090", "flagship"], ["RTX 5080", "flagship"], ["RTX 5070 Ti", "high"], ["RTX 5070", "high"], ["RTX 5060 Ti", "mid"], ["RTX 5060", "mid"], ["RTX 5050", "mid"], ["RTX 50 Serisi dizüstü GPU", "high", 1]]],
      ["RTX 40 Serisi", [["RTX 4090", "flagship"], ["RTX 4080 / 4080 Super", "flagship"], ["RTX 4070 Ti / Ti Super", "high"], ["RTX 4070 / 4070 Super", "high"], ["RTX 4060 Ti", "mid"], ["RTX 4060", "mid"], ["RTX 40 Serisi dizüstü GPU", "mid", 1]]],
      ["RTX 30 Serisi", [["RTX 3090 / 3090 Ti", "high"], ["RTX 3080 / 3080 Ti", "high"], ["RTX 3070 / 3070 Ti", "mid"], ["RTX 3060 Ti", "mid"], ["RTX 3060 / 3050", "mid"], ["RTX 30 Serisi dizüstü GPU", "mid", 1]]],
      ["RTX 20 ve GTX 16 Serisi", [["RTX 2080 Ti / 2080 Super", "mid"], ["RTX 2070 / 2070 Super", "mid"], ["RTX 2060 / 2060 Super", "low"], ["GTX 1660 Ti / 1660 Super", "low"], ["GTX 1650 / 1650 Super", "low"]]],
      ["GTX 10 Serisi ve Eski", [["GTX 1080 Ti / 1080", "low"], ["GTX 1070 / 1070 Ti", "low"], ["GTX 1060 / 1050 Ti", "low"], ["GTX 900 serisi veya eski", "low"]]],
    ],
    radeon: [
      ["RX 7000 Serisi", [["RX 7900 XTX", "flagship"], ["RX 7900 XT / GRE", "high"], ["RX 7800 XT", "high"], ["RX 7700 XT", "mid"], ["RX 7600 / 7600 XT", "mid"]]],
      ["RX 6000 Serisi", [["RX 6950 XT / 6900 XT", "high"], ["RX 6800 XT / 6800", "high"], ["RX 6750 XT / 6700 XT", "mid"], ["RX 6650 XT / 6600 XT", "mid"], ["RX 6600 / 6500 XT", "low"]]],
      ["RX 5000 / 500 ve Eski", [["RX 5700 XT / 5700", "low"], ["RX 5600 XT", "low"], ["RX 590 / 580 / 570", "low"], ["RX 400 serisi veya eski", "low"]]],
    ],
  };
  const RAM = [["8GB", "Tek modül (yavaş)"], ["16GB", "DDR5 / DDR4"], ["32GB", "DDR5 / DDR4 • Tatlı nokta"], ["48GB", "DDR5 / DDR4"], ["64GB", "DDR5 / DDR4"], ["96GB+", "DDR5 / DDR4"], ["Diğer", "< 8GB / karışık"]];
  const STORAGE = ["NVMe M.2 SSD (En hızlı)", "SATA 2.5\" SSD", "Mekanik sabit disk (HDD)"];
  const NET = ["Ethernet", "Wi-Fi"];

  const PACKS = {
    none: { name: "Hizmete gerek yok", detail: "Donanım yapılandırman ve ayarların sağlıklı bir performans payı gösteriyor. Oturum ayarlamana gerek yok. Sistemini temiz tutmak istersen aşağıdaki ücretsiz kontrol listesini kullan." },
    basic: { name: "Temel Paket", detail: "Sorunun kaynağı büyük ihtimalle sistem yükü ve ayarlar. Temizlik, servisler, güç planı ve başlangıç optimizasyonu ile başlamak doğru adım." },
    adv: { name: "Gelişmiş Paket", detail: "Belirtilerin sürücü, ağ ve oyun profili katmanına işaret ediyor. Gecikme ve takılma için doğru seviye: Temel'in tamamı artı sürücü profili, ağ, ISLC ve oyun ayarları." },
    expert: { name: "Uzman Paket", detail: "Masaüstü donanımın ve hedefin tam geçişi hak ediyor: Gelişmiş'in tamamı artı BIOS, bellek zamanlamaları, undervolt, çekirdek afinitesi ve temiz özel Windows kurulumu." },
  };
  const RANGES = {
    low: { color: "#10b981", label: "Düşük risk" },
    possible: { color: "#38bdf8", label: "Biraz pay var" },
    likely: { color: "#f59e0b", label: "Belirgin iyileştirme payı" },
    high: { color: "#ef4444", label: "Ciddi darboğaz" },
  };
  const CHECKLIST = [
    ["BIOS temeli", ["Anakart üreticisinin sayfasından en güncel kararlı BIOS'u kur.", "XMP, DOCP veya EXPO'yu aç; RAM anma hızında çalışsın.", "AMD'de yüksek hızlı kitleri bellek denetleyicisinin kararlı olduğundan emin olmadıkça 6000 MT/s civarında tut.", "Above 4G Decoding ve Resizable BAR'ı aç.", "Anti-cheat oyunlar için Secure Boot açık kalsın.", "Harici ekran kartı kullanıyorsan PCIe güç tasarrufu ve tümleşik grafikleri kapat."]],
    ["Windows hazırlığı", ["Yerel bir Windows hesabına geç.", "Başlangıç uygulamalarını Görev Yöneticisi'nden gözden geçir, gereksizleri kapat.", "Güç planını 'Yüksek performans' yap.", "Windows güncellemelerini tamamla, sonra masaüstüne dön ve devam et."]],
    ["Sürücüler ve GPU", ["NVIDIA sürücüsünü DDU ile temiz kur ya da önerilen AMD sürücü yolunu izle.", "NVIDIA ise Profile Inspector profilini uygula.", "NVIDIA veya AMD kontrol panelini temel ayarlara göre kontrol et.", "MSI mod aracını yönetici olarak çalıştır, GPU'nun işaretli olduğunu doğrula."]],
    ["Ağ ve temizlik", ["Ağ adaptörü sürücüsü için yalnızca gerekli sürücüyü kur, bulduğu her şeyi değil.", "Adaptör özelliklerinde IPv4 ve QoS işaretli kalsın; kullanılmayan bağları kaldır.", "Energy Efficient Ethernet gibi güç tasarrufu seçeneklerini kapat.", "Sistem dosyaları için Disk Temizleme çalıştır.", "Autoruns ile ölü başlangıç girdilerini, eski servisleri ve gereksiz zamanlanmış görevleri temizle."]],
    ["İsteğe bağlı: kumanda", ["Kumandayla oynuyorsan ve cihazın destekliyorsa polling-rate değişikliği için HIDUSBF kullan.", "Değişikliğin çalıştığını varsayma; test aracıyla doğrula."]],
  ];

  /* ---------------- DURUM ---------------- */
  const state = { game: "", problem: "", target: "", cpuBrand: "", cpu: "", chipset: "", gpuBrand: "", gpu: "", ram: "", storage: "", net: "", windows: "", tried: [], name: "", email: "", discord: "", consent: false };
  let step = 0, error = "", result = null;

  const findCpu = () => { for (const [, items] of (CPUS[state.cpuBrand] || [])) for (const it of items) if (it[0] === state.cpu) return it; return null; };
  const findGpu = () => { for (const [, items] of (GPUS[state.gpuBrand] || [])) for (const it of items) if (it[0] === state.gpu) return it; return null; };

  function validate(i) {
    if (i === 0 && !state.game) return "Oynadığın oyunu seç.";
    if (i === 1 && !state.problem) return "Gördüğün sorunu seç.";
    if (i === 2 && !state.target) return "Hedeflediğin FPS'i seç.";
    if (i === 3) { if (!state.cpu) return "İşlemci modelini seç."; if (!state.gpu) return "Ekran kartı modelini seç."; if (!state.ram) return "RAM miktarını seç."; }
    if (i === 4 && !state.windows) return "Windows sürümünü seç.";
    if (i === 5 && !state.tried.length) return "Denediğin en az bir şeyi seç.";
    if (i === 6) { if (!state.name.trim()) return "Adını yaz."; if (state.email && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(state.email.trim())) return "Geçerli bir e-posta yaz."; if (!state.consent) return "Sonuçlarını görmek için kutuyu işaretle."; }
    return "";
  }

  /* ---------------- PUAN ---------------- */
  function score() {
    const cpu = findCpu(), gpu = findGpu();
    const T = { flagship: 0, high: 1, mid: 2, low: 3 };
    const laptop = !!(cpu && cpu[2]) || !!(gpu && gpu[2]);
    let s = 12;
    const tc = cpu ? T[cpu[1]] : 2, tg = gpu ? T[gpu[1]] : 2;
    s += tc * 9 + tg * 10;
    const tgt = state.target.includes("360") || state.target.includes("300") ? 2 : state.target.includes("240") || state.target.includes("180") ? 1 : 0;
    s += tgt * 6 + Math.max(0, tgt - (3 - Math.max(tc, tg))) * 6;
    if (state.ram === "8GB") s += 14; else if (state.ram === "Diğer") s += 18; else if (state.ram === "16GB") s += 4;
    if (state.storage.startsWith("Mekanik")) s += 12; else if (state.storage.startsWith("SATA")) s += 3;
    if (state.net === "Wi-Fi") s += 5;
    if (state.windows === "Windows 10") s += 3;
    const p = state.problem;
    if (p === "Düşük FPS") s += 12; if (p === "FPS düşüşleri") s += 15; if (p === "Takılmalar") s += 17; if (p === "Girdi gecikmesi") s += 15; if (p === "Çökme / kararsızlık") s += 18; if (p === "Oyun ağır / yavaş hissediyor") s += 12;
    const tr = state.tried;
    if (tr.includes("Daha önce FRAME ile optimize ettirdim")) s -= 25;
    if (tr.includes("Ücretsiz listeyi uyguladım")) s -= 10;
    if (tr.includes("Windows'u sıfırdan kurdum")) s -= 6;
    if (tr.includes("GPU sürücülerini güncelledim")) s -= 3;
    if (tr.includes("Optimizer yazılımı kullandım")) s += 8;
    if (tr.includes("Henüz hiçbir şey")) s += 6;
    if (laptop) s += 6;
    s = Math.max(4, Math.min(97, Math.round(s)));
    const range = s <= 30 ? "low" : s <= 50 ? "possible" : s <= 72 ? "likely" : "high";
    const balance = !cpu || !gpu ? "Dengeli" : Math.abs(tc - tg) >= 2 ? (tc > tg ? "İşlemci sınırlı" : "Ekran kartı sınırlı") : "Dengeli";
    let pack = "basic";
    if (range === "low") pack = "none";
    else if (!laptop && tc <= 1 && tg <= 1 && (tgt >= 1 || p === "Girdi gecikmesi")) pack = "expert";
    else if (p === "Girdi gecikmesi" || p === "Takılmalar" || p === "FPS düşüşleri" || range === "high") pack = "adv";
    const explain = {
      low: "Bilgisayarın iyi durumda",
      possible: "Ayarlarında kullanılmayan bir pay var",
      likely: `${p === "Emin değilim" ? "Sistem" : p} ayar katmanından kaynaklanıyor gibi görünüyor`,
      high: "Mevcut yapılandırma donanımını geride bırakıyor",
    }[range];
    return { score: s, range, pack, laptop, balance, gpuTier: gpu ? gpu[1] : "custom", explain };
  }

  /* ---------------- GÖRÜNÜM ---------------- */
  const neon = (on) => `<span class="neon${on ? " on" : ""}" aria-hidden="true"><span class="neon-frame"><svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span><span class="neon-borders"><i></i><i></i><i></i><i></i></span><span class="neon-rings"></span><span class="neon-particles">${"<i></i>".repeat(6)}</span></span>`;
  const optBtn = (label, on, sub) => `<button type="button" class="opt${on ? " on" : ""}" data-opt="${label}">${neon(on)}<span class="opt-text">${label}${sub ? `<small>${sub}</small>` : ""}</span></button>`;

  function titleFor(i) {
    return [["Hangi oyunu oynuyorsun?", "Daha iyi çalışmasını istediğin oyunu seç."],
      ["Hangi sorunu görüyorsun?", "Seni en çok rahatsız edeni seç."],
      ["Hedefin kaç FPS?", "En çok önemsediğin hedefi seç. Call of Duty için 1440p seçenekleri de var; çok oyuncu o çözünürlükte oynuyor."],
      ["Donanımını seç", "Parçalarını aşağıdaki menülerden seç. İşlemci, ekran kartı ve RAM zorunlu."],
      ["Hangi Windows?", "Bu bilgisayardaki ana Windows sürümünü seç."],
      ["Neler denedin?", "Uyan her şeyi seç. İşe yaramamış olsa bile."],
      ["Sonuçlarını kime hazırlayalım?", "Puanın anında ekranda görünür. Hiçbir veri gönderilmez."]][i];
  }

  function render() {
    root.innerHTML = "";
    if (result) return renderResult();
    const total = STEPS.length, pct = Math.round(((step + 1) / total) * 100);
    root.append(el(`<div class="wz-head"><div><span class="wz-step">Adım ${step + 1} / ${total}</span><strong>${STEPS[step].toUpperCase()}</strong></div><span class="wz-pct">%${pct} tamamlandı</span></div>`));
    root.append(el(`<div class="wz-bar">${STEPS.map((_, i) => `<i class="${i < step ? "done" : i === step ? "cur" : ""}"></i>`).join("")}</div>`));
    const [q, sub] = titleFor(step);
    const body = el(`<div class="wz-body anim-in"><h3 class="wz-q">${q}</h3><p class="wz-sub">${sub}</p></div>`);
    const grid = el(`<div class="wz-grid"></div>`);

    if (step === 0) GAMES.forEach((g) => grid.append(el(optBtn(g, state.game === g))));
    if (step === 1) PROBLEMS.forEach((g) => grid.append(el(optBtn(g, state.problem === g))));
    if (step === 2) (state.game.startsWith("Call of Duty") ? TARGETS_COD : TARGETS).forEach((g) => grid.append(el(optBtn(g, state.target === g))));
    if (step === 4) WINDOWS.forEach((g) => grid.append(el(optBtn(g, state.windows === g))));
    if (step === 5) TRIED.forEach((g) => grid.append(el(optBtn(g, state.tried.includes(g)))));
    if (step === 3) body.append(renderHardware()); else if (step === 6) body.append(renderContact()); else body.append(grid);

    grid.addEventListener("click", (e) => {
      const b = e.target.closest("[data-opt]"); if (!b) return;
      const v = b.dataset.opt; error = "";
      if (step === 0) state.game = v; if (step === 1) state.problem = v; if (step === 2) state.target = v; if (step === 4) state.windows = v;
      if (step === 5) {
        const exclusive = v === "Henüz hiçbir şey";
        if (exclusive) state.tried = state.tried.includes(v) ? [] : [v];
        else { state.tried = state.tried.filter((x) => x !== "Henüz hiçbir şey"); state.tried = state.tried.includes(v) ? state.tried.filter((x) => x !== v) : [...state.tried, v]; }
      }
      refreshOpts(grid);
    });
    if (error) body.append(el(`<div class="wz-error"><i></i>${error}</div>`));
    root.append(body);

    const nav = el(`<div class="wz-nav"></div>`);
    const back = el(`<button type="button" class="btn btn-ghost btn-sm wz-back"${step === 0 ? " disabled" : ""}>Geri</button>`);
    const next = el(`<button type="button" class="btn btn-primary wz-next">${step === total - 1 ? "Ücretsiz puanımı göster" : "Devam"} ${icon("arrow")}</button>`);
    back.addEventListener("click", () => { error = ""; step = Math.max(0, step - 1); render(); scrollTo(); });
    next.addEventListener("click", () => {
      next.classList.add("pressed"); setTimeout(() => next.classList.remove("pressed"), 650);
      const err = validate(step);
      if (err) { error = err; render(); return; }
      error = "";
      if (step === total - 1) { result = score(); render(); scrollTo(); return; }
      step += 1; render(); scrollTo();
    });
    nav.append(back, next); root.append(nav);
  }

  function refreshOpts(grid) {
    grid.querySelectorAll("[data-opt]").forEach((b) => {
      const v = b.dataset.opt;
      const on = step === 5 ? state.tried.includes(v) : [state.game, state.problem, state.target, "", state.windows][step] === v;
      const was = b.classList.contains("on");
      b.classList.toggle("on", on); b.querySelector(".neon").classList.toggle("on", on);
      if (on && !was) { b.querySelector(".neon").classList.add("burst"); setTimeout(() => b.querySelector(".neon").classList.remove("burst"), 700); }
    });
    const err = root.querySelector(".wz-error"); if (err) err.remove();
  }

  /* --- Donanım adımı --- */
  function renderHardware() {
    const wrap = el(`<div class="hw"></div>`);
    const selectHtml = (ph, groups, value, cls = "") => `<div class="sel-wrap ${cls}"><select class="sel"><option value="">${ph}</option>${groups.map(([g, items]) => `<optgroup label="${g}">${items.map((it) => `<option${(Array.isArray(it) ? it[0] : it) === value ? " selected" : ""}>${Array.isArray(it) ? it[0] : it}</option>`).join("")}</optgroup>`).join("")}</select>${icon("arrow", "icon sel-arrow")}</div>`;

    /* 1. CPU */
    const cpu = el(`<div class="hw-card"><div class="hw-title">${icon("cpu")} 1. İşlemciyi seç (CPU) <b>*</b></div>
      <div class="brand-row">
        <button type="button" class="brand-btn amd${state.cpuBrand === "amd" ? " on" : ""}" data-brand="cpu:amd"><img src="assets/images/brands/amd.svg" alt="AMD"></button>
        <button type="button" class="brand-btn intel${state.cpuBrand === "intel" ? " on" : ""}" data-brand="cpu:intel"><img src="assets/images/brands/intel.svg" alt="Intel"></button>
      </div>
      ${state.cpuBrand ? selectHtml(`${state.cpuBrand === "amd" ? "AMD" : "Intel"} işlemci modelini seç...`, CPUS[state.cpuBrand], state.cpu, "anim-in") : ""}
    </div>`);
    wrap.append(cpu);
    const c = findCpu();
    if (c) {
      const ch = CHIPSETS[c[3]];
      const chip = el(`<div class="hw-card anim-in"><div class="hw-title-row"><span class="hw-title small">Anakart yonga seti <i>(isteğe bağlı)</i></span><span class="tag-mono">${ch[0]}</span></div>${selectHtml(`Uyumlu ${ch[0]} seç (emin değilsen boş bırak)...`, [[ch[1], ch[2]]], state.chipset)}</div>`);
      chip.querySelector("select").addEventListener("change", (e) => { state.chipset = e.target.value; });
      wrap.append(chip);
    }
    /* 2. GPU */
    const gpu = el(`<div class="hw-card"><div class="hw-title">${icon("gpu")} 2. Ekran kartını seç (GPU) <b>*</b></div>
      <div class="brand-row">
        <button type="button" class="brand-btn nvidia${state.gpuBrand === "nvidia" ? " on" : ""}" data-brand="gpu:nvidia"><img src="assets/images/brands/nvidia.svg" alt="NVIDIA"></button>
        <button type="button" class="brand-btn radeon${state.gpuBrand === "radeon" ? " on" : ""}" data-brand="gpu:radeon"><img src="assets/images/brands/radeon.svg" alt="AMD Radeon"></button>
      </div>
      ${state.gpuBrand ? selectHtml(`${state.gpuBrand === "nvidia" ? "NVIDIA GeForce" : "AMD Radeon"} modelini seç...`, GPUS[state.gpuBrand], state.gpu, "anim-in") : ""}
    </div>`);
    wrap.append(gpu);
    /* 3. RAM */
    const ram = el(`<div class="hw-card"><div class="hw-title-row"><span class="hw-title">${icon("ram")} 3. RAM miktarını seç <b>*</b></span><span class="tag-mono">DDR5 / DDR4</span></div>
      <div class="ram-grid">${RAM.map(([v, sub]) => `<button type="button" class="ram${state.ram === v ? " on" : ""}" data-ram="${v}"><b>${v}</b><small>${sub}</small></button>`).join("")}</div></div>`);
    wrap.append(ram);
    /* Storage + Net */
    const extra = el(`<div class="hw-two">
      <div class="hw-card"><span class="hw-title small">Depolama türü <i>(isteğe bağlı)</i></span>${selectHtml("Disk türünü seç (isteğe bağlı)...", [["Depolama", STORAGE]], state.storage)}</div>
      <div class="hw-card"><span class="hw-title small">İnternet bağlantısı</span><div class="net-row">${NET.map((n) => `<button type="button" class="net${state.net === n ? " on" : ""}" data-net="${n}">${n.toUpperCase()}</button>`).join("")}</div></div>
    </div>`);
    wrap.append(extra);

    wrap.addEventListener("click", (e) => {
      const b = e.target.closest("[data-brand],[data-ram],[data-net]"); if (!b) return;
      error = "";
      if (b.dataset.brand) { const [k, v] = b.dataset.brand.split(":"); if (k === "cpu") { state.cpuBrand = v; state.cpu = ""; state.chipset = ""; } else { state.gpuBrand = v; state.gpu = ""; } render(); return; }
      if (b.dataset.ram) { state.ram = b.dataset.ram; wrap.querySelectorAll("[data-ram]").forEach((x) => x.classList.toggle("on", x.dataset.ram === state.ram)); }
      if (b.dataset.net) { state.net = b.dataset.net; wrap.querySelectorAll("[data-net]").forEach((x) => x.classList.toggle("on", x.dataset.net === state.net)); }
    });
    wrap.querySelectorAll("select").forEach((s) => s.addEventListener("change", (e) => {
      const ph = s.options[0].text;
      if (ph.includes("işlemci")) { state.cpu = e.target.value; state.chipset = ""; render(); }
      else if (ph.includes("modelini") ) { state.gpu = e.target.value; }
      else if (ph.includes("Disk")) { state.storage = e.target.value; }
    }));
    return wrap;
  }

  /* --- İletişim adımı --- */
  function renderContact() {
    const w = el(`<div class="contact-step">
      <div class="float"><input type="text" id="f-name" placeholder=" " value="${state.name}"><label for="f-name">Ad</label></div>
      <div class="float"><input type="email" id="f-email" placeholder=" " value="${state.email}"><label for="f-email">E-posta <small>(isteğe bağlı)</small></label></div>
      <div class="float"><input type="text" id="f-discord" placeholder=" " value="${state.discord}"><label for="f-discord">Discord kullanıcı adı <small>(isteğe bağlı)</small></label></div>
      <button type="button" class="consent${state.consent ? " on" : ""}">${neon(state.consent)}<span>Evet, FRAME sonuçlarım ve bilgisayarımı nasıl düzelteceğim hakkında bana yazabilir.</span></button>
    </div>`);
    w.querySelector("#f-name").addEventListener("input", (e) => { state.name = e.target.value; });
    w.querySelector("#f-email").addEventListener("input", (e) => { state.email = e.target.value; });
    w.querySelector("#f-discord").addEventListener("input", (e) => { state.discord = e.target.value; });
    const cb = w.querySelector(".consent");
    cb.addEventListener("click", () => { state.consent = !state.consent; cb.classList.toggle("on", state.consent); const n = cb.querySelector(".neon"); n.classList.toggle("on", state.consent); if (state.consent) { n.classList.add("burst"); setTimeout(() => n.classList.remove("burst"), 700); } const err = root.querySelector(".wz-error"); if (err) err.remove(); });
    return w;
  }

  /* --- Sonuç --- */
  function renderResult() {
    const r = result, R = RANGES[r.range], clear = r.range === "low", p = PACKS[r.pack];
    const radius = 42, circ = 2 * Math.PI * radius, off = circ - (r.score / 100) * circ;
    const tier = { flagship: "Amiral gemisi", high: "Üst seviye", mid: "Orta seviye", low: "Giriş / eski", custom: "Özel" }[r.gpuTier];
    const headroom = clear ? "Optimize" : r.range === "possible" ? "Orta" : "Yüksek potansiyel";
    const name = state.name.trim();
    const wrap = el(`<div class="res anim-in">
      <div class="res-top">
        <div class="gauge" style="--c:${R.color}">
          <svg viewBox="0 0 100 100"><circle class="g-bg" cx="50" cy="50" r="${radius}"/><circle class="g-val" cx="50" cy="50" r="${radius}" style="stroke-dasharray:${circ};stroke-dashoffset:${circ}" data-off="${off}"/></svg>
          <div class="g-num"><b>${r.score}</b><small>/ 100</small></div>
          <span class="g-label" style="color:${R.color};background:${R.color}1a;border-color:${R.color}40">${R.label}</span>
        </div>
        <div class="res-main">
          <span class="res-badge${clear ? " ok" : ""}">${clear ? "Her şey yolunda" : "Sonucun"}</span>
          <h3>${name ? name + ", " : ""}${clear ? "bilgisayarın gayet iyi durumda" : r.explain.toLowerCase()}</h3>
          <div class="res-tiles">
            <div><span>Donanım seviyesi</span><b>${tier}</b></div>
            <div><span>Kurulum dengesi</span><b class="blue">${r.laptop ? "Oyuncu dizüstü" : r.balance}</b></div>
            <div><span>Ayar payı</span><b class="${clear ? "ok" : "blue"}">${headroom}</b></div>
          </div>
          <div class="res-next">
            <span class="res-kicker">${clear ? "Değerlendirme özeti" : "Önerilen sonraki adım"}</span>
            <h4>${clear ? "Kritik darboğaz bulunmadı" : p.name}</h4>
            <p>${p.detail}</p>
          </div>
        </div>
      </div>
      <div class="res-actions">
        <button type="button" class="btn btn-ghost" data-open-list>${icon("doc")} Kontrol listesini aç</button>
        ${clear ? "" : `<a class="btn btn-primary" href="pricing.html">${p.name}'i incele ${icon("arrow")}</a>`}
        <button type="button" class="btn btn-ghost" data-copy-summary>${icon("copy")} Özeti kopyala</button>
        <a class="btn btn-ghost" href="#" data-discord>${icon("chat")} Discord'dan gönder</a>
        <span class="status" data-copy-status aria-live="polite"></span>
      </div>
      <p class="res-note">Puan bilgisayarında hesaplandı; hiçbir veri gönderilmedi. Kesin teşhis canlı oturumda yapılır.</p>
      <div class="wz-nav"><button type="button" class="btn btn-ghost btn-sm" data-restart>Baştan başla</button></div>
    </div>`);
    root.append(wrap);
    requestAnimationFrame(() => requestAnimationFrame(() => { const v = wrap.querySelector(".g-val"); v.style.strokeDashoffset = v.dataset.off; }));
    wrap.querySelector("[data-restart]").addEventListener("click", () => { result = null; step = 0; Object.assign(state, { game: "", problem: "", target: "", cpuBrand: "", cpu: "", chipset: "", gpuBrand: "", gpu: "", ram: "", storage: "", net: "", windows: "", tried: [], consent: false }); render(); scrollTo(); });
    wrap.querySelector("[data-open-list]").addEventListener("click", openModal);
    const d = wrap.querySelector("[data-discord]"); if (CFG.discord) { d.href = CFG.discord; d.target = "_blank"; d.rel = "noreferrer"; } else d.href = "contact.html";
    const status = wrap.querySelector("[data-copy-status]");
    const show = (m) => { status.textContent = m; status.classList.add("show"); setTimeout(() => status.classList.remove("show"), 2200); };
    wrap.querySelector("[data-copy-summary]").addEventListener("click", async () => {
      const text = summary();
      try { await navigator.clipboard.writeText(text); show("Kopyalandı"); }
      catch { const a = document.createElement("textarea"); a.value = text; document.body.append(a); a.select(); try { document.execCommand("copy"); show("Kopyalandı"); } catch { show("Kopyalanamadı"); } a.remove(); }
    });
  }

  function summary() {
    const r = result;
    return [`FRAME ücretsiz PC kontrolü — puan ${r.score}/100 (${RANGES[r.range].label})`,
      `Ad: ${state.name || "-"} | Discord: ${state.discord || "-"} | E-posta: ${state.email || "-"}`,
      `Oyun: ${state.game} | Sorun: ${state.problem} | Hedef: ${state.target}`,
      `CPU: ${state.cpu} (${state.cpuBrand}) | Yonga seti: ${state.chipset || "-"}`,
      `GPU: ${state.gpu} (${state.gpuBrand}) | RAM: ${state.ram} | Disk: ${state.storage || "-"} | Bağlantı: ${state.net || "-"}`,
      `Windows: ${state.windows} | Denenenler: ${state.tried.join(", ")}`,
      `Önerilen: ${PACKS[r.pack].name}`].join("\n");
  }

  function openModal() {
    const m = el(`<div class="modal" role="dialog" aria-modal="true" aria-label="Kontrol listesi"><div class="modal-bg"></div><div class="modal-panel">
      <div class="modal-head"><div><span class="res-kicker">Ücretsiz</span><h3>Optimizasyon kontrol listesi</h3></div><button type="button" class="modal-close" aria-label="Kapat">${icon("close")}</button></div>
      <div class="modal-body"><div class="modal-grid">${CHECKLIST.map(([t, items]) => `<section><h4>${t}</h4><ul>${items.map((x) => `<li>${icon("check")}<span>${x}</span></li>`).join("")}</ul></section>`).join("")}</div></div>
      <div class="modal-foot"><a class="btn btn-primary" href="contact.html">Yardım iste ${icon("arrow")}</a><button type="button" class="btn btn-ghost" data-close>Kapat</button></div>
    </div></div>`);
    const close = () => { m.remove(); document.body.style.overflow = ""; document.removeEventListener("keydown", onKey); };
    const onKey = (e) => { if (e.key === "Escape") close(); };
    m.querySelector(".modal-bg").addEventListener("click", close); m.querySelector(".modal-close").addEventListener("click", close); m.querySelector("[data-close]").addEventListener("click", close);
    document.addEventListener("keydown", onKey); document.body.style.overflow = "hidden"; document.body.append(m);
  }

  function scrollTo() { const r = root.getBoundingClientRect(); if (r.top < 70) window.scrollTo({ top: window.scrollY + r.top - 90, behavior: "smooth" }); }

  /* Derin bağlantı: #adim=4 ilgili adımı açar; #ornek örnek cevaplarla sonucu gösterir */
  const h = location.hash;
  const mStep = h.match(/adim=(\d)/);
  if (mStep) step = Math.min(6, Math.max(0, Number(mStep[1]) - 1));
  if (h.includes("ornek")) {
    Object.assign(state, { game: "Valorant", problem: "Takılmalar", target: "240 FPS, 1080p", cpuBrand: "intel", cpu: "Core i5-12400 / F", chipset: "B760 / B660 (Ana akım)", gpuBrand: "nvidia", gpu: "RTX 3060 / 3050", ram: "16GB", storage: "SATA 2.5\" SSD", net: "Wi-Fi", windows: "Windows 11", tried: ["GPU sürücülerini güncelledim", "Optimizer yazılımı kullandım"], name: "Örnek", consent: true });
    result = score();
  }
  render();
})();
