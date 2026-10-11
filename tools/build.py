# -*- coding: utf-8 -*-
"""FRAME sitesi: ortak üst/alt bilgi ile sayfaları üretir."""
import pathlib, json

OUT = pathlib.Path(__file__).resolve().parent.parent
SITE_URL = "https://frame.example"  # DÜZENLE: yayın adresi

def chip_art():
    return '''<div class="chip-art" aria-hidden="true"><svg viewBox="0 0 120 120" fill="none">
  <g stroke="rgba(255,255,255,.22)" stroke-width="3" stroke-linecap="round">
    <path d="M30 8v12M45 8v12M60 8v12M75 8v12M90 8v12M30 100v12M45 100v12M60 100v12M75 100v12M90 100v12M8 30h12M8 45h12M8 60h12M8 75h12M8 90h12M100 30h12M100 45h12M100 60h12M100 75h12M100 90h12"/>
  </g>
  <rect x="20" y="20" width="80" height="80" rx="12" fill="#15181e" stroke="rgba(255,255,255,.14)"/>
  <rect x="30" y="30" width="60" height="60" rx="9" fill="#0d0f13" stroke="var(--tier)" stroke-opacity=".5"/>
  <path d="M40 48v-5a3 3 0 0 1 3-3h5M72 40h5a3 3 0 0 1 3 3v5M80 72v5a3 3 0 0 1-3 3h-5M48 80h-5a3 3 0 0 1-3-3v-5" stroke="var(--tier)" stroke-width="2.2" stroke-linecap="round"/>
  <path d="M50 73V47h18v6H56.4v4.2H66v6h-9.6V73H50Z" fill="var(--tier)"/>
</svg></div>'''

def icon(name, cls="icon"):
    return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'

def head(title, desc, slug):
    url = f"{SITE_URL}/{slug}"
    return f"""<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="theme-color" content="#0b0c0f">
  <title>{title}</title>
  <!-- DÜZENLE: Arama sonuçlarında görünen açıklama -->
  <meta name="description" content="{desc}">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="FRAME">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{SITE_URL}/assets/images/og.png">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="icon" href="favicon.svg" type="image/svg+xml">
  <link rel="apple-touch-icon" href="assets/images/apple-touch-icon.png">
  <link rel="preload" href="assets/fonts/spacegrotesk-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="assets/fonts/spacegrotesk-latin-ext.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="assets/fonts/dmsans-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="assets/fonts/dmsans-latin-ext.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="assets/fonts/fonts.css">
  <link rel="stylesheet" href="assets/css/site.css">
  <script src="assets/js/icons.js"></script>
  <script src="assets/js/main.js" defer></script>
  <script src="assets/js/bench.js" defer></script>
</head>"""

def header():
    return f"""
  <a class="skip-link" href="#main">İçeriğe geç</a>
  <header class="header">
    <nav class="container nav" aria-label="Ana menü">
      <a class="brand" href="index.html" aria-label="FRAME ana sayfa">{icon("frame")}<span class="wordmark">FRAME</span></a>
      <div class="nav-links" id="nav-links">
        <a href="services.html">Hizmetler</a>
        <a href="process.html">Süreç</a>
        <a href="check.html">Ücretsiz kontrol</a>
        <a href="faq.html">Sorular</a>
        <a href="contact.html">İletişim</a>
      </div>
      <div class="nav-right">
        <a class="btn btn-primary btn-sm" href="pricing.html">Paketleri gör {icon("arrow")}</a>
        <button class="menu-toggle" type="button" aria-label="Menüyü aç" aria-expanded="false" aria-controls="nav-links">{icon("menu","icon icon-menu")}{icon("close","icon icon-close")}</button>
      </div>
    </nav>
  </header>"""

def footer():
    return f"""
  <footer>
    <div class="container footer-main">
      <a class="brand" href="index.html">{icon("frame")}FRAME</a>
      <nav class="footer-links" aria-label="Alt menü">
        <a href="services.html">Hizmetler</a><a href="process.html">Süreç</a><a href="pricing.html">Paketler</a><a href="check.html">Ücretsiz kontrol</a><a href="faq.html">Sorular</a><a href="contact.html">İletişim</a>
      </nav>
    </div>
    <div class="container footer-bottom">
      <span>© 2026 FRAME. Tüm hakları saklıdır.</span>
      <span>Sonuçlar donanıma ve kullanım koşullarına göre değişir.</span>
    </div>
  </footer>"""

def cta(label, title, text, btn="İletişime geç"):
    return f"""
    <section class="section-tight"><div class="container">
      <div class="cta corners">
        <div><span class="label">{label}</span><h2>{title}</h2><p>{text}</p></div>
        <a class="btn btn-primary" href="contact.html">{btn} {icon("arrow")}</a>
      </div>
    </div></section>"""

def page_hero(crumb, label, h1, lead):
    return f"""
    <section class="page-hero"><div class="glow glow-soft" aria-hidden="true"></div><div class="container">
      <div class="crumbs"><a href="index.html">Ana sayfa</a><span>/</span><span>{crumb}</span></div>
      <span class="label">{label}</span>
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
    </div></section>"""

def wrap(slug, title, desc, body, extra_head=""):
    html = head(title, desc, slug) + extra_head + f"""
<body data-page="{slug.replace('.html','').replace('index','home')}">{header()}
  <main id="main">{body}
  </main>{footer()}
</body>
</html>
"""
    (OUT / slug).write_text(html, encoding="utf-8")
    print("yazıldı:", slug)

