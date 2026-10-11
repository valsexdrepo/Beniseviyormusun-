# FRAME — site notları

Statik site. Sunucuya yüklemek için bu klasörün tamamını kopyalaman yeterli.

## Mutlaka düzenle
- `assets/js/main.js` → `FRAME_CONFIG.discord`: Discord davet linkin. Tüm "Discord'dan yaz" butonları buradan beslenir.
- `assets/js/check.js` — ücretsiz PC kontrolü (7 adım). Oyun/sorun/donanım listeleri dosyanın başında, puanlama `score()` içinde. `check.html#adim=4` ile bir adıma, `check.html#ornek` ile örnek sonuca gidilir.
- `assets/js/bench.js` — ana sayfadaki önce/sonra bölümü. `BENCH` listesine kendi kayıtlarını ekle: `video: "cs2.webm"` (tek dosya, sol STOK / sağ OPTİMİZE) veya `video: {stock:"cs2-stok.webm", opt:"cs2-opt.webm"}`; dosyalar `assets/videos/` içinde. Rakamlar (avg, low, ft, gpu, cpu) kendi ölçümlerin olmalı; 0 bırakılanlar "—" görünür.
- `video/` klasörü yayına dahil değildir (başka siteden indirilen klipler orada; kendi kayıtların gelince `assets/videos/` altına koy).
- `tools/build.py` → `SITE_URL`: yayın adresin (paylaşım kartları ve canonical için).

## Yapı
- `assets/css/site.css` — tek tasarım dosyası. Renkler ve yazı tipleri en üstteki `:root` bloğunda.
- `assets/js/icons.js` — siteye özel ikon seti. Yeni ikon eklemek için bir `<symbol id="i-isim">` ekle, `<svg class="icon"><use href="#i-isim"/></svg>` ile kullan.
- `assets/fonts/` — fontlar siteye gömülü (Space Grotesk, DM Sans, JetBrains Mono). Dış servis yok, sayfalar arası yazı kayması yok.
- `assets/images/logo.svg`, `favicon.svg`, `og.png`, `apple-touch-icon.png` — marka dosyaları.
- `assets/js/check.js` — ücretsiz PC kontrolü (7 adım). Oyun/sorun/donanım listeleri dosyanın başında, puanlama `score()` içinde. `check.html#adim=4` ile bir adıma, `check.html#ornek` ile örnek sonuca gidilir.
- `assets/js/bench.js` — ana sayfadaki önce/sonra bölümü. `BENCH` listesine kendi kayıtlarını ekle: `video: "cs2.webm"` (tek dosya, sol STOK / sağ OPTİMİZE) veya `video: {stock:"cs2-stok.webm", opt:"cs2-opt.webm"}`; dosyalar `assets/videos/` içinde. Rakamlar (avg, low, ft, gpu, cpu) kendi ölçümlerin olmalı; 0 bırakılanlar "—" görünür.
- `video/` klasörü yayına dahil değildir (başka siteden indirilen klipler orada; kendi kayıtların gelince `assets/videos/` altına koy).
- `tools/build.py` — sayfaları ortak üst/alt bilgiyle üretir. Menü veya altbilgiyi değiştireceksen burada değiştirip `python tools/build.py` çalıştır. (HTML dosyalarını doğrudan da düzenleyebilirsin; o zaman betiği tekrar çalıştırma.)
