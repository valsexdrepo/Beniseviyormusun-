/* FRAME ikon seti — siteye özel, tek çizgi kalınlığında SVG semboller.
   Kullanım: <svg class="icon"><use href="#i-cpu"/></svg>
   Yeni ikon eklemek için aşağıya bir <symbol id="i-isim"> ekle. */
(function () {
  var sprite = '<svg xmlns="http://www.w3.org/2000/svg" style="position:absolute;width:0;height:0;overflow:hidden" aria-hidden="true">' +
    '<defs>' +

    /* Marka işareti: çerçeve köşeleri + F monogramı */
    '<symbol id="i-frame" viewBox="0 0 48 48" fill="none">' +
      '<path d="M6 16V10a4 4 0 0 1 4-4h6M32 6h6a4 4 0 0 1 4 4v6M42 32v6a4 4 0 0 1-4 4h-6M16 42h-6a4 4 0 0 1-4-4v-6" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>' +
      '<path d="M18 34V14h14v5h-8.6v3.4H30v5h-6.6V34H18Z" fill="currentColor"/>' +
    '</symbol>' +

    /* Donanım */
    '<symbol id="i-cpu" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' +
      '<rect x="6" y="6" width="12" height="12" rx="2"/><rect x="10" y="10" width="4" height="4" rx=".5"/>' +
      '<path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>' +
    '</symbol>' +
    '<symbol id="i-gpu" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' +
      '<path d="M2 5v14"/><rect x="5" y="6" width="17" height="11" rx="2"/><circle cx="11" cy="11.5" r="3"/><path d="M11 8.5v6M8 11.5h6"/><path d="M8 17v2h4v-2M14 17v2h4v-2"/>' +
    '</symbol>' +
    '<symbol id="i-ram" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' +
      '<rect x="3" y="7" width="18" height="10" rx="1.5"/><path d="M7 11v2M10.5 11v2M14 11v2M17 11v2M6 17v2M10 17v2M14 17v2M18 17v2"/>' +
    '</symbol>' +
    '<symbol id="i-chip" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' +
      '<rect x="4" y="4" width="16" height="16" rx="3"/><path d="M4 10h3M4 14h3M17 10h3M17 14h3M10 4v3M14 4v3M10 17v3M14 17v3"/><path d="M9.5 12h5"/>' +
    '</symbol>' +
    '<symbol id="i-monitor" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' +
      '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>' +
    '</symbol>' +
    '<symbol id="i-windows" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' +
      '<rect x="4" y="4" width="7" height="7" rx="1.5"/><rect x="13" y="4" width="7" height="7" rx="1.5"/><rect x="4" y="13" width="7" height="7" rx="1.5"/><rect x="13" y="13" width="7" height="7" rx="1.5"/>' +
    '</symbol>' +
    '<symbol id="i-game" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' +
      '<path d="M7 7h10a5 5 0 0 1 5 5v2.5a3.5 3.5 0 0 1-6.2 2.2L14.5 15h-5l-1.3 1.7A3.5 3.5 0 0 1 2 14.5V12a5 5 0 0 1 5-5Z"/><path d="M8 10v4M6 12h4M16 11h.01M18 13h.01"/>' +
    '</symbol>' +

    /* Performans ve süreç */
    '<symbol id="i-bolt" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' +
      '<path d="M13 2 4 14h7l-1 8 9-12h-7l1-8Z"/>' +
    '</symbol>' +
    '<symbol id="i-gauge" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' +
      '<path d="M4.9 18.5A9 9 0 1 1 19.1 18.5"/><path d="M12 13l4-4"/><circle cx="12" cy="13" r="1.4"/>' +
    '</symbol>' +
    '<symbol id="i-thermo" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' +
      '<path d="M10 4a2 2 0 1 1 4 0v9.2a4 4 0 1 1-4 0V4Z"/><path d="M12 10v5"/>' +
    '</symbol>' +
    '<symbol id="i-network" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' +
      '<circle cx="12" cy="5" r="2"/><circle cx="5" cy="18" r="2"/><circle cx="19" cy="18" r="2"/><path d="M12 7v4M12 11l-5.5 5.5M12 11l5.5 5.5"/>' +
    '</symbol>' +
    '<symbol id="i-sliders" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' +
      '<path d="M4 7h9M17 7h3M4 17h3M11 17h9"/><circle cx="15" cy="7" r="2"/><circle cx="9" cy="17" r="2"/>' +
    '</symbol>' +
    '<symbol id="i-layers" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' +
      '<path d="m12 3 9 5-9 5-9-5 9-5Z"/><path d="m3 13 9 5 9-5"/>' +
    '</symbol>' +
    '<symbol id="i-steps" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' +
      '<path d="M4 18h5v-5h5V8h6"/><path d="M17 5l3 3-3 3"/>' +
    '</symbol>' +
    '<symbol id="i-test" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' +
      '<path d="M4 19h16"/><path d="M5 15l4-5 3 3 3-6 4 4"/>' +
    '</symbol>' +

    /* Güven */
    '<symbol id="i-shield" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' +
      '<path d="M12 3 5 6v5c0 4.5 3 8 7 10 4-2 7-5.5 7-10V6l-7-3Z"/><path d="m9 12 2 2 4-4"/>' +
    '</symbol>' +
    '<symbol id="i-eye" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' +
      '<path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12Z"/><circle cx="12" cy="12" r="3"/>' +
    '</symbol>' +
    '<symbol id="i-rollback" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' +
      '<path d="M3 12a9 9 0 1 0 3-6.7"/><path d="M3 4v5h5"/><path d="M12 8v4l2.5 2.5"/>' +
    '</symbol>' +
    '<symbol id="i-lock" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' +
      '<rect x="5" y="10" width="14" height="10" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/><path d="M12 14v2"/>' +
    '</symbol>' +
    '<symbol id="i-hand" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round">' +
      '<path d="M8 12V5.5a1.5 1.5 0 0 1 3 0V11M11 10V4.5a1.5 1.5 0 0 1 3 0V11M14 10.5V6a1.5 1.5 0 0 1 3 0v8.5a6 6 0 0 1-6 6h-.5a6 6 0 0 1-4.9-2.5L3.4 15a1.5 1.5 0 0 1 2.3-1.9L8 15.5"/>' +
    '</symbol>' +

    /* Arayüz */
    '<symbol id="i-check" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12.5 4.5 4.5L19 7.5"/></symbol>' +
    '<symbol id="i-minus" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 12h12"/></symbol>' +
    '<symbol id="i-arrow" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12h15M13 6l6 6-6 6"/></symbol>' +
    '<symbol id="i-arrow-ne" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7M8 7h9v9"/></symbol>' +
    '<symbol id="i-chat" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M4 6a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H9l-5 4V6Z"/><path d="M8 9h8M8 12.5h5"/></symbol>' +
    '<symbol id="i-clock" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></symbol>' +
    '<symbol id="i-doc" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M7 3h7l5 5v13H7V3Z"/><path d="M14 3v5h5M10 12h5M10 16h5"/></symbol>' +
    '<symbol id="i-copy" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15V6a2 2 0 0 1 2-2h9"/></symbol>' +
    '<symbol id="i-wifi" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.75" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9.5a14 14 0 0 1 18 0M6.5 13a9 9 0 0 1 11 0M10 16.5a4 4 0 0 1 4 0"/><circle cx="12" cy="19.5" r=".8" fill="currentColor"/></symbol>' +
    '<symbol id="i-menu" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></symbol>' +
    '<symbol id="i-close" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></symbol>' +
    '<symbol id="i-dot" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5" fill="currentColor"/></symbol>' +

    '</defs></svg>';

  var holder = document.createElement("div");
  holder.innerHTML = sprite;
  var insert = function () { document.body.insertBefore(holder.firstChild, document.body.firstChild); };
  if (document.body) insert(); else document.addEventListener("DOMContentLoaded", insert);
})();