# ---------------------------------------------------------------- ANA SAYFA
home = f"""
    <section class="hero hero-center"><div class="glow" aria-hidden="true"></div><div class="container hero-inner">
      <span class="label">Bilgisayarına özel optimizasyon</span>
      <h1>Daha fazla FPS.<br><em>Daha az gecikme.</em></h1>
      <p class="lead">Hazır script yok. Donanımına ve oyunlarına göre, ekranı canlı izlediğin bir oturumda yapılır.</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="pricing.html">Paketleri gör {icon("arrow")}</a>
        <a class="btn btn-ghost" href="check.html">Ücretsiz PC kontrolü</a>
      </div>
      <div class="stats">
        <div><b><span data-count="400">400</span> ₺</b><span>başlangıç fiyatı</span></div>
        <div><b>1–3 saat</b><span>oturum süresi</span></div>
        <div><b>Canlı</b><span>ekranı sen izlersin</span></div>
        <div><b>Geri alınabilir</b><span>her oturumda yedek</span></div>
      </div>
    </div></section>

    <section class="section-tight"><div class="container">
      <div class="badges">
        <span>{icon("shield")} Anti-cheat güvenli</span>
        <span>{icon("eye")} Ekranı canlı izle</span>
        <span>{icon("rollback")} Tamamen geri alınabilir</span>
        <span>{icon("lock")} Şifre ve dosya istenmez</span>
      </div>
    </div></section>

    <section class="section-tight">
      <div class="container"><div class="section-head center" style="margin-bottom:0"><h2>Oynadığın her oyunda <em>fark eder.</em></h2><span class="sub">Sistemi optimize ediyoruz, oyunu değil. Kazanım tüm oyunlara yansır.</span></div></div>
      <div class="covers" data-covers><div class="covers-track"><figure class="cover"><img src="assets/images/games/cs2.jpg" alt="Counter-Strike 2" loading="lazy"><figcaption>Counter-Strike 2 <small>FPS</small></figcaption></figure><figure class="cover"><img src="assets/images/games/valorant.jpg" alt="Valorant" loading="lazy"><figcaption>Valorant <small>FPS</small></figcaption></figure><figure class="cover"><img src="assets/images/games/fortnite.jpg" alt="Fortnite" loading="lazy"><figcaption>Fortnite <small>BR</small></figcaption></figure><figure class="cover"><img src="assets/images/games/rust.jpg" alt="Rust" loading="lazy"><figcaption>Rust <small>SURVIVAL</small></figcaption></figure><figure class="cover"><img src="assets/images/games/apex.jpg" alt="Apex Legends" loading="lazy"><figcaption>Apex Legends <small>BR</small></figcaption></figure><figure class="cover"><img src="assets/images/games/warzone.jpg" alt="Warzone" loading="lazy"><figcaption>Warzone <small>BR</small></figcaption></figure><figure class="cover"><img src="assets/images/games/pubg.jpg" alt="PUBG" loading="lazy"><figcaption>PUBG <small>BR</small></figcaption></figure><figure class="cover"><img src="assets/images/games/r6.jpg" alt="Rainbow Six Siege" loading="lazy"><figcaption>Rainbow Six Siege <small>FPS</small></figcaption></figure><figure class="cover"><img src="assets/images/games/finals.jpg" alt="The Finals" loading="lazy"><figcaption>The Finals <small>FPS</small></figcaption></figure><figure class="cover"><img src="assets/images/games/rivals.jpg" alt="Marvel Rivals" loading="lazy"><figcaption>Marvel Rivals <small>HERO</small></figcaption></figure><figure class="cover"><img src="assets/images/games/overwatch.jpg" alt="Overwatch 2" loading="lazy"><figcaption>Overwatch 2 <small>HERO</small></figcaption></figure><figure class="cover"><img src="assets/images/games/lol.jpg" alt="League of Legends" loading="lazy"><figcaption>League of Legends <small>MOBA</small></figcaption></figure><figure class="cover"><img src="assets/images/games/arena.jpg" alt="Arena Breakout" loading="lazy"><figcaption>Arena Breakout <small>FPS</small></figcaption></figure><figure class="cover"><img src="assets/images/games/dota.jpg" alt="Dota 2" loading="lazy"><figcaption>Dota 2 <small>MOBA</small></figcaption></figure><figure class="cover"><img src="assets/images/games/gta.jpg" alt="GTA V" loading="lazy"><figcaption>GTA V <small>OPEN WORLD</small></figcaption></figure></div></div>
    </section>

    <section class="section section-alt" id="sonuclar"><div class="container">
      <div class="section-head center"><h2>Gerçek kazanç, <em>gerçek kareler.</em></h2><span class="sub">Aynı PC, aynı sahne, aynı ayarlar. Stok ve optimize.</span></div>
      <div class="vb" data-bench>
        <div class="vb-tabs" role="tablist" aria-label="Oyun seç"></div>
        <div class="vb-grid">
          <div class="vb-video-col"><div class="vb-video card"></div><div class="vb-under"></div></div>
          <div class="vb-stats card"></div>
        </div>
        <div class="vb-strip card">
          <div>{icon("bolt")}<span>Tepkisellik</span><b>Tam</b></div><i></i>
          <div>{icon("test")}<span>Takılma</span><b>Yok</b></div><i></i>
          <div>{icon("gauge")}<span>Girdi gecikmesi</span><b>Minimum</b></div><i></i>
          <div>{icon("network")}<span>Ağ performansı</span><b>Kararlı</b></div><i></i>
          <div>{icon("thermo")}<span>Sıcaklıklar</span><b>Sağlıklı</b></div>
        </div>
        <p class="note center">Her kayıt aynı PC'de, aynı sahnede ve aynı ayarlarla, oturum öncesi ve sonrası alınır. Sonuçlar donanıma, oyuna ve ayarlara göre değişir.</p>
      </div>
    </div></section>

    <section class="section"><div class="container">
      <div class="section-head center"><span class="label">Neler yapılır?</span><h2>Üç alan, tek hedef: <em>akıcı oyun.</em></h2><span class="sub">Aynı bilgisayar, aynı oyun, daha tutarlı kare süresi</span></div>
      <div class="grid-3">
        <article class="feature corners"><span class="num">001</span><span class="icon-box">{icon("windows")}</span><h3>Windows ve sistem</h3><p>Gereksiz yükler, servisler ve güç planı temizlenir.</p></article>
        <article class="feature corners"><span class="num">002</span><span class="icon-box">{icon("gpu")}</span><h3>Sürücü ve oyun profili</h3><p>Ekran kartına ve oyunlarına göre yapılandırılır.</p></article>
        <article class="feature corners"><span class="num">003</span><span class="icon-box">{icon("bolt")}</span><h3>Gecikme ve kararlılık</h3><p>Girdi gecikmesi, ağ ve takılmalar hedeflenir.</p></article>
      </div>
    </div></section>

    <section class="section section-alt"><div class="container">
      <div class="section-head center"><h2>Üç adımda zirveye.</h2><span class="sub">Oturum ayarla, optimize ol, hükmet.</span></div>
      <div class="howtab">
        <div class="howtab-bar" role="tablist" aria-label="Üç adım">
          <button class="howtab-btn is-active" role="tab" aria-selected="true"><span class="howtab-n">Adım 1</span><span class="howtab-t">Kurulum ve hazırlık</span><i class="dots"></i><i class="prog"></i></button>
          <button class="howtab-btn" role="tab" aria-selected="false"><span class="howtab-n">Adım 2</span><span class="howtab-t">Optimizasyon süreci</span><i class="dots"></i><i class="prog"></i></button>
          <button class="howtab-btn" role="tab" aria-selected="false"><span class="howtab-n">Adım 3</span><span class="howtab-t">Oturumun tamamlanması</span><i class="dots"></i><i class="prog"></i></button>
        </div>
        <div class="howtab-stage">
          <div class="howtab-panel is-active" role="tabpanel">
            <div class="howtab-body">
              <h3 class="howtab-title">Kurulum ve hazırlık</h3>
              <p class="howtab-desc">Uygun bir saat seç ve randevunu al. Oturum öncesi adım adım hazırlık talimatlarını alırsın; ihtiyaç duyarsan hazırlanırken de yanında oluruz. Temiz bir temelde çalışmak için AnyDesk kurulu ve önemli dosyaların yedekli olmalı.</p>
              <div class="howtab-feats">
                <div class="sf-row"><span class="sf-ic">{icon("chat")}</span><div><b>Discord</b><small>Randevu ve hazırlık tek kanalda.</small></div></div>
                <div class="sf-row"><span class="sf-ic">{icon("doc")}</span><div><b>Hazırlık listesi</b><small>5 dakikada tamamlanır.</small></div></div>
              </div>
            </div>
            <div class="howtab-media"><div class="leak"></div><div class="scene s-phone" aria-hidden="true">
  <div class="vlines"><i></i><i></i></div>
  <div class="ph-cam"><div class="ph-flash"></div>
    <div class="phone">
      <i class="btn-side vol1"></i><i class="btn-side vol2"></i><i class="btn-side pwr"></i>
      <div class="phone-screen">
        <div class="wall"><i></i><i></i><i></i></div>
        <div class="island"></div>
        <div class="lock"><svg class="lock-ic" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round"><rect x="5" y="10" width="14" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg><b class="lock-site">frametweaks.com</b><small>Cuma, 14 Kasım</small></div>
        <div class="stack">
          <div class="notif n1"><div class="n-app cal"><svg viewBox="0 0 24 24" fill="none" stroke="#1b1403" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="5" width="18" height="16" rx="3"/><path d="M3 10h18M8 3v4M16 3v4"/></svg></div><div class="n-body"><div class="n-row"><b>Randevu alındı</b><small>şimdi</small></div></div></div>
          <div class="notif n2"><div class="n-app ok"><svg viewBox="0 0 24 24" fill="none" stroke="#1b1403" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg></div><div class="n-body"><div class="n-row"><b>Randevu onaylandı</b><small>şimdi</small></div></div></div>
          <div class="notif n3"><div class="n-app brand"><svg viewBox="0 0 48 48" fill="none"><path d="M6 16V10a4 4 0 0 1 4-4h6M32 6h6a4 4 0 0 1 4 4v6M42 32v6a4 4 0 0 1-4 4h-6M16 42h-6a4 4 0 0 1-4-4v-6" stroke="#e6b450" stroke-width="3" stroke-linecap="round"/><path d="M18 34V14h14v5h-8.6v3.4H30v5h-6.6V34H18Z" fill="#f2f1ec"/></svg></div><div class="n-body"><div class="n-row"><b>FRAME sana arkadaşlık isteği gönderdi.</b><small>şimdi</small></div><div class="n-btns"><i class="ok"><span class="tap"></span>Kabul</i><i class="ghost">Yoksay</i></div></div></div>
        </div>
        <div class="dock"><i><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 3h6l1 4-2 2v10a1 1 0 0 1-1 1h-2a1 1 0 0 1-1-1V9L8 7l1-4Z"/><path d="M12 12v4"/></svg></i><i><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 8a2 2 0 0 1 2-2h2l1.5-2h5L16 6h2a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V8Z"/><circle cx="12" cy="12.5" r="3.2"/></svg></i></div><div class="homebar"></div>
        <div class="glass"></div>
      </div>
    </div>
  </div>
</div></div>
          </div>
          <div class="howtab-panel" role="tabpanel" hidden>
            <div class="howtab-body">
              <h3 class="howtab-title">Optimizasyon süreci</h3>
              <p class="howtab-desc">AnyDesk ile uzaktan bağlanırız (oturum sonunda kapatırsın) ve Windows'unu, sürücülerini, pakete göre BIOS ve donanımını adım adım optimize ederiz. Ekranı canlı izlersin; onayın olmadan hiçbir ayar değişmez.</p>
              <div class="howtab-feats">
                <div class="sf-row"><span class="sf-ic">{icon("network")}</span><div><b>Ağ</b><small>Tam optimize. Her vuruş işler.</small></div></div>
                <div class="sf-row"><span class="sf-ic">{icon("bolt")}</span><div><b>Sıfır takılma</b><small>Oyun içi donmalar giderilir.</small></div></div>
              </div>
            </div>
            <div class="howtab-media"><div class="leak"></div><div class="scene s-board" aria-hidden="true">
  <div class="shot shot1"><div class="cam cam1"><svg viewBox="0 0 400 240" preserveAspectRatio="xMidYMid slice">
    <defs>
      <pattern id="ahex" width="14" height="12" patternUnits="userSpaceOnUse"><circle cx="7" cy="6" r="1.1" fill="rgba(255,255,255,.06)"/></pattern>
      <linearGradient id="atop" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2a2e38"/><stop offset="1" stop-color="#0f1115"/></linearGradient>
      <radialGradient id="adie" cx=".5" cy=".5" r=".6"><stop offset="0" stop-color="#e6b450" stop-opacity=".6"/><stop offset="1" stop-color="#e6b450" stop-opacity="0"/></radialGradient>
      
    </defs>
    <rect width="400" height="240" fill="#0b0d11"/><rect width="400" height="240" fill="url(#ahex)"/>
    <g><g transform="translate(231 143)"><rect x="2" y="3" width="51" height="28" rx="3" fill="#07080a"/><rect width="51" height="28" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="43" height="20" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(260 150)"><rect x="2" y="3" width="34" height="19" rx="3" fill="#07080a"/><rect width="34" height="19" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="26" height="11" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(262 121)"><rect x="2" y="3" width="62" height="33" rx="3" fill="#07080a"/><rect width="62" height="33" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="54" height="25" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(95 24)"><rect x="2" y="3" width="50" height="23" rx="3" fill="#07080a"/><rect width="50" height="23" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="42" height="15" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(72 23)"><rect x="2" y="3" width="56" height="39" rx="3" fill="#07080a"/><rect width="56" height="39" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="48" height="31" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(355 162)"><rect x="2" y="3" width="24" height="33" rx="3" fill="#07080a"/><rect width="24" height="33" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="16" height="25" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(202 115)"><rect x="2" y="3" width="63" height="37" rx="3" fill="#07080a"/><rect width="63" height="37" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="55" height="29" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(315 166)"><rect x="2" y="3" width="32" height="33" rx="3" fill="#07080a"/><rect width="32" height="33" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="24" height="25" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(7 135)"><rect x="2" y="3" width="26" height="15" rx="3" fill="#07080a"/><rect width="26" height="15" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="18" height="7" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(18 48)"><rect x="2" y="3" width="37" height="33" rx="3" fill="#07080a"/><rect width="37" height="33" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="29" height="25" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(15 199)"><rect x="2" y="3" width="51" height="24" rx="3" fill="#07080a"/><rect width="51" height="24" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="43" height="16" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(225 151)"><rect x="2" y="3" width="34" height="30" rx="3" fill="#07080a"/><rect width="34" height="30" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="26" height="22" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(119 163)"><rect x="2" y="3" width="40" height="29" rx="3" fill="#07080a"/><rect width="40" height="29" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="32" height="21" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(2 169)"><rect x="2" y="3" width="27" height="28" rx="3" fill="#07080a"/><rect width="27" height="28" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="19" height="20" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(335 71)"><rect x="2" y="3" width="48" height="31" rx="3" fill="#07080a"/><rect width="48" height="31" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="40" height="23" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(42 181)"><rect x="2" y="3" width="38" height="24" rx="3" fill="#07080a"/><rect width="38" height="24" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="30" height="16" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(117 131)"><rect x="2" y="3" width="40" height="14" rx="3" fill="#07080a"/><rect width="40" height="14" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="32" height="6" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(35 144)"><rect x="2" y="3" width="28" height="26" rx="3" fill="#07080a"/><rect width="28" height="26" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="20" height="18" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g></g><g><rect x="55" y="216" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="148" y="98" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="34" y="4" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="350" y="0" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="109" y="53" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="26" y="120" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="192" y="181" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="203" y="107" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="37" y="144" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="322" y="50" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="345" y="69" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="172" y="22" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="159" y="85" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="7" y="104" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="388" y="30" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="68" y="63" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="361" y="25" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="5" y="15" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="238" y="204" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="249" y="45" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="349" y="143" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="96" y="114" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="260" y="48" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="374" y="196" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="67" y="107" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="329" y="98" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="59" y="101" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="215" y="54" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="0" y="69" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="303" y="77" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="10" y="53" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="95" y="100" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="308" y="164" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="295" y="25" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="21" y="37" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="109" y="113" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="132" y="2" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="312" y="84" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="151" y="98" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="37" y="19" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="46" y="53" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="298" y="162" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="124" y="3" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="307" y="94" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="190" y="159" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="232" y="32" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="300" y="123" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="294" y="34" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="197" y="46" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="321" y="39" width="5" height="3" rx="1" fill="#2c2f37"/></g><g><g transform="translate(339 179)"><circle r="7" fill="#0a0b0e"/><circle r="6" fill="#1d2027" stroke="rgba(255,255,255,.12)"/><circle r="2.5" fill="#0a0b0e"/></g><g transform="translate(378 181)"><circle r="7" fill="#0a0b0e"/><circle r="6" fill="#1d2027" stroke="rgba(255,255,255,.12)"/><circle r="2.5" fill="#0a0b0e"/></g><g transform="translate(324 170)"><circle r="7" fill="#0a0b0e"/><circle r="6" fill="#1d2027" stroke="rgba(255,255,255,.12)"/><circle r="2.5" fill="#0a0b0e"/></g><g transform="translate(380 220)"><circle r="7" fill="#0a0b0e"/><circle r="6" fill="#1d2027" stroke="rgba(255,255,255,.12)"/><circle r="2.5" fill="#0a0b0e"/></g></g>
    <g fill="none" stroke="rgba(255,255,255,.09)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M0 60 H60 L80 80 H134"/><path d="M0 170 H70 L90 150 H134"/><path d="M266 100 H330 L350 80 H400"/><path d="M266 140 H320 L340 160 H400"/><path d="M200 0 V40 L220 60 V84"/><path d="M180 156 V200 L160 220 V240"/><path d="M40 240 V200 L60 180 H100 V156"/><path d="M360 0 V30 L340 50 V84 H266"/><path d="M0 110 H100 L120 120 H134"/><path d="M266 120 H300 L320 100 V40 H400"/><path d="M120 0 V30 L140 50 V84"/><path d="M300 240 V190 L280 170 V156"/><path d="M0 20 H400"/><path d="M0 215 H400"/></g>
    <g class="b-glow b-glow-soft" fill="none" stroke="rgba(230,180,80,.35)" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"><path d="M0 60 H60 L80 80 H134" style="animation-delay:0.00s"/><path d="M0 170 H70 L90 150 H134" style="animation-delay:0.33s"/><path d="M266 100 H330 L350 80 H400" style="animation-delay:0.66s"/><path d="M266 140 H320 L340 160 H400" style="animation-delay:0.99s"/><path d="M200 0 V40 L220 60 V84" style="animation-delay:1.32s"/><path d="M180 156 V200 L160 220 V240" style="animation-delay:1.65s"/><path d="M40 240 V200 L60 180 H100 V156" style="animation-delay:1.98s"/><path d="M360 0 V30 L340 50 V84 H266" style="animation-delay:2.31s"/><path d="M0 110 H100 L120 120 H134" style="animation-delay:2.64s"/><path d="M266 120 H300 L320 100 V40 H400" style="animation-delay:2.97s"/><path d="M120 0 V30 L140 50 V84" style="animation-delay:3.30s"/><path d="M300 240 V190 L280 170 V156" style="animation-delay:3.63s"/><path d="M0 20 H400" style="animation-delay:3.96s"/><path d="M0 215 H400" style="animation-delay:4.29s"/></g><g class="b-glow" fill="none" stroke="#ffd88a" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M0 60 H60 L80 80 H134" style="animation-delay:0.00s"/><path d="M0 170 H70 L90 150 H134" style="animation-delay:0.33s"/><path d="M266 100 H330 L350 80 H400" style="animation-delay:0.66s"/><path d="M266 140 H320 L340 160 H400" style="animation-delay:0.99s"/><path d="M200 0 V40 L220 60 V84" style="animation-delay:1.32s"/><path d="M180 156 V200 L160 220 V240" style="animation-delay:1.65s"/><path d="M40 240 V200 L60 180 H100 V156" style="animation-delay:1.98s"/><path d="M360 0 V30 L340 50 V84 H266" style="animation-delay:2.31s"/><path d="M0 110 H100 L120 120 H134" style="animation-delay:2.64s"/><path d="M266 120 H300 L320 100 V40 H400" style="animation-delay:2.97s"/><path d="M120 0 V30 L140 50 V84" style="animation-delay:3.30s"/><path d="M300 240 V190 L280 170 V156" style="animation-delay:3.63s"/><path d="M0 20 H400" style="animation-delay:3.96s"/><path d="M0 215 H400" style="animation-delay:4.29s"/></g>
    <g><rect x="147" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="147" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="155" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="155" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="163" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="163" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="171" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="171" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="179" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="179" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="187" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="187" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="195" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="195" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="203" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="203" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="211" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="211" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="219" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="219" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="227" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="227" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="235" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="235" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="243" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="243" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="251" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="251" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="134" y="92" width="8" height="3" fill="#9aa0aa"/><rect x="258" y="92" width="8" height="3" fill="#9aa0aa"/><rect x="134" y="100" width="8" height="3" fill="#9aa0aa"/><rect x="258" y="100" width="8" height="3" fill="#9aa0aa"/><rect x="134" y="108" width="8" height="3" fill="#9aa0aa"/><rect x="258" y="108" width="8" height="3" fill="#9aa0aa"/><rect x="134" y="116" width="8" height="3" fill="#9aa0aa"/><rect x="258" y="116" width="8" height="3" fill="#9aa0aa"/><rect x="134" y="124" width="8" height="3" fill="#9aa0aa"/><rect x="258" y="124" width="8" height="3" fill="#9aa0aa"/><rect x="134" y="132" width="8" height="3" fill="#9aa0aa"/><rect x="258" y="132" width="8" height="3" fill="#9aa0aa"/><rect x="134" y="140" width="8" height="3" fill="#9aa0aa"/><rect x="258" y="140" width="8" height="3" fill="#9aa0aa"/></g>
    <rect x="140" y="92" width="120" height="68" rx="6" fill="#030304"/>
    <rect class="b-chip" x="140" y="86" width="120" height="68" rx="6" fill="url(#atop)" stroke="rgba(255,255,255,.12)"/>
    <rect x="166" y="100" width="68" height="40" rx="4" fill="#0a0b0e" stroke="rgba(230,180,80,.5)"/>
    <rect x="166" y="100" width="68" height="40" rx="4" fill="url(#adie)" class="b-die"/>
    <g transform="translate(184 104) scale(.68)" fill="none"><path d="M6 16V10a4 4 0 0 1 4-4h6M32 6h6a4 4 0 0 1 4 4v6M42 32v6a4 4 0 0 1-4 4h-6M16 42h-6a4 4 0 0 1-4-4v-6" stroke="#e6b450" stroke-width="2.4" stroke-linecap="round"/><path d="M18 34V14h14v5h-8.6v3.4H30v5h-6.6V34H18Z" fill="#f2f1ec"/></g>
  </svg></div></div>
  <div class="shot shot2"><div class="biglogo"><div class="bl-face"><svg viewBox="0 0 48 48" fill="none"><path d="M6 16V10a4 4 0 0 1 4-4h6M32 6h6a4 4 0 0 1 4 4v6M42 32v6a4 4 0 0 1-4 4h-6M16 42h-6a4 4 0 0 1-4-4v-6" stroke="#e6b450" stroke-width="2.4" stroke-linecap="round"/><path d="M18 34V14h14v5h-8.6v3.4H30v5h-6.6V34H18Z" fill="#f2f1ec"/></svg></div><div class="bl-side"></div></div></div>
  <div class="shot shot3"><div class="cam cam3"><svg viewBox="0 0 400 240" preserveAspectRatio="xMidYMid slice">
    <defs>
      <pattern id="bhex" width="14" height="12" patternUnits="userSpaceOnUse"><circle cx="7" cy="6" r="1.1" fill="rgba(255,255,255,.06)"/></pattern>
      <linearGradient id="btop" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2a2e38"/><stop offset="1" stop-color="#0f1115"/></linearGradient>
      <radialGradient id="bdie" cx=".5" cy=".5" r=".6"><stop offset="0" stop-color="#e6b450" stop-opacity=".6"/><stop offset="1" stop-color="#e6b450" stop-opacity="0"/></radialGradient>
      
    </defs>
    <rect width="400" height="240" fill="#0b0d11"/><rect width="400" height="240" fill="url(#bhex)"/>
    <g><g transform="translate(100 175)"><rect x="2" y="3" width="46" height="29" rx="3" fill="#07080a"/><rect width="46" height="29" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="38" height="21" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(309 20)"><rect x="2" y="3" width="48" height="15" rx="3" fill="#07080a"/><rect width="48" height="15" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="40" height="7" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(53 27)"><rect x="2" y="3" width="24" height="30" rx="3" fill="#07080a"/><rect width="24" height="30" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="16" height="22" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(130 61)"><rect x="2" y="3" width="47" height="22" rx="3" fill="#07080a"/><rect width="47" height="22" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="39" height="14" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(215 210)"><rect x="2" y="3" width="60" height="29" rx="3" fill="#07080a"/><rect width="60" height="29" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="52" height="21" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(150 133)"><rect x="2" y="3" width="33" height="37" rx="3" fill="#07080a"/><rect width="33" height="37" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="25" height="29" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(35 32)"><rect x="2" y="3" width="36" height="29" rx="3" fill="#07080a"/><rect width="36" height="29" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="28" height="21" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(286 167)"><rect x="2" y="3" width="61" height="33" rx="3" fill="#07080a"/><rect width="61" height="33" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="53" height="25" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(37 71)"><rect x="2" y="3" width="35" height="20" rx="3" fill="#07080a"/><rect width="35" height="20" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="27" height="12" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(8 17)"><rect x="2" y="3" width="39" height="27" rx="3" fill="#07080a"/><rect width="39" height="27" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="31" height="19" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(228 63)"><rect x="2" y="3" width="25" height="15" rx="3" fill="#07080a"/><rect width="25" height="15" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="17" height="7" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(90 72)"><rect x="2" y="3" width="45" height="30" rx="3" fill="#07080a"/><rect width="45" height="30" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="37" height="22" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(292 33)"><rect x="2" y="3" width="27" height="25" rx="3" fill="#07080a"/><rect width="27" height="25" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="19" height="17" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(70 115)"><rect x="2" y="3" width="43" height="35" rx="3" fill="#07080a"/><rect width="43" height="35" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="35" height="27" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(353 133)"><rect x="2" y="3" width="59" height="18" rx="3" fill="#07080a"/><rect width="59" height="18" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="51" height="10" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(302 8)"><rect x="2" y="3" width="23" height="29" rx="3" fill="#07080a"/><rect width="23" height="29" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="15" height="21" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(183 179)"><rect x="2" y="3" width="41" height="15" rx="3" fill="#07080a"/><rect width="41" height="15" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="33" height="7" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g><g transform="translate(10 153)"><rect x="2" y="3" width="62" height="16" rx="3" fill="#07080a"/><rect width="62" height="16" rx="3" fill="#171a21" stroke="rgba(255,255,255,.08)"/><rect x="4" y="4" width="54" height="8" rx="2" fill="none" stroke="rgba(255,255,255,.05)"/></g></g><g><rect x="246" y="17" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="374" y="79" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="163" y="34" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="37" y="19" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="231" y="139" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="188" y="188" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="22" y="230" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="377" y="188" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="360" y="33" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="174" y="90" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="43" y="175" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="242" y="230" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="39" y="223" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="213" y="202" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="15" y="221" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="255" y="146" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="7" y="159" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="339" y="97" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="194" y="149" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="6" y="155" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="36" y="20" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="46" y="163" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="59" y="65" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="213" y="186" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="169" y="99" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="376" y="177" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="297" y="117" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="225" y="118" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="277" y="21" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="265" y="192" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="263" y="7" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="158" y="153" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="44" y="123" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="11" y="58" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="357" y="28" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="254" y="199" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="314" y="168" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="248" y="65" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="5" y="94" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="154" y="36" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="347" y="156" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="103" y="132" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="86" y="192" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="175" y="168" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="226" y="127" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="123" y="83" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="207" y="170" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="128" y="50" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="324" y="110" width="5" height="3" rx="1" fill="#2c2f37"/><rect x="386" y="51" width="5" height="3" rx="1" fill="#2c2f37"/></g><g><g transform="translate(327 199)"><circle r="7" fill="#0a0b0e"/><circle r="6" fill="#1d2027" stroke="rgba(255,255,255,.12)"/><circle r="2.5" fill="#0a0b0e"/></g><g transform="translate(328 190)"><circle r="7" fill="#0a0b0e"/><circle r="6" fill="#1d2027" stroke="rgba(255,255,255,.12)"/><circle r="2.5" fill="#0a0b0e"/></g><g transform="translate(326 167)"><circle r="7" fill="#0a0b0e"/><circle r="6" fill="#1d2027" stroke="rgba(255,255,255,.12)"/><circle r="2.5" fill="#0a0b0e"/></g><g transform="translate(317 213)"><circle r="7" fill="#0a0b0e"/><circle r="6" fill="#1d2027" stroke="rgba(255,255,255,.12)"/><circle r="2.5" fill="#0a0b0e"/></g></g>
    <g fill="none" stroke="rgba(255,255,255,.09)" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M0 60 H60 L80 80 H134"/><path d="M0 170 H70 L90 150 H134"/><path d="M266 100 H330 L350 80 H400"/><path d="M266 140 H320 L340 160 H400"/><path d="M200 0 V40 L220 60 V84"/><path d="M180 156 V200 L160 220 V240"/><path d="M40 240 V200 L60 180 H100 V156"/><path d="M360 0 V30 L340 50 V84 H266"/><path d="M0 110 H100 L120 120 H134"/><path d="M266 120 H300 L320 100 V40 H400"/><path d="M120 0 V30 L140 50 V84"/><path d="M300 240 V190 L280 170 V156"/><path d="M0 20 H400"/><path d="M0 215 H400"/></g>
    <g class="b-glow b-glow-soft" fill="none" stroke="rgba(230,180,80,.35)" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"><path d="M0 60 H60 L80 80 H134" style="animation-delay:0.00s"/><path d="M0 170 H70 L90 150 H134" style="animation-delay:0.33s"/><path d="M266 100 H330 L350 80 H400" style="animation-delay:0.66s"/><path d="M266 140 H320 L340 160 H400" style="animation-delay:0.99s"/><path d="M200 0 V40 L220 60 V84" style="animation-delay:1.32s"/><path d="M180 156 V200 L160 220 V240" style="animation-delay:1.65s"/><path d="M40 240 V200 L60 180 H100 V156" style="animation-delay:1.98s"/><path d="M360 0 V30 L340 50 V84 H266" style="animation-delay:2.31s"/><path d="M0 110 H100 L120 120 H134" style="animation-delay:2.64s"/><path d="M266 120 H300 L320 100 V40 H400" style="animation-delay:2.97s"/><path d="M120 0 V30 L140 50 V84" style="animation-delay:3.30s"/><path d="M300 240 V190 L280 170 V156" style="animation-delay:3.63s"/><path d="M0 20 H400" style="animation-delay:3.96s"/><path d="M0 215 H400" style="animation-delay:4.29s"/></g><g class="b-glow" fill="none" stroke="#ffd88a" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M0 60 H60 L80 80 H134" style="animation-delay:0.00s"/><path d="M0 170 H70 L90 150 H134" style="animation-delay:0.33s"/><path d="M266 100 H330 L350 80 H400" style="animation-delay:0.66s"/><path d="M266 140 H320 L340 160 H400" style="animation-delay:0.99s"/><path d="M200 0 V40 L220 60 V84" style="animation-delay:1.32s"/><path d="M180 156 V200 L160 220 V240" style="animation-delay:1.65s"/><path d="M40 240 V200 L60 180 H100 V156" style="animation-delay:1.98s"/><path d="M360 0 V30 L340 50 V84 H266" style="animation-delay:2.31s"/><path d="M0 110 H100 L120 120 H134" style="animation-delay:2.64s"/><path d="M266 120 H300 L320 100 V40 H400" style="animation-delay:2.97s"/><path d="M120 0 V30 L140 50 V84" style="animation-delay:3.30s"/><path d="M300 240 V190 L280 170 V156" style="animation-delay:3.63s"/><path d="M0 20 H400" style="animation-delay:3.96s"/><path d="M0 215 H400" style="animation-delay:4.29s"/></g>
    <g><rect x="147" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="147" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="155" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="155" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="163" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="163" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="171" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="171" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="179" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="179" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="187" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="187" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="195" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="195" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="203" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="203" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="211" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="211" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="219" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="219" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="227" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="227" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="235" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="235" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="243" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="243" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="251" y="78" width="3" height="8" fill="#9aa0aa"/><rect x="251" y="154" width="3" height="8" fill="#9aa0aa"/><rect x="134" y="92" width="8" height="3" fill="#9aa0aa"/><rect x="258" y="92" width="8" height="3" fill="#9aa0aa"/><rect x="134" y="100" width="8" height="3" fill="#9aa0aa"/><rect x="258" y="100" width="8" height="3" fill="#9aa0aa"/><rect x="134" y="108" width="8" height="3" fill="#9aa0aa"/><rect x="258" y="108" width="8" height="3" fill="#9aa0aa"/><rect x="134" y="116" width="8" height="3" fill="#9aa0aa"/><rect x="258" y="116" width="8" height="3" fill="#9aa0aa"/><rect x="134" y="124" width="8" height="3" fill="#9aa0aa"/><rect x="258" y="124" width="8" height="3" fill="#9aa0aa"/><rect x="134" y="132" width="8" height="3" fill="#9aa0aa"/><rect x="258" y="132" width="8" height="3" fill="#9aa0aa"/><rect x="134" y="140" width="8" height="3" fill="#9aa0aa"/><rect x="258" y="140" width="8" height="3" fill="#9aa0aa"/></g>
    <rect x="140" y="92" width="120" height="68" rx="6" fill="#030304"/>
    <rect class="b-chip" x="140" y="86" width="120" height="68" rx="6" fill="url(#btop)" stroke="rgba(255,255,255,.12)"/>
    <rect x="166" y="100" width="68" height="40" rx="4" fill="#0a0b0e" stroke="rgba(230,180,80,.5)"/>
    <rect x="166" y="100" width="68" height="40" rx="4" fill="url(#bdie)" class="b-die"/>
    <g transform="translate(184 104) scale(.68)" fill="none"><path d="M6 16V10a4 4 0 0 1 4-4h6M32 6h6a4 4 0 0 1 4 4v6M42 32v6a4 4 0 0 1-4 4h-6M16 42h-6a4 4 0 0 1-4-4v-6" stroke="#e6b450" stroke-width="2.4" stroke-linecap="round"/><path d="M18 34V14h14v5h-8.6v3.4H30v5h-6.6V34H18Z" fill="#f2f1ec"/></g>
  </svg></div><div class="hud"><span style="--i:0"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Güç planı</span><span style="--i:1"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Sürücüler</span><span style="--i:2"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Ağ ve gecikme</span><span style="--i:3"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>BIOS</span></div></div>
  <div class="fade"></div>
</div></div>
          </div>
          <div class="howtab-panel" role="tabpanel" hidden>
            <div class="howtab-body">
              <h3 class="howtab-title">Oturumun tamamlanması</h3>
              <p class="howtab-desc">Aynı sahnede, aynı ayarlarla önce/sonra karşılaştırması yapılır. Değişiklik özeti ve geri alma adımları sende kalır; takip desteği süresince sorularına cevap veririz.</p>
              <div class="howtab-feats">
                <div class="sf-row"><span class="sf-ic">{icon("test")}</span><div><b>Önce / sonra</b><small>Aynı koşullarda ölçüm.</small></div></div>
                <div class="sf-row"><span class="sf-ic">{icon("rollback")}</span><div><b>Oturum raporu</b><small>Her değişiklik yazılı.</small></div></div>
              </div>
            </div>
            <div class="howtab-media"><div class="leak"></div><div class="scene s-gauge" aria-hidden="true">
  <div class="g-swirl"></div>
  <div class="fps-hud"><span>FPS</span><b class="g-digit">0</b><i></i></div>
  <div class="g-wrap"><div class="g-cam">
  <svg viewBox="0 0 200 200">
    <defs>
      <linearGradient id="rim" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f4f4f4"/><stop offset=".25" stop-color="#8e9298"/><stop offset=".5" stop-color="#e8e8ea"/><stop offset=".75" stop-color="#5c6066"/><stop offset="1" stop-color="#d8d8da"/></linearGradient>
      <linearGradient id="rim2" x1="1" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3a3d43"/><stop offset="1" stop-color="#15161a"/></linearGradient>
      <radialGradient id="face" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#2a1d08"/><stop offset=".45" stop-color="#15151a"/><stop offset="1" stop-color="#0a0a0c"/></radialGradient>
      <radialGradient id="core" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#e6b450" stop-opacity=".95"/><stop offset=".6" stop-color="#8a5c14" stop-opacity=".5"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
      <linearGradient id="needleG" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#f2f1ec"/><stop offset=".5" stop-color="#e6b450"/><stop offset="1" stop-color="#ff9a3c"/></linearGradient>
      <radialGradient id="cap" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#fff"/><stop offset=".4" stop-color="#9a9ca3"/><stop offset="1" stop-color="#2b2d33"/></radialGradient>
      <filter id="nglow"><feGaussianBlur stdDeviation="1.6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
      <filter id="arcglow"><feGaussianBlur stdDeviation="2.5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
    </defs>
    <circle cx="100" cy="100" r="99" fill="url(#rim)"/>
    <circle cx="100" cy="100" r="95" fill="url(#rim2)"/>
    <circle cx="100" cy="100" r="93" fill="#0b0b0d"/>
    <circle cx="100" cy="100" r="91" fill="url(#face)"/>
    <path d="M26.5 161.7 A96 96 0 1 1 173.5 161.7" fill="none" stroke="rgba(255,255,255,.08)" stroke-width="3"/>
    <path class="g-arc" style="display:none" d="M26.5 161.7 A96 96 0 1 1 173.5 161.7" fill="none" stroke="#e6b450" stroke-width="3" stroke-linecap="round" filter="url(#arcglow)" style="stroke-dasharray:435.6;stroke-dashoffset:435.6"/>
    <path d="M188.0 81.3 A90 90 0 0 1 168.9 157.9" fill="none" stroke="#e6b450" stroke-width="5" opacity=".75"/>
    <g stroke="#f2f1ec"><line x1="38.7" y1="151.4" x2="29.5" y2="159.1" stroke-width="1.8" opacity="1"/><line x1="30.1" y1="153.4" x2="26.9" y2="155.9" stroke-width="0.6" opacity="0.5"/><line x1="27.7" y1="150.2" x2="24.5" y2="152.5" stroke-width="0.6" opacity="0.5"/><line x1="25.5" y1="146.9" x2="22.2" y2="149.0" stroke-width="0.6" opacity="0.5"/><line x1="23.5" y1="143.5" x2="20.0" y2="145.4" stroke-width="0.6" opacity="0.5"/><line x1="24.3" y1="138.6" x2="18.0" y2="141.8" stroke-width="1" opacity="0.8"/><line x1="19.9" y1="136.4" x2="16.2" y2="138.0" stroke-width="0.6" opacity="0.5"/><line x1="18.3" y1="132.7" x2="14.6" y2="134.2" stroke-width="0.6" opacity="0.5"/><line x1="16.9" y1="128.9" x2="13.1" y2="130.3" stroke-width="0.6" opacity="0.5"/><line x1="15.7" y1="125.1" x2="11.8" y2="126.3" stroke-width="0.6" opacity="0.5"/><line x1="22.4" y1="119.4" x2="10.7" y2="122.3" stroke-width="1.8" opacity="1"/><line x1="13.7" y1="117.4" x2="9.8" y2="118.2" stroke-width="0.6" opacity="0.5"/><line x1="13.0" y1="113.5" x2="9.1" y2="114.1" stroke-width="0.6" opacity="0.5"/><line x1="12.5" y1="109.5" x2="8.5" y2="109.9" stroke-width="0.6" opacity="0.5"/><line x1="12.2" y1="105.5" x2="8.2" y2="105.8" stroke-width="0.6" opacity="0.5"/><line x1="15.0" y1="101.5" x2="8.0" y2="101.6" stroke-width="1" opacity="0.8"/><line x1="12.0" y1="97.5" x2="8.0" y2="97.4" stroke-width="0.6" opacity="0.5"/><line x1="12.2" y1="93.6" x2="8.2" y2="93.3" stroke-width="0.6" opacity="0.5"/><line x1="12.6" y1="89.6" x2="8.6" y2="89.1" stroke-width="0.6" opacity="0.5"/><line x1="13.2" y1="85.6" x2="9.2" y2="85.0" stroke-width="0.6" opacity="0.5"/><line x1="21.7" y1="83.4" x2="10.0" y2="80.9" stroke-width="1.8" opacity="1"/><line x1="14.8" y1="77.8" x2="11.0" y2="76.8" stroke-width="0.6" opacity="0.5"/><line x1="15.9" y1="74.0" x2="12.1" y2="72.8" stroke-width="0.6" opacity="0.5"/><line x1="17.2" y1="70.2" x2="13.4" y2="68.8" stroke-width="0.6" opacity="0.5"/><line x1="18.6" y1="66.5" x2="14.9" y2="64.9" stroke-width="0.6" opacity="0.5"/><line x1="23.0" y1="64.1" x2="16.6" y2="61.1" stroke-width="1" opacity="0.8"/><line x1="22.0" y1="59.2" x2="18.5" y2="57.4" stroke-width="0.6" opacity="0.5"/><line x1="23.9" y1="55.7" x2="20.5" y2="53.7" stroke-width="0.6" opacity="0.5"/><line x1="26.0" y1="52.3" x2="22.7" y2="50.2" stroke-width="0.6" opacity="0.5"/><line x1="28.3" y1="49.0" x2="25.0" y2="46.7" stroke-width="0.6" opacity="0.5"/><line x1="37.0" y1="50.7" x2="27.5" y2="43.4" stroke-width="1.8" opacity="1"/><line x1="33.2" y1="42.7" x2="30.1" y2="40.1" stroke-width="0.6" opacity="0.5"/><line x1="35.9" y1="39.8" x2="32.9" y2="37.0" stroke-width="0.6" opacity="0.5"/><line x1="38.6" y1="36.9" x2="35.9" y2="34.0" stroke-width="0.6" opacity="0.5"/><line x1="41.6" y1="34.2" x2="38.9" y2="31.2" stroke-width="0.6" opacity="0.5"/><line x1="46.5" y1="33.9" x2="42.1" y2="28.5" stroke-width="1" opacity="0.8"/><line x1="47.8" y1="29.2" x2="45.4" y2="25.9" stroke-width="0.6" opacity="0.5"/><line x1="51.0" y1="26.9" x2="48.8" y2="23.5" stroke-width="0.6" opacity="0.5"/><line x1="54.4" y1="24.7" x2="52.3" y2="21.3" stroke-width="0.6" opacity="0.5"/><line x1="57.9" y1="22.7" x2="56.0" y2="19.2" stroke-width="0.6" opacity="0.5"/><line x1="64.9" y1="28.1" x2="59.7" y2="17.3" stroke-width="1.8" opacity="1"/><line x1="65.1" y1="19.2" x2="63.5" y2="15.6" stroke-width="0.6" opacity="0.5"/><line x1="68.8" y1="17.7" x2="67.3" y2="14.0" stroke-width="0.6" opacity="0.5"/><line x1="72.5" y1="16.4" x2="71.3" y2="12.6" stroke-width="0.6" opacity="0.5"/><line x1="76.3" y1="15.2" x2="75.3" y2="11.4" stroke-width="0.6" opacity="0.5"/><line x1="80.9" y1="17.2" x2="79.3" y2="10.4" stroke-width="1" opacity="0.8"/><line x1="84.1" y1="13.4" x2="83.4" y2="9.5" stroke-width="0.6" opacity="0.5"/><line x1="88.1" y1="12.8" x2="87.5" y2="8.9" stroke-width="0.6" opacity="0.5"/><line x1="92.0" y1="12.4" x2="91.7" y2="8.4" stroke-width="0.6" opacity="0.5"/><line x1="96.0" y1="12.1" x2="95.8" y2="8.1" stroke-width="0.6" opacity="0.5"/><line x1="100.0" y1="20.0" x2="100.0" y2="8.0" stroke-width="1.8" opacity="1"/><line x1="104.0" y1="12.1" x2="104.2" y2="8.1" stroke-width="0.6" opacity="0.5"/><line x1="108.0" y1="12.4" x2="108.3" y2="8.4" stroke-width="0.6" opacity="0.5"/><line x1="111.9" y1="12.8" x2="112.5" y2="8.9" stroke-width="0.6" opacity="0.5"/><line x1="115.9" y1="13.4" x2="116.6" y2="9.5" stroke-width="0.6" opacity="0.5"/><line x1="119.1" y1="17.2" x2="120.7" y2="10.4" stroke-width="1" opacity="0.8"/><line x1="123.7" y1="15.2" x2="124.7" y2="11.4" stroke-width="0.6" opacity="0.5"/><line x1="127.5" y1="16.4" x2="128.7" y2="12.6" stroke-width="0.6" opacity="0.5"/><line x1="131.2" y1="17.7" x2="132.7" y2="14.0" stroke-width="0.6" opacity="0.5"/><line x1="134.9" y1="19.2" x2="136.5" y2="15.6" stroke-width="0.6" opacity="0.5"/><line x1="135.1" y1="28.1" x2="140.3" y2="17.3" stroke-width="1.8" opacity="1"/><line x1="142.1" y1="22.7" x2="144.0" y2="19.2" stroke-width="0.6" opacity="0.5"/><line x1="145.6" y1="24.7" x2="147.7" y2="21.3" stroke-width="0.6" opacity="0.5"/><line x1="149.0" y1="26.9" x2="151.2" y2="23.5" stroke-width="0.6" opacity="0.5"/><line x1="152.2" y1="29.2" x2="154.6" y2="25.9" stroke-width="0.6" opacity="0.5"/><line x1="153.5" y1="33.9" x2="157.9" y2="28.5" stroke-width="1" opacity="0.8"/><line x1="158.4" y1="34.2" x2="161.1" y2="31.2" stroke-width="0.6" opacity="0.5"/><line x1="161.4" y1="36.9" x2="164.1" y2="34.0" stroke-width="0.6" opacity="0.5"/><line x1="164.1" y1="39.8" x2="167.1" y2="37.0" stroke-width="0.6" opacity="0.5"/><line x1="166.8" y1="42.7" x2="169.9" y2="40.1" stroke-width="0.6" opacity="0.5"/><line x1="163.0" y1="50.7" x2="172.5" y2="43.4" stroke-width="1.8" opacity="1"/><line x1="171.7" y1="49.0" x2="175.0" y2="46.7" stroke-width="0.6" opacity="0.5"/><line x1="174.0" y1="52.3" x2="177.3" y2="50.2" stroke-width="0.6" opacity="0.5"/><line x1="176.1" y1="55.7" x2="179.5" y2="53.7" stroke-width="0.6" opacity="0.5"/><line x1="178.0" y1="59.2" x2="181.5" y2="57.4" stroke-width="0.6" opacity="0.5"/><line x1="177.0" y1="64.1" x2="183.4" y2="61.1" stroke-width="1" opacity="0.8"/><line x1="181.4" y1="66.5" x2="185.1" y2="64.9" stroke-width="0.6" opacity="0.5"/><line x1="182.8" y1="70.2" x2="186.6" y2="68.8" stroke-width="0.6" opacity="0.5"/><line x1="184.1" y1="74.0" x2="187.9" y2="72.8" stroke-width="0.6" opacity="0.5"/><line x1="185.2" y1="77.8" x2="189.0" y2="76.8" stroke-width="0.6" opacity="0.5"/><line x1="178.3" y1="83.4" x2="190.0" y2="80.9" stroke-width="1.8" opacity="1"/><line x1="186.8" y1="85.6" x2="190.8" y2="85.0" stroke-width="0.6" opacity="0.5"/><line x1="187.4" y1="89.6" x2="191.4" y2="89.1" stroke-width="0.6" opacity="0.5"/><line x1="187.8" y1="93.6" x2="191.8" y2="93.3" stroke-width="0.6" opacity="0.5"/><line x1="188.0" y1="97.5" x2="192.0" y2="97.4" stroke-width="0.6" opacity="0.5"/><line x1="185.0" y1="101.5" x2="192.0" y2="101.6" stroke-width="1" opacity="0.8"/><line x1="187.8" y1="105.5" x2="191.8" y2="105.8" stroke-width="0.6" opacity="0.5"/><line x1="187.5" y1="109.5" x2="191.5" y2="109.9" stroke-width="0.6" opacity="0.5"/><line x1="187.0" y1="113.5" x2="190.9" y2="114.1" stroke-width="0.6" opacity="0.5"/><line x1="186.3" y1="117.4" x2="190.2" y2="118.2" stroke-width="0.6" opacity="0.5"/><line x1="177.6" y1="119.4" x2="189.3" y2="122.3" stroke-width="1.8" opacity="1"/><line x1="184.3" y1="125.1" x2="188.2" y2="126.3" stroke-width="0.6" opacity="0.5"/><line x1="183.1" y1="128.9" x2="186.9" y2="130.3" stroke-width="0.6" opacity="0.5"/><line x1="181.7" y1="132.7" x2="185.4" y2="134.2" stroke-width="0.6" opacity="0.5"/><line x1="180.1" y1="136.4" x2="183.8" y2="138.0" stroke-width="0.6" opacity="0.5"/><line x1="175.7" y1="138.6" x2="182.0" y2="141.8" stroke-width="1" opacity="0.8"/><line x1="176.5" y1="143.5" x2="180.0" y2="145.4" stroke-width="0.6" opacity="0.5"/><line x1="174.5" y1="146.9" x2="177.8" y2="149.0" stroke-width="0.6" opacity="0.5"/><line x1="172.3" y1="150.2" x2="175.5" y2="152.5" stroke-width="0.6" opacity="0.5"/><line x1="169.9" y1="153.4" x2="173.1" y2="155.9" stroke-width="0.6" opacity="0.5"/><line x1="161.3" y1="151.4" x2="170.5" y2="159.1" stroke-width="1.8" opacity="1"/></g>
    <g fill="#f2f1ec" font-size="7" font-weight="700" text-anchor="middle" font-family="Space Grotesk, sans-serif"><text x="47.9" y="146.7">0%</text><text x="33.5" y="88.9">20%</text><text x="70.2" y="41.9">40%</text><text x="129.8" y="41.9">60%</text><text x="166.5" y="88.9">80%</text><text x="152.1" y="146.7">100%</text></g>
    
    <circle cx="100" cy="100" r="18" fill="url(#core)" class="g-core"/>
    <g transform="translate(88 50) scale(.5)" fill="none"><path d="M6 16V10a4 4 0 0 1 4-4h6M32 6h6a4 4 0 0 1 4 4v6M42 32v6a4 4 0 0 1-4 4h-6M16 42h-6a4 4 0 0 1-4-4v-6" stroke="#e6b450" stroke-width="2.4" stroke-linecap="round"/><path d="M18 34V14h14v5h-8.6v3.4H30v5h-6.6V34H18Z" fill="#f2f1ec"/></g>
    <g class="g-needle" filter="url(#nglow)"><path d="M100 97.5 L170 100 L100 102.5 Z" fill="url(#needleG)"/><path d="M100 100 L84 100" stroke="#f2f1ec" stroke-width="3" stroke-linecap="round" opacity=".6"/></g>
    <circle cx="100" cy="100" r="7" fill="url(#cap)"/>
    <circle cx="100" cy="100" r="2.2" fill="#0b0b0d"/>
    <ellipse cx="78" cy="60" rx="48" ry="26" fill="#fff" opacity=".035" transform="rotate(-25 78 60)"/>
  </svg>
  </div></div>
</div></div>
          </div>
        </div>
      </div>
    </div></section>

    <section class="section-tight"><div class="container end-actions">
      <span class="ring-wrap"><a class="btn btn-white" href="pricing.html"><span>Paketleri gör</span></a></span>
      <span class="ring-wrap"><a class="btn btn-white" href="contact.html"><span>İletişim</span></a></span>
    </div></section>
"""

wrap("index.html", "FRAME — Bilgisayarına özel PC performans optimizasyonu",
     "Bilgisayarına ve oyunlarına özel, şeffaf ve kontrollü PC performans optimizasyonu. Her adım onayınla, ekranı canlı izlersin.", home)

# ---------------------------------------------------------------- HİZMETLER
services = page_hero("Hizmetler", "Hizmetler", "Her sistemin <em>ihtiyacı farklı.</em>",
    "Hazır liste yok. Bilgisayarına ve oyunlarına göre yalnızca anlamlı adımlar.") + f"""
    <section class="section"><div class="container">
      <div class="section-head"><span class="label">Alanlar</span><h2>Altı alan, sana göre seçilir.</h2></div>
      <div class="grid-2">
        <article class="card"><span class="card-index">01</span><span class="icon-box">{icon("windows")}</span><h3>Windows ve sistem ayarları</h3><p>Başlangıç uygulamaları, servisler, güç planı ve arka plan yükleri. Kullanımını bozan kapatma yapılmaz.</p></article>
        <article class="card"><span class="card-index">02</span><span class="icon-box">{icon("gpu")}</span><h3>Oyun ve grafik profilleri</h3><p>Oyunlarının grafik ayarları, yenileme hızı ve sürücü profili birlikte ele alınır.</p></article>
        <article class="card"><span class="card-index">03</span><span class="icon-box">{icon("bolt")}</span><h3>Sürücü ve gecikme kontrolü</h3><p>Zamanlayıcı, ağ ve girdi gecikmesine etki eden ayarlar. Her tweak otomatik faydalı sayılmaz.</p></article>
        <article class="card"><span class="card-index">04</span><span class="icon-box">{icon("thermo")}</span><h3>Sıcaklık ve kararlılık</h3><p>Sıcaklık ve güç sınırları gözetilir. Kararlılığı riske atan ayar yapılmaz.</p></article>
        <article class="card"><span class="card-index">05</span><span class="icon-box">{icon("chip")}</span><h3>BIOS ve donanım desteği</h3><p>Yalnızca donanımının desteklediği ayarlar. BIOS değişikliği açık onay olmadan yapılmaz.</p></article>
        <article class="card"><span class="card-index">06</span><span class="icon-box">{icon("test")}</span><h3>Karşılaştırma ve teslim</h3><p>Aynı koşullarda önce/sonra kontrolü. Değişiklik özeti ve geri alma adımları sende kalır.</p></article>
      </div>
    </div></section>

""" + cta("Sana uygun mu?", "Önce ihtiyacını anlayalım.", "Sistem parçalarını ve yaşadığın sorunu gönder; hangi hizmetlerin mantıklı olduğunu konuşalım.")

wrap("services.html", "Hizmetler — FRAME PC optimizasyon",
     "Windows, oyun, sürücü, gecikme, sıcaklık ve BIOS odaklı PC optimizasyon hizmetleri. Her adım donanımına göre seçilir.", services)

# ---------------------------------------------------------------- SÜREÇ
process = page_hero("Süreç", "Nasıl çalışıyor?", "Ne olacağını <em>önceden bil.</em>",
    "Bilgisayarını teslim edip beklemezsin. Her adımı görür, her adımı onaylarsın.") + f"""
    <section class="section"><div class="container split">
      <div class="section-head"><span class="label">Dört net aşama</span><h2>Paket seçiminden teslime.</h2><p>Siparişten test ve teslimata kadar tüm adımlar açıkça ilerler.</p></div>
      <ol class="timeline">
        <li><span class="tl-num">01</span><div><h3>Paket seçimi ve iletişim</h3><p>Paketi seç, bize yaz. Kapsamı ve saati netleştiririz.</p><span class="tl-meta">{icon("chat")} Discord</span></div></li>
        <li><span class="tl-num">02</span><div><h3>Donanım ve sistem analizi</h3><p>Kısa şablonla donanımını ve oyunlarını paylaşırsın. Sana özel plan çıkar.</p><span class="tl-meta">{icon("doc")} Sistem bilgisi şablonu</span></div></li>
        <li><span class="tl-num">03</span><div><h3>Güvenli uzaktan bağlantı</h3><p>AnyDesk ile bağlanırız. Ekranı izlersin, istediğin an durdurursun.</p><span class="tl-meta">{icon("eye")} Canlı izleme</span></div></li>
        <li><span class="tl-num">04</span><div><h3>Test ve teslim</h3><p>Sistem test edilir; değişiklik özeti ve geri alma adımları sende kalır.</p><span class="tl-meta">{icon("test")} Önce / sonra kontrolü</span></div></li>
      </ol>
    </div></section>

    <section class="section"><div class="container">
      <div class="section-head"><span class="label">Güvenlik ve şeffaflık</span><h2>Güvenliğin ve gizliliğin önce gelir.</h2><p>Optimizasyon boyunca kontrol sende; şeffaflık ve veri gizliliği önceliğimizdir.</p></div>
      <div class="grid-3">
        <article class="card"><span class="icon-box">{icon("eye")}</span><h3>Tam şeffaflık</h3><p>Bilgisayarında yapılan her ayar, script veya komut gözünün önünde, canlı olarak gerçekleştirilir. Gizli hiçbir işlem yapılmaz.</p></article>
        <article class="card"><span class="icon-box">{icon("lock")}</span><h3>Veri gizliliği</h3><p>Kişisel dosyaların, fotoğrafların veya özel verilerin asla kopyalanmaz, incelenmez veya dışarı aktarılmaz. İşlem yalnızca sistem performansına odaklıdır.</p></article>
        <article class="card"><span class="icon-box">{icon("rollback")}</span><h3>Geri dönüş güvencesi</h3><p>Uzman pakette tam sistem imajı alınır ve Güvenli Mod kurtarma adımları önceden hazırlanır. Diğer paketlerde geri yükleme noktası oluşturulur.</p></article>
      </div>
    </div></section>

    <section class="section"><div class="container">
      <div class="section-head"><span class="label">Beklentiyi doğru kuralım</span><h2>Her bilgisayar aynı sonucu vermez.</h2></div>
      <div class="duo">
        <article class="card"><h3>{icon("check")} Optimizasyon ne yapabilir?</h3><p>Yanlış yapılandırılmış ayarları düzeltmeye, gereksiz yükleri azaltmaya ve performans ile kararlılık dengesini kurmaya yardımcı olabilir.</p></article>
        <article class="card no"><h3>{icon("minus")} Ne yapamaz?</h3><p>Arızalı parçayı onaramaz, donanım sınırlarını ortadan kaldıramaz. Belirli bir FPS kazanımı garanti edilmez; sonuçlar sisteme bağlıdır.</p></article>
      </div>
    </div></section>
""" + cta("Hazır mısın?", "Önce sistemini değerlendirelim.", "Oyununu ve bilgisayar özelliklerini paylaş, doğru kapsamı birlikte belirleyelim.")

wrap("process.html", "Süreç — FRAME PC optimizasyon nasıl işler?",
     "Paket seçiminden AnyDesk ile güvenli uzaktan bağlantıya ve teslime kadar FRAME optimizasyon süreci. Hazırlık listesi ve güvenlik ilkeleri.", process)

# ---------------------------------------------------------------- PAKETLER
def feat(items, inherit=None):
    out = ""
    if inherit:
        out += f'<li>{icon("check")}<span class="inherit">{inherit}</span></li>'
    for i in items:
        out += f'<li>{icon("check")}<span>{i}</span></li>'
    return out

basic = ["Derin sistem temizliği", "Uygulama debloat", "Hayalet aygıt temizliği", "MSI mod ayarı",
         "Servis ve BCD optimizasyonu", "UWP uygulama temizliği", "Güç planı ve Core Parking",
         "Timer Resolution", "Başlangıç optimizasyonu", "Aygıt Yöneticisi ayarı", "Playbook kurulumu"]
adv = ["NVIDIA / AMD sürücü profili", "VBS / HVCI kapatma", "Ağ, QoS ve DNS", "Nagle optimizasyonu",
       "Saf sürücü kurulumu", "ISLC ve sanal bellek", "Monitör / CRU ayarı", "Mouse hissiyatı",
       "Oyun CFG ve başlatma ayarları"]
exp = ["Çekirdek afinitesi (Process Lasso)", "Tam BIOS modifikasyonu", "C-States ve fTPM", "PBO / EXPO",
       "RAM timing daraltma", "CPU ve GPU undervolt", "Frekans sabitleme", "USB ve IRQ ayrıştırma",
       "Özel Windows (Custom OS)", "Tam sistem imajı", "Güvenli Mod kurtarma planı"]

def chips(items):
    return "".join(f'<span>{icon("check")}{i}</span>' for i in items)

def row(name, a, b, c):
    def cell(v, featured=False):
        cls = ' class="col-featured"' if featured else ""
        if v:
            return f'<td{cls}>{icon("check")}<span class="sr-only"></span></td>'
        return f'<td{cls}>{icon("minus","icon no")}</td>'
    return f'<tr><th scope="row">{name}</th>{cell(a)}{cell(b, True)}{cell(c)}</tr>'

rows = [("Sistem temizliği, servis ve güç optimizasyonu",1,1,1),("Ekran kartı sürücüsü ve profil optimizasyonu",0,1,1),
        ("Ağ, gecikme, monitör ve oyun ayarları",0,1,1),
        ("BIOS, RAM zamanlamaları ve voltaj ayarları",0,0,1),("Özel Windows kurulumu ve tam sistem imajı",0,0,1)]

pricing = f"""
    <section class="page-bar"><div class="container"><div class="crumbs"><a href="index.html">Ana sayfa</a><span>/</span><span>Paketler</span></div><h1 class="sr-only">Paketler ve fiyatlar</h1></div></section>
    <section class="section-tight" id="paketler"><div class="container">
      <div class="plans2">
        <article class="pcard tier-basic wide">
          <div class="chip3d" aria-hidden="true">
  <svg viewBox="0 0 200 200" fill="none">
    <defs>
      <linearGradient id="pa-metal" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e3e6ec"/><stop offset=".5" stop-color="#8d939e"/><stop offset="1" stop-color="#3b3f47"/></linearGradient>
      <linearGradient id="pa-body" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#30343d"/><stop offset=".45" stop-color="#15171c"/><stop offset="1" stop-color="#0a0b0e"/></linearGradient>
      <linearGradient id="pa-side" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0d0e12"/><stop offset="1" stop-color="#020203"/></linearGradient>
      <linearGradient id="pa-plate" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="var(--tier-dark)"/><stop offset=".5" stop-color="#0c0d11"/><stop offset="1" stop-color="var(--tier-dark)"/></linearGradient>
      <linearGradient id="pa-logo" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".95"/><stop offset=".35" stop-color="var(--tier)"/><stop offset="1" stop-color="var(--tier-dark)"/></linearGradient>
      <linearGradient id="pa-gloss" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".28"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/></linearGradient>
      <linearGradient id="pa-trail" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="var(--tier)" stop-opacity="0"/><stop offset=".5" stop-color="var(--tier)"/><stop offset="1" stop-color="var(--tier)" stop-opacity="0"/></linearGradient>
      <radialGradient id="pa-halo" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="var(--tier)" stop-opacity=".7"/><stop offset="1" stop-color="var(--tier)" stop-opacity="0"/></radialGradient>
      <clipPath id="pa-clip"><rect x="50" y="50" width="100" height="100" rx="14"/></clipPath>
    </defs>
    <ellipse cx="100" cy="150" rx="78" ry="22" fill="#000" opacity=".55"/>
    <g class="trails" fill="none" stroke="url(#pa-trail)" stroke-linecap="round">
      <path d="M-20 150 C 40 190, 160 190, 220 140" stroke-width="10" opacity=".25"/>
      <path d="M-20 150 C 40 190, 160 190, 220 140" stroke-width="3" class="trail-line"/>
      <path d="M-20 125 C 50 175, 150 180, 220 160" stroke-width="2" opacity=".6" class="trail-line t2"/>
    </g>
    <circle cx="100" cy="100" r="78" fill="url(#pa-halo)" class="chip-halo"/>
    <g fill="url(#pa-metal)" opacity=".95"><rect x="62.0" y="34" width="4" height="16" rx="1.5"/><rect x="71.5" y="34" width="4" height="16" rx="1.5"/><rect x="81.0" y="34" width="4" height="16" rx="1.5"/><rect x="90.5" y="34" width="4" height="16" rx="1.5"/><rect x="100.0" y="34" width="4" height="16" rx="1.5"/><rect x="109.5" y="34" width="4" height="16" rx="1.5"/><rect x="119.0" y="34" width="4" height="16" rx="1.5"/><rect x="128.5" y="34" width="4" height="16" rx="1.5"/><rect x="62.0" y="150" width="4" height="18" rx="1.5"/><rect x="71.5" y="150" width="4" height="18" rx="1.5"/><rect x="81.0" y="150" width="4" height="18" rx="1.5"/><rect x="90.5" y="150" width="4" height="18" rx="1.5"/><rect x="100.0" y="150" width="4" height="18" rx="1.5"/><rect x="109.5" y="150" width="4" height="18" rx="1.5"/><rect x="119.0" y="150" width="4" height="18" rx="1.5"/><rect x="128.5" y="150" width="4" height="18" rx="1.5"/><rect x="34" y="64.0" width="16" height="4" rx="1.5"/><rect x="34" y="73.5" width="16" height="4" rx="1.5"/><rect x="34" y="83.0" width="16" height="4" rx="1.5"/><rect x="34" y="92.5" width="16" height="4" rx="1.5"/><rect x="34" y="102.0" width="16" height="4" rx="1.5"/><rect x="34" y="111.5" width="16" height="4" rx="1.5"/><rect x="34" y="121.0" width="16" height="4" rx="1.5"/><rect x="34" y="130.5" width="16" height="4" rx="1.5"/><rect x="150" y="64.0" width="18" height="4" rx="1.5"/><rect x="150" y="73.5" width="18" height="4" rx="1.5"/><rect x="150" y="83.0" width="18" height="4" rx="1.5"/><rect x="150" y="92.5" width="18" height="4" rx="1.5"/><rect x="150" y="102.0" width="18" height="4" rx="1.5"/><rect x="150" y="111.5" width="18" height="4" rx="1.5"/><rect x="150" y="121.0" width="18" height="4" rx="1.5"/><rect x="150" y="130.5" width="18" height="4" rx="1.5"/></g>
    <rect x="50" y="58" width="100" height="100" rx="14" fill="url(#pa-side)"/>
    <rect x="50" y="50" width="100" height="100" rx="14" fill="url(#pa-body)" stroke="rgba(255,255,255,.16)"/>
    <rect x="58" y="58" width="84" height="84" rx="10" fill="#07080a"/>
    <rect x="60" y="60" width="80" height="80" rx="9" fill="url(#pa-plate)" stroke="color-mix(in srgb, var(--tier) 55%, transparent)"/>
    <g transform="translate(62 62) scale(1.58)">
      <path d="M6 16V10a4 4 0 0 1 4-4h6M32 6h6a4 4 0 0 1 4 4v6M42 32v6a4 4 0 0 1-4 4h-6M16 42h-6a4 4 0 0 1-4-4v-6" stroke="#000" stroke-width="3.2" stroke-linecap="round" opacity=".6" transform="translate(.6 1.2)"/>
      <path d="M18 34V14h14v5h-8.6v3.4H30v5h-6.6V34H18Z" fill="#000" opacity=".6" transform="translate(.8 1.4)"/>
      <path d="M6 16V10a4 4 0 0 1 4-4h6M32 6h6a4 4 0 0 1 4 4v6M42 32v6a4 4 0 0 1-4 4h-6M16 42h-6a4 4 0 0 1-4-4v-6" stroke="url(#pa-logo)" stroke-width="2.6" stroke-linecap="round"/>
      <path d="M18 34V14h14v5h-8.6v3.4H30v5h-6.6V34H18Z" fill="url(#pa-logo)"/>
      <path d="M18 34V14h14v5h-8.6v3.4H30v5h-6.6V34H18Z" fill="none" stroke="#fff" stroke-width=".5" opacity=".5"/>
    </g>
    <g clip-path="url(#pa-clip)"><rect class="sweep" x="-60" y="40" width="40" height="130" fill="#fff" opacity=".16" transform="skewX(-25)"/></g>
    <rect x="50" y="50" width="100" height="100" rx="14" fill="url(#pa-gloss)"/>
  </svg>
</div>
          <div class="pbody">
            <div class="phead"><div><h3>Temel Paket</h3><span class="psub">Basic Tweak · Windows ve sistem optimizasyonu</span></div><div class="pprice"><b>400 <small>₺</small></b><span>tek seferlik</span></div></div>
            <div class="pavail"><i></i>Canlı oturum · AnyDesk · ~1 saat</div>
            <p class="pdesc">Windows'un hantallığından kurtulup sistemin nefes almasını sağlayan standart optimizasyon. Emin değilsen buradan başla.</p>
            <div class="pbars"><i class="on"></i><i class="on"></i><i class=""></i><i class=""></i><i class=""></i><i class=""></i></div>
            <div class="pfeats"><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Derin sistem temizliği</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Uygulama debloat</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Servis ve BCD optimizasyonu</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Güç planı ve Core Parking</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>MSI mod ayarı</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Timer Resolution</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Başlangıç optimizasyonu</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>UWP temizliği</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Aygıt Yöneticisi ayarı</span><span class="f off"><svg viewBox="0 0 24 24"><path d="M7 7l10 10M17 7 7 17"/></svg>Sürücü profili</span><span class="f off"><svg viewBox="0 0 24 24"><path d="M7 7l10 10M17 7 7 17"/></svg>Ağ ve gecikme</span><span class="f off"><svg viewBox="0 0 24 24"><path d="M7 7l10 10M17 7 7 17"/></svg>BIOS</span></div>
            <div class="pbtns"><a class="btn btn-ghost" href="check.html">Hangi paket?</a><a class="btn btn-tier" href="contact.html">Temel ile başla</a></div>
          </div>
        </article>
        <article class="pcard tier-adv">
          <div class="chip3d" aria-hidden="true">
  <svg viewBox="0 0 200 200" fill="none">
    <defs>
      <linearGradient id="pb-metal" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e3e6ec"/><stop offset=".5" stop-color="#8d939e"/><stop offset="1" stop-color="#3b3f47"/></linearGradient>
      <linearGradient id="pb-body" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#30343d"/><stop offset=".45" stop-color="#15171c"/><stop offset="1" stop-color="#0a0b0e"/></linearGradient>
      <linearGradient id="pb-side" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0d0e12"/><stop offset="1" stop-color="#020203"/></linearGradient>
      <linearGradient id="pb-plate" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="var(--tier-dark)"/><stop offset=".5" stop-color="#0c0d11"/><stop offset="1" stop-color="var(--tier-dark)"/></linearGradient>
      <linearGradient id="pb-logo" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".95"/><stop offset=".35" stop-color="var(--tier)"/><stop offset="1" stop-color="var(--tier-dark)"/></linearGradient>
      <linearGradient id="pb-gloss" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".28"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/></linearGradient>
      <linearGradient id="pb-trail" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="var(--tier)" stop-opacity="0"/><stop offset=".5" stop-color="var(--tier)"/><stop offset="1" stop-color="var(--tier)" stop-opacity="0"/></linearGradient>
      <radialGradient id="pb-halo" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="var(--tier)" stop-opacity=".7"/><stop offset="1" stop-color="var(--tier)" stop-opacity="0"/></radialGradient>
      <clipPath id="pb-clip"><rect x="50" y="50" width="100" height="100" rx="14"/></clipPath>
    </defs>
    <ellipse cx="100" cy="150" rx="78" ry="22" fill="#000" opacity=".55"/>
    <g class="trails" fill="none" stroke="url(#pb-trail)" stroke-linecap="round">
      <path d="M-20 150 C 40 190, 160 190, 220 140" stroke-width="10" opacity=".25"/>
      <path d="M-20 150 C 40 190, 160 190, 220 140" stroke-width="3" class="trail-line"/>
      <path d="M-20 125 C 50 175, 150 180, 220 160" stroke-width="2" opacity=".6" class="trail-line t2"/>
    </g>
    <circle cx="100" cy="100" r="78" fill="url(#pb-halo)" class="chip-halo"/>
    <g fill="url(#pb-metal)" opacity=".95"><rect x="62.0" y="34" width="4" height="16" rx="1.5"/><rect x="71.5" y="34" width="4" height="16" rx="1.5"/><rect x="81.0" y="34" width="4" height="16" rx="1.5"/><rect x="90.5" y="34" width="4" height="16" rx="1.5"/><rect x="100.0" y="34" width="4" height="16" rx="1.5"/><rect x="109.5" y="34" width="4" height="16" rx="1.5"/><rect x="119.0" y="34" width="4" height="16" rx="1.5"/><rect x="128.5" y="34" width="4" height="16" rx="1.5"/><rect x="62.0" y="150" width="4" height="18" rx="1.5"/><rect x="71.5" y="150" width="4" height="18" rx="1.5"/><rect x="81.0" y="150" width="4" height="18" rx="1.5"/><rect x="90.5" y="150" width="4" height="18" rx="1.5"/><rect x="100.0" y="150" width="4" height="18" rx="1.5"/><rect x="109.5" y="150" width="4" height="18" rx="1.5"/><rect x="119.0" y="150" width="4" height="18" rx="1.5"/><rect x="128.5" y="150" width="4" height="18" rx="1.5"/><rect x="34" y="64.0" width="16" height="4" rx="1.5"/><rect x="34" y="73.5" width="16" height="4" rx="1.5"/><rect x="34" y="83.0" width="16" height="4" rx="1.5"/><rect x="34" y="92.5" width="16" height="4" rx="1.5"/><rect x="34" y="102.0" width="16" height="4" rx="1.5"/><rect x="34" y="111.5" width="16" height="4" rx="1.5"/><rect x="34" y="121.0" width="16" height="4" rx="1.5"/><rect x="34" y="130.5" width="16" height="4" rx="1.5"/><rect x="150" y="64.0" width="18" height="4" rx="1.5"/><rect x="150" y="73.5" width="18" height="4" rx="1.5"/><rect x="150" y="83.0" width="18" height="4" rx="1.5"/><rect x="150" y="92.5" width="18" height="4" rx="1.5"/><rect x="150" y="102.0" width="18" height="4" rx="1.5"/><rect x="150" y="111.5" width="18" height="4" rx="1.5"/><rect x="150" y="121.0" width="18" height="4" rx="1.5"/><rect x="150" y="130.5" width="18" height="4" rx="1.5"/></g>
    <rect x="50" y="58" width="100" height="100" rx="14" fill="url(#pb-side)"/>
    <rect x="50" y="50" width="100" height="100" rx="14" fill="url(#pb-body)" stroke="rgba(255,255,255,.16)"/>
    <rect x="58" y="58" width="84" height="84" rx="10" fill="#07080a"/>
    <rect x="60" y="60" width="80" height="80" rx="9" fill="url(#pb-plate)" stroke="color-mix(in srgb, var(--tier) 55%, transparent)"/>
    <g transform="translate(62 62) scale(1.58)">
      <path d="M6 16V10a4 4 0 0 1 4-4h6M32 6h6a4 4 0 0 1 4 4v6M42 32v6a4 4 0 0 1-4 4h-6M16 42h-6a4 4 0 0 1-4-4v-6" stroke="#000" stroke-width="3.2" stroke-linecap="round" opacity=".6" transform="translate(.6 1.2)"/>
      <path d="M18 34V14h14v5h-8.6v3.4H30v5h-6.6V34H18Z" fill="#000" opacity=".6" transform="translate(.8 1.4)"/>
      <path d="M6 16V10a4 4 0 0 1 4-4h6M32 6h6a4 4 0 0 1 4 4v6M42 32v6a4 4 0 0 1-4 4h-6M16 42h-6a4 4 0 0 1-4-4v-6" stroke="url(#pb-logo)" stroke-width="2.6" stroke-linecap="round"/>
      <path d="M18 34V14h14v5h-8.6v3.4H30v5h-6.6V34H18Z" fill="url(#pb-logo)"/>
      <path d="M18 34V14h14v5h-8.6v3.4H30v5h-6.6V34H18Z" fill="none" stroke="#fff" stroke-width=".5" opacity=".5"/>
    </g>
    <g clip-path="url(#pb-clip)"><rect class="sweep" x="-60" y="40" width="40" height="130" fill="#fff" opacity=".16" transform="skewX(-25)"/></g>
    <rect x="50" y="50" width="100" height="100" rx="14" fill="url(#pb-gloss)"/>
  </svg>
</div>
          <div class="pbody">
            <div class="phead"><div><h3>Gelişmiş Paket <span class="ptag">En popüler</span></h3><span class="psub">Advanced Tweak · Sürücü, ağ ve oyun profilleri</span></div><div class="pprice"><b>900 <small>₺</small></b><span>tek seferlik</span></div></div>
            <div class="pavail"><i></i>Canlı oturum · AnyDesk · 1,5–2 saat</div>
            <p class="pdesc">Gecikmeyi ve girdi gecikmesini hedef alan ileri düzey yapılandırma. Rekabetçi oyuncuların çoğu için doğru seviye.</p>
            <div class="pbars"><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class=""></i><i class=""></i></div>
            <div class="pfeats"><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Temel'deki her şey</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>NVIDIA / AMD sürücü profili</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>VBS / HVCI kapatma</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Ağ, QoS ve DNS</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Nagle optimizasyonu</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Saf sürücü kurulumu</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>ISLC ve sanal bellek</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Monitör / CRU ayarı</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Oyun CFG ve başlatma ayarları</span><span class="f off"><svg viewBox="0 0 24 24"><path d="M7 7l10 10M17 7 7 17"/></svg>BIOS modifikasyonu</span><span class="f off"><svg viewBox="0 0 24 24"><path d="M7 7l10 10M17 7 7 17"/></svg>RAM timing</span><span class="f off"><svg viewBox="0 0 24 24"><path d="M7 7l10 10M17 7 7 17"/></svg>Custom OS</span></div>
            <div class="pbtns"><a class="btn btn-ghost" href="check.html">Hangi paket?</a><a class="btn btn-tier" href="contact.html">Gelişmiş ile başla</a></div>
          </div>
        </article>
        <article class="pcard tier-expert">
          <div class="chip3d" aria-hidden="true">
  <svg viewBox="0 0 200 200" fill="none">
    <defs>
      <linearGradient id="pc-metal" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e3e6ec"/><stop offset=".5" stop-color="#8d939e"/><stop offset="1" stop-color="#3b3f47"/></linearGradient>
      <linearGradient id="pc-body" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#30343d"/><stop offset=".45" stop-color="#15171c"/><stop offset="1" stop-color="#0a0b0e"/></linearGradient>
      <linearGradient id="pc-side" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0d0e12"/><stop offset="1" stop-color="#020203"/></linearGradient>
      <linearGradient id="pc-plate" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="var(--tier-dark)"/><stop offset=".5" stop-color="#0c0d11"/><stop offset="1" stop-color="var(--tier-dark)"/></linearGradient>
      <linearGradient id="pc-logo" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".95"/><stop offset=".35" stop-color="var(--tier)"/><stop offset="1" stop-color="var(--tier-dark)"/></linearGradient>
      <linearGradient id="pc-gloss" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".28"/><stop offset=".5" stop-color="#fff" stop-opacity="0"/></linearGradient>
      <linearGradient id="pc-trail" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="var(--tier)" stop-opacity="0"/><stop offset=".5" stop-color="var(--tier)"/><stop offset="1" stop-color="var(--tier)" stop-opacity="0"/></linearGradient>
      <radialGradient id="pc-halo" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="var(--tier)" stop-opacity=".7"/><stop offset="1" stop-color="var(--tier)" stop-opacity="0"/></radialGradient>
      <clipPath id="pc-clip"><rect x="50" y="50" width="100" height="100" rx="14"/></clipPath>
    </defs>
    <ellipse cx="100" cy="150" rx="78" ry="22" fill="#000" opacity=".55"/>
    <g class="trails" fill="none" stroke="url(#pc-trail)" stroke-linecap="round">
      <path d="M-20 150 C 40 190, 160 190, 220 140" stroke-width="10" opacity=".25"/>
      <path d="M-20 150 C 40 190, 160 190, 220 140" stroke-width="3" class="trail-line"/>
      <path d="M-20 125 C 50 175, 150 180, 220 160" stroke-width="2" opacity=".6" class="trail-line t2"/>
    </g>
    <circle cx="100" cy="100" r="78" fill="url(#pc-halo)" class="chip-halo"/>
    <g fill="url(#pc-metal)" opacity=".95"><rect x="62.0" y="34" width="4" height="16" rx="1.5"/><rect x="71.5" y="34" width="4" height="16" rx="1.5"/><rect x="81.0" y="34" width="4" height="16" rx="1.5"/><rect x="90.5" y="34" width="4" height="16" rx="1.5"/><rect x="100.0" y="34" width="4" height="16" rx="1.5"/><rect x="109.5" y="34" width="4" height="16" rx="1.5"/><rect x="119.0" y="34" width="4" height="16" rx="1.5"/><rect x="128.5" y="34" width="4" height="16" rx="1.5"/><rect x="62.0" y="150" width="4" height="18" rx="1.5"/><rect x="71.5" y="150" width="4" height="18" rx="1.5"/><rect x="81.0" y="150" width="4" height="18" rx="1.5"/><rect x="90.5" y="150" width="4" height="18" rx="1.5"/><rect x="100.0" y="150" width="4" height="18" rx="1.5"/><rect x="109.5" y="150" width="4" height="18" rx="1.5"/><rect x="119.0" y="150" width="4" height="18" rx="1.5"/><rect x="128.5" y="150" width="4" height="18" rx="1.5"/><rect x="34" y="64.0" width="16" height="4" rx="1.5"/><rect x="34" y="73.5" width="16" height="4" rx="1.5"/><rect x="34" y="83.0" width="16" height="4" rx="1.5"/><rect x="34" y="92.5" width="16" height="4" rx="1.5"/><rect x="34" y="102.0" width="16" height="4" rx="1.5"/><rect x="34" y="111.5" width="16" height="4" rx="1.5"/><rect x="34" y="121.0" width="16" height="4" rx="1.5"/><rect x="34" y="130.5" width="16" height="4" rx="1.5"/><rect x="150" y="64.0" width="18" height="4" rx="1.5"/><rect x="150" y="73.5" width="18" height="4" rx="1.5"/><rect x="150" y="83.0" width="18" height="4" rx="1.5"/><rect x="150" y="92.5" width="18" height="4" rx="1.5"/><rect x="150" y="102.0" width="18" height="4" rx="1.5"/><rect x="150" y="111.5" width="18" height="4" rx="1.5"/><rect x="150" y="121.0" width="18" height="4" rx="1.5"/><rect x="150" y="130.5" width="18" height="4" rx="1.5"/></g>
    <rect x="50" y="58" width="100" height="100" rx="14" fill="url(#pc-side)"/>
    <rect x="50" y="50" width="100" height="100" rx="14" fill="url(#pc-body)" stroke="rgba(255,255,255,.16)"/>
    <rect x="58" y="58" width="84" height="84" rx="10" fill="#07080a"/>
    <rect x="60" y="60" width="80" height="80" rx="9" fill="url(#pc-plate)" stroke="color-mix(in srgb, var(--tier) 55%, transparent)"/>
    <g transform="translate(62 62) scale(1.58)">
      <path d="M6 16V10a4 4 0 0 1 4-4h6M32 6h6a4 4 0 0 1 4 4v6M42 32v6a4 4 0 0 1-4 4h-6M16 42h-6a4 4 0 0 1-4-4v-6" stroke="#000" stroke-width="3.2" stroke-linecap="round" opacity=".6" transform="translate(.6 1.2)"/>
      <path d="M18 34V14h14v5h-8.6v3.4H30v5h-6.6V34H18Z" fill="#000" opacity=".6" transform="translate(.8 1.4)"/>
      <path d="M6 16V10a4 4 0 0 1 4-4h6M32 6h6a4 4 0 0 1 4 4v6M42 32v6a4 4 0 0 1-4 4h-6M16 42h-6a4 4 0 0 1-4-4v-6" stroke="url(#pc-logo)" stroke-width="2.6" stroke-linecap="round"/>
      <path d="M18 34V14h14v5h-8.6v3.4H30v5h-6.6V34H18Z" fill="url(#pc-logo)"/>
      <path d="M18 34V14h14v5h-8.6v3.4H30v5h-6.6V34H18Z" fill="none" stroke="#fff" stroke-width=".5" opacity=".5"/>
    </g>
    <g clip-path="url(#pc-clip)"><rect class="sweep" x="-60" y="40" width="40" height="130" fill="#fff" opacity=".16" transform="skewX(-25)"/></g>
    <rect x="50" y="50" width="100" height="100" rx="14" fill="url(#pc-gloss)"/>
  </svg>
</div>
          <div class="pbody">
            <div class="phead"><div><h3>Uzman Paket</h3><span class="psub">Custom OS &amp; BIOS · Tam donanım optimizasyonu</span></div><div class="pprice"><b>2.400 <small>₺</small></b><span>tek seferlik</span></div></div>
            <div class="pavail"><i></i>Canlı oturum · AnyDesk · 2–3 saat</div>
            <p class="pdesc">Minimum gecikme ve maksimum kararlılık için BIOS, bellek zamanlamaları, undervolt ve temiz özel Windows kurulumu.</p>
            <div class="pbars"><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i><i class="on"></i></div>
            <div class="pfeats"><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Gelişmiş'teki her şey</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Tam BIOS modifikasyonu</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>C-States ve fTPM</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>PBO / EXPO</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>RAM timing daraltma</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>CPU ve GPU undervolt</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Frekans sabitleme</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>USB ve IRQ ayrıştırma</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Çekirdek afinitesi</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Özel Windows (Custom OS)</span><span class="f on"><svg viewBox="0 0 24 24"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>Tam sistem imajı</span></div>
            <div class="pbtns"><a class="btn btn-ghost" href="check.html">Hangi paket?</a><a class="btn btn-tier" href="contact.html">Uzman ile başla</a></div>
          </div>
        </article>
      </div>
      <div class="quick card">
        <span class="icon-box">{icon("bolt")}</span>
        <div class="quick-text"><b>Hızlı Değerlendirme</b><p>Hangi paketi seçeceğinden emin değil misin? Sistemini inceleyip 15 dakikada net bir cevap verir, donanımına en uygun paketi öneririz.</p></div>
        <div class="quick-price"><b>100 <small>₺</small></b><span>15 dakika</span></div>
        <a class="btn btn-light" href="contact.html">Değerlendirme al</a>
      </div>
      <p class="note center">Optimizasyonun tam olarak ne yaptığını merak mı ediyorsun? <a href="process.html">Nasıl çalıştığını gör.</a></p>


      <div class="eval card" style="margin-top:14px">
        <span class="icon-box">{icon("bolt")}</span>
        <div><b>Ücretsiz PC kontrolü</b><p>Emin değilsen 7 soruluk kontrolü yap; darboğaz puanını, sana uygun paketi ve ücretsiz başlangıç listesini anında gör.</p></div>
        <div class="eval-price"><strong>0 ₺</strong><small>2 dakika</small></div>
        <a class="btn btn-primary" href="check.html">Kontrolü başlat {icon("arrow")}</a>
      </div>
    </div></section>

"""

wrap("pricing.html", "Paketler ve fiyatlar — FRAME PC optimizasyon",
     "Temel 400 ₺, Gelişmiş 900 ₺ ve Uzman 2.400 ₺ sabit fiyatlı PC optimizasyon paketleri. Kapsam karşılaştırması ve paket seçme rehberi.", pricing)

# ---------------------------------------------------------------- SSS
faqs = [
 ("Performans ve sonuçlar", [
  ("Kesin FPS artışı garanti ediyor musunuz?", "Hayır. Sonuçlar bilgisayarın parçalarına, oyuna, sıcaklıklara ve mevcut ayarlara göre değişir. Sabit FPS artışı sözü vermek yerine ölçülebilir ve gerçekçi beklentiler belirleriz."),
  ("Optimizasyon her bilgisayarda işe yarar mı?", "Hayır. Bazı sistemlerde ayarlar zaten doğru olabilir veya sorun donanım arızasından kaynaklanabilir. Böyle bir durumda optimizasyonun çözüm olmayabileceğini açıkça söyleriz."),
  ("İşlem bilgisayarıma zarar verir mi?", "Donanıma uygun ve geri alınabilir adımları tercih ederiz. BIOS, undervolt veya bellek zamanlaması gibi hassas ayarlar yalnızca Uzman pakette, ayrıca değerlendirilir ve açık onay olmadan uygulanmaz."),
  ("Anti-cheat (Vanguard, VAC, EAC) sorun çıkarır mı?", "Hayır. Hiçbir anti-cheat atlatılmaz, güvenlik bileşenleri kapatılmaz; yalnızca performansı etkileyen sistem ayarları düzenlenir. Valorant, CS2, Fortnite ve benzeri oyunlarda yasak riski oluşturacak bir işlem yapılmaz."),
  ("Dizüstü bilgisayarlar için de uygun mu?", "Evet. Dizüstülerde güç sınırları ve sıcaklık daha belirleyicidir; bu yüzden hedefler buna göre kurulur. BIOS ayarları çoğu dizüstüde kısıtlı olduğundan Uzman paketin kapsamı sistemine göre netleştirilir."),
  ("Windows 10 ve Windows 11 fark eder mi?", "İkisi de desteklenir. Bazı adımlar sürüme göre farklılık gösterir; plan buna göre uyarlanır."),
 ]),
 ("Uzaktan destek ve gizlilik", [
  ("Bilgisayarımın kontrolü bende kalıyor mu?", "Evet. Uzaktan bağlantı yalnızca senin bilgin ve onayınla başlar. İşlemi görebilir, soru sorabilir veya istediğin anda oturumu durdurabilirsin."),
  ("Hangi uzaktan bağlantı aracı kullanılıyor?", "AnyDesk. Resmi sitesinden indirip kurman yeterli. Bağlantı kodunu yalnızca oturum başında paylaşırsın; oturum bitince erişim kapanır."),
  ("Şifrelerimi veya kişisel dosyalarımı ister misiniz?", "Hayır. Hesap şifrelerini paylaşmamalısın; kişisel dosyaların optimizasyonun parçası değildir ve incelenmez."),
  ("Uzaktan bağlantıyı nasıl sonlandırırım?", "Oturum bittiğinde AnyDesk'i kapatabilir ve erişim iznini kaldırabilirsin. Bağlantının nasıl kapatılacağını oturum sonunda birlikte kontrol ederiz."),
 ]),
 ("Paketler, ödeme ve randevu", [
  ("Hangi paketi seçmeliyim?", "Sistemin yavaş ve hantalsa Temel; oyunda gecikme ve takılma yaşıyorsan Gelişmiş; BIOS ve temiz özel kurulum dahil her şeyi istiyorsan Uzman. Emin değilsen Discord'dan sistemini yaz, birlikte karar verelim."),
  ("Fiyatlar sabit mi?", "Evet. Üç paketin fiyatı sitede yazdığı gibidir ve işlem başlamadan önce onaylanır. Sonradan ek ücret çıkmaz."),
  ("Ödeme nasıl yapılıyor?", "Ödeme yöntemi ve zamanı Discord üzerinden, randevu netleşince konuşulur. İşlem başlamadan önce kapsam ve ücret yazılı olarak onaylanır."),
  ("Optimizasyon ne kadar sürer?", "Temel paket yaklaşık 1 saat, Gelişmiş 1,5 ile 2 saat, Uzman paket temiz kurulum nedeniyle 2 ile 3 saat sürebilir. Randevu öncesi tahmini süreyi paylaşırız."),
  ("Bir sorun çıkarsa geri alınabilir mi?", "Evet. Her oturumda geri yükleme noktası oluşturulur; Uzman pakette ayrıca tam sistem imajı alınır. Değişiklik özeti ve geri alma adımları sana yazılı verilir."),
  ("Oturumdan sonra sorum olursa?", "Takip desteği süresi içinde (Temel 7, Gelişmiş 14, Uzman 30 gün) bize yazabilirsin. Windows güncellemesi bir ayarı bozarsa bu sürede ücretsiz düzeltilir."),
  ("Oturum raporu nedir?", "Oturum sonunda yapılan her değişikliğin listesi, geri alma adımları ve varsa önce/sonra ölçümleri yazılı olarak sana verilir."),
 ]),
]
faq_html = ""
for title, items in faqs:
    faq_html += f'<div class="faq-group"><h2>{title}</h2><div class="faq">'
    for q, a in items:
        faq_html += f"<details><summary>{q}</summary><p>{a}</p></details>"
    faq_html += "</div></div>"

ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
    {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for _, items in faqs for q, a in items]}
faq_head = '\n<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>'

faq_page = page_hero("Sık sorulanlar", "Sorular", "Aklındaki sorular, <em>açık yanıtlar.</em>",
    "Nasıl çalıştığımız, güvenliğin, ödeme ve gerçekçi performans beklentileri hakkında merak edilenler.") + f"""
    <section class="section"><div class="container faq-page">
      {faq_html}
    </div></section>
""" + cta("Başka sorun mu var?", "Sistemin ve sorunun hakkında bize yaz.", "Genelde aynı gün dönüş yaparız.", "Soru sor")

wrap("faq.html", "Sık sorulanlar — FRAME PC optimizasyon",
     "FPS garantisi, güvenlik, AnyDesk, ödeme, süre ve geri alma hakkında sık sorulan sorular ve açık yanıtlar.", faq_page, faq_head)

# ---------------------------------------------------------------- İLETİŞİM
contact = f"""
    <section class="page-bar"><div class="container"><div class="crumbs"><a href="index.html">Ana sayfa</a><span>/</span><span>İletişim</span></div><h1 class="contact-h">Sistemini yaz, <em>başlayalım.</em></h1></div></section>

    <section class="section-tight"><div class="container contact-wrap">
      <aside class="contact-side">
        <div class="card contact-main">
          <span class="icon-box">{icon("chat")}</span>
          <h3>Discord sunucusu</h3>
          <p>Soru, randevu ve paket seçimi için tek kanal. Mesajını bırak; genelde aynı gün dönüş yaparız.</p>
          <a class="btn btn-primary btn-block" href="#" data-discord>Discord'a katıl {icon("arrow-ne")}</a>
          <div data-email hidden><p class="email-line">E-posta: <a href="#"></a></p></div>
        <ul class="contact-facts">
          <li>{icon("clock")}<span><b>Aynı gün dönüş</b><small>Genellikle birkaç saat içinde</small></span></li>
          <li>{icon("eye")}<span><b>Canlı oturum</b><small>AnyDesk ile, ekranı sen izlersin</small></span></li>
          <li>{icon("shield")}<span><b>Şifre istenmez</b><small>Kişisel dosyalarına dokunulmaz</small></span></li>
        </ul>
        </div>
      </aside>
      <div class="card contact-form">
        <div class="form-head"><span class="icon-box">{icon("doc")}</span><div><h3>Sistem bilgisi şablonu</h3><p>Kopyalayıp doldur, Discord'dan gönder. Ne kadar ayrıntılı olursa plan o kadar isabetli olur.</p></div></div>
        <pre class="template" id="sistem-sablonu">İşlemci (CPU):
Ekran kartı (GPU):
RAM (miktar / hız):
Anakart:
Depolama (SSD / HDD):
Monitör (çözünürlük / Hz):
Windows sürümü:
Oynadığım oyunlar:
Yaşadığım sorun:
İlgilendiğim paket:</pre>
        <div class="copy-row"><button class="btn btn-primary" type="button" data-copy="#sistem-sablonu">{icon("copy")} Şablonu kopyala</button><a class="btn btn-ghost" href="check.html">Emin değilim, kontrol yap</a><span class="status" data-copy-status aria-live="polite"></span></div>
      </div>
        <div class="card contact-prep">
          <h4>Oturum öncesi</h4>
          <ul class="prep-list prep-row">
            <li>{icon("monitor")}<span><b>AnyDesk kur</b><small>Kodu yalnızca oturum başında paylaş</small></span></li>
            <li>{icon("wifi")}<span><b>Kablolu internet</b><small>İndirme ve yayın kapalı olsun</small></span></li>
            <li>{icon("clock")}<span><b>1–3 saat ayır</b><small>Pakete göre değişir</small></span></li>
            <li>{icon("lock")}<span><b>Yedek al</b><small>Geri dönüş noktası oluşturulur, yine de yedekle</small></span></li>
          </ul>
        </div>
    </div></section>
"""
wrap("contact.html", "İletişim — FRAME PC optimizasyon",
     "FRAME ile Discord üzerinden iletişime geç. Sistem bilgisi şablonunu kopyala, doldur, gönder; paket ve randevuyu birlikte netleştirelim.", contact)


# ---------------------------------------------------------------- ÜCRETSİZ KONTROL
check = f"""
    <section class="page-hero"><div class="glow glow-soft" aria-hidden="true"></div><div class="container check-hero">
      <div>
        <div class="crumbs"><a href="index.html">Ana sayfa</a><span>/</span><span>Ücretsiz PC kontrolü</span></div>
        <span class="label">Ücretsiz PC performans kontrolü</span>
        <h1>Bilgisayarın masada <em>FPS mi bırakıyor?</em></h1>
        <p class="lead">Birkaç kısa soruyu cevapla, darboğaz puanını ve oyun bilgisayarını neyin tuttuğunu gör.</p>
        <div class="hero-actions"><a class="btn btn-primary" href="#kontrol">Ücretsiz kontrole başla {icon("arrow")}</a><a class="btn btn-ghost" href="pricing.html">Oturum ayarla</a></div>
        <p class="note">2 dakika sürer · Kayıt yok · Hiçbir veri gönderilmez</p>
      </div>
      <div class="side-panels">
        <div class="side-panel card"><h4>Kontrol ne soruyor</h4><ol>
          <li>Hangi oyunu oynadığını</li><li>Fark ettiğin ana sorunu</li><li>FPS hedefini</li><li>İşlemci, ekran kartı ve RAM'ini</li><li>Windows sürümünü</li><li>Şimdiye kadar ne denediğini</li><li>Sonuçları kime hazırlayacağımızı</li>
        </ol></div>
        <div class="side-panel card"><h4>Karşılığında ne alıyorsun</h4><ul>
          <li>{icon("check")}0–100 arası bir darboğaz puanı, sade bir açıklamayla</li>
          <li>{icon("check")}Önerilen sonraki adım: hizmet gerekmiyor, Temel, Gelişmiş veya Uzman</li>
          <li>{icon("check")}Kendin uygulayabileceğin bir PC optimizasyon kontrol listesi</li>
        </ul></div>
      </div>
    </div></section>

    <section class="section-tight"><div class="container">
      <div class="section-head"><h2>Nasıl çalışır</h2><p>Şişirme yazılım kurmadan kişisel donanım geri bildirimi. Puan, elle ayarladığımız sistemlere dayanarak anında hesaplanır.</p></div>
      <div class="grid-4">
        <article class="how-card card"><div class="how-top"><span class="icon-box">{icon("monitor")}</span><span class="tag">Hızlı özellikler</span></div><h3>Parçalarını gir</h3><p>İşlemci, ekran kartı, RAM, Windows sürümü ve cihaz tipini 30 saniyede seç.</p></article>
        <article class="how-card card"><div class="how-top"><span class="icon-box">{icon("doc")}</span><span class="tag">Belirtiler</span></div><h3>Oyun ve sorunu seç</h3><p>Hangi oyunu oynadığını ve ana belirtini seç: FPS düşüşü, girdi gecikmesi, mikro takılma.</p></article>
        <article class="how-card card"><div class="how-top"><span class="icon-box">{icon("gauge")}</span><span class="tag">Veriye dayalı</span></div><h3>Ayar ve yapılandırma denetimi</h3><p>Bilgisayarını geride tutabilecek ayarları kontrol ederiz. Canlı oturum sebebini test edebilir.</p></article>
        <article class="how-card card"><div class="how-top"><span class="icon-box">{icon("shield")}</span><span class="tag">Lafı dolandırmadan</span></div><h3>Dürüst geri bildirim</h3><p>Bilgisayarın sağlıklıysa söyleriz. Değilse hangi paketin uyduğunu net söyleriz.</p></article>
      </div>
      <div class="audit card">{icon("shield")}<span><b>Yapılandırma denetimi:</b> Bu araç işletim sistemi, sürücü, gecikme ve donanım dengesi darboğazlarını cevaplarına göre değerlendirir. Bu bir ayar kontrolüdür, yerel FPS testi değildir.</span></div>
    </div></section>

    <section class="section-tight" id="kontrol"><div class="container">
      <div class="wizard card" data-check aria-live="polite"></div>
    </div></section>

    <section class="section"><div class="container faq-page">
      <div class="section-head center"><h2>Sık sorulan sorular</h2></div>
      <div class="faq">
        <details open><summary>Performans kontrolü gerçekten ücretsiz mi?</summary><p>Evet. Kontrol tamamen ücretsizdir. Sistemin darboğaz gösteriyorsa bunu çözecek en uygun paketi öneririz; devam edip etmemek sana kalır.</p></details>
        <details><summary>Optimize olursam ne kadar FPS kazanırım?</summary><p>Donanımına ve sistemin şu an nasıl yapılandırıldığına bağlı. Fabrika ayarlarında veya kötü ayarlanmış sistemler en büyük sıçramayı yapar. Sabit bir sayı vermeyiz; kazanım sisteme göre değişir.</p></details>
        <details><summary>Optimizasyon süreci güvenli mi?</summary><p>Evet. Hiçbir anti-cheat atlatılmaz, güvenlik bileşenleri kapatılmaz. Her oturumda geri yükleme noktası oluşturulur; Uzman pakette tam sistem imajı alınır.</p></details>
        <details><summary>Darboğaz puanımı aldıktan sonra ne olur?</summary><p>Ücretsiz kontrol listesini kendin uygularsın. Yeterli gelmezse "Özeti kopyala" ile cevaplarını bize gönderirsin; canlı oturumu buna göre planlarız.</p></details>
        <details><summary>Kontrol için tüm parçalarımı bilmem gerekiyor mu?</summary><p>İşlemci, ekran kartı ve RAM yeterli. Yonga seti ve disk isteğe bağlıdır. Emin değilsen Görev Yöneticisi → Performans sekmesinden parça adlarını görebilirsin.</p></details>
        <details><summary>Temel, Gelişmiş ve Uzman arasındaki fark ne?</summary><p>Temel: sistem temizliği, servisler, güç planı. Gelişmiş: artı sürücü profili, ağ, oyun ayarları. Uzman: artı BIOS, bellek zamanlamaları, undervolt ve temiz özel Windows kurulumu.</p></details>
      </div>
    </div></section>
"""
wrap("check.html", "Ücretsiz PC performans kontrolü — FRAME darboğaz puanı",
     "7 soruluk ücretsiz PC kontrolü: 0–100 darboğaz puanı, önerilen paket ve kendin uygulayabileceğin optimizasyon kontrol listesi. Kayıt yok, veri gönderilmez.", check, '\n<script src="assets/js/check.js" defer></script>')

# ---------------------------------------------------------------- 404
nf = f"""
    <section class="page-hero"><div class="glow glow-soft" aria-hidden="true"></div><div class="container">
      <span class="label">404</span>
      <h1>Bu sayfa <em>bulunamadı.</em></h1>
      <p class="lead">Bağlantı değişmiş ya da yanlış yazılmış olabilir. Ana sayfadan devam edebilirsin.</p>
      <div class="hero-actions"><a class="btn btn-primary" href="index.html">Ana sayfa {icon("arrow")}</a><a class="btn btn-ghost" href="pricing.html">Paketler</a></div>
    </div></section>
"""
pages = ["index.html", "services.html", "process.html", "pricing.html", "faq.html", "contact.html", "check.html"]
sm = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>" + chr(10) + "<urlset xmlns=\"http://www.sitemaps.org/schemas/sitemap/0.9\">" + chr(10)
sm += "".join("  <url><loc>" + SITE_URL + "/" + p + "</loc></url>" + chr(10) for p in pages) + "</urlset>" + chr(10)
(OUT / "sitemap.xml").write_text(sm, encoding="utf-8")
(OUT / "robots.txt").write_text("User-agent: *" + chr(10) + "Allow: /" + chr(10) + "Sitemap: " + SITE_URL + "/sitemap.xml" + chr(10), encoding="utf-8")

wrap("404.html", "Sayfa bulunamadı — FRAME", "Aradığın sayfa bulunamadı.", nf)
