const menuToggle = document.querySelector(".menu-toggle");
const navLinks = document.querySelector("#nav-links");
const currentPage = document.body.dataset.page;
const progressBar = document.querySelector(".scroll-progress span");

if (currentPage && navLinks) {
  const pageLinks = {
    home: "index.html",
    services: "services.html",
    process: "process.html",
    pricing: "pricing.html",
    faq: "faq.html"
  };
  const currentHref = pageLinks[currentPage];

  if (currentHref) {
    navLinks.querySelectorAll("a[href]").forEach((link) => {
      if (link.getAttribute("href") === currentHref) {
        link.setAttribute("aria-current", "page");
      }
    });
  }
}

if (menuToggle && navLinks) {
  const closeMenu = () => {
    navLinks.classList.remove("open");
    menuToggle.setAttribute("aria-expanded", "false");
    menuToggle.setAttribute("aria-label", "Menüyü aç");
  };

  menuToggle.addEventListener("click", () => {
    const isOpen = navLinks.classList.toggle("open");
    menuToggle.setAttribute("aria-expanded", String(isOpen));
    menuToggle.setAttribute("aria-label", isOpen ? "Menüyü kapat" : "Menüyü aç");
  });

  navLinks.addEventListener("click", (event) => {
    if (event.target.closest("a")) closeMenu();
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") closeMenu();
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 620) closeMenu();
  }, { passive: true });
}

const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
const ambientScene = document.querySelector(".ambient-scene");

if (ambientScene) {
  const networkCanvas = document.createElement("canvas");
  const networkContext = networkCanvas.getContext("2d", { alpha: true });

  if (networkContext) {
    networkCanvas.className = "network-canvas";
    networkCanvas.setAttribute("aria-hidden", "true");
    ambientScene.append(networkCanvas);

    const nodes = [];
    const random = (min, max) => min + Math.random() * (max - min);
    let canvasWidth = 0;
    let canvasHeight = 0;
    let pixelRatio = 1;
    let previousFrame = 0;
    let animationFrame = 0;
    let pointerX = -1000;
    let pointerY = -1000;
    let pointerActive = false;

    const resizeNetwork = () => {
      const previousWidth = canvasWidth;
      const previousHeight = canvasHeight;
      pixelRatio = Math.min(window.devicePixelRatio || 1, 1.5);
      canvasWidth = window.innerWidth;
      canvasHeight = window.innerHeight;
      networkCanvas.width = Math.round(canvasWidth * pixelRatio);
      networkCanvas.height = Math.round(canvasHeight * pixelRatio);
      networkContext.setTransform(pixelRatio, 0, 0, pixelRatio, 0, 0);
      if (previousWidth && previousHeight) {
        nodes.forEach((node) => {
          node.originX *= canvasWidth / previousWidth;
          node.originY *= canvasHeight / previousHeight;
        });
      }

      const mobile = window.matchMedia("(max-width: 700px)").matches;
      const targetCount = Math.min(mobile ? 30 : 58, Math.round(canvasWidth / (mobile ? 15 : 22)));
      const driftRange = prefersReducedMotion
        ? (mobile ? [12, 22] : [18, 30])
        : (mobile ? [20, 36] : [30, 52]);
      while (nodes.length < targetCount) {
        const x = random(0, canvasWidth);
        const y = random(0, canvasHeight);
        nodes.push({
          x,
          y,
          originX: x,
          originY: y,
          phase: random(0, Math.PI * 2),
          phaseY: random(0, Math.PI * 2),
          driftX: random(driftRange[0], driftRange[1]),
          driftY: random(driftRange[0] * .65, driftRange[1] * .8),
          radius: random(.8, 1.6)
        });
      }
      nodes.length = targetCount;
      drawNetwork(0);
    };

    const drawNetwork = (timestamp) => {
      networkContext.clearRect(0, 0, canvasWidth, canvasHeight);

      for (const node of nodes) {
        const motionScale = prefersReducedMotion ? 3600 : 2400;
        const targetX = node.originX + Math.sin(timestamp / motionScale + node.phase) * node.driftX;
        const targetY = node.originY + Math.cos(timestamp / (motionScale * 1.25) + node.phaseY) * node.driftY;
        let mouseOffsetX = 0;
        let mouseOffsetY = 0;

        if (pointerActive) {
          const deltaX = node.x - pointerX;
          const deltaY = node.y - pointerY;
          const distance = Math.hypot(deltaX, deltaY);
          const radius = 165;
          if (distance < radius && distance > 0) {
            const influence = (1 - distance / radius) * 24;
            mouseOffsetX = deltaX / distance * influence;
            mouseOffsetY = deltaY / distance * influence;
          }
        }

        node.x += (targetX + mouseOffsetX - node.x) * .12;
        node.y += (targetY + mouseOffsetY - node.y) * .12;
      }

      const connectionDistance = window.matchMedia("(max-width: 700px)").matches ? 112 : 145;
      for (let i = 0; i < nodes.length; i += 1) {
        const node = nodes[i];
        for (let j = i + 1; j < nodes.length; j += 1) {
          const other = nodes[j];
          const distance = Math.hypot(node.x - other.x, node.y - other.y);
          if (distance < connectionDistance) {
            networkContext.beginPath();
            networkContext.moveTo(node.x, node.y);
            networkContext.lineTo(other.x, other.y);
            networkContext.strokeStyle = `rgba(190, 204, 216, ${(1 - distance / connectionDistance) * .2})`;
            networkContext.lineWidth = .7;
            networkContext.stroke();
          }
        }
      }

      for (const node of nodes) {
        networkContext.beginPath();
        networkContext.fillStyle = "rgba(220, 230, 239, .62)";
        networkContext.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
        networkContext.fill();
      }
    };

    const animateNetwork = (timestamp) => {
      animationFrame = 0;
      if (document.hidden) {
        previousFrame = 0;
        return;
      }

      const elapsed = previousFrame ? Math.min((timestamp - previousFrame) / 1000, .05) : 0;
      previousFrame = timestamp;

      drawNetwork(timestamp);
      animationFrame = window.requestAnimationFrame(animateNetwork);
    };

    const startNetwork = () => {
      if (!document.hidden && !animationFrame) {
        previousFrame = 0;
        animationFrame = window.requestAnimationFrame(animateNetwork);
      }
    };

    if (window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
      window.addEventListener("pointermove", (event) => {
        pointerX = event.clientX;
        pointerY = event.clientY;
        pointerActive = true;
      }, { passive: true });
      document.documentElement.addEventListener("pointerleave", () => {
        pointerActive = false;
      });
    }

    window.addEventListener("resize", resizeNetwork, { passive: true });
    document.addEventListener("visibilitychange", startNetwork);
    resizeNetwork();
    startNetwork();
  }
}

if (!prefersReducedMotion && window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
  let pointerFrame = 0;
  let activeCard = null;
  let pointerX = 0;
  let pointerY = 0;

  document.addEventListener("pointermove", (event) => {
    const card = event.target.closest(".service-card, .editorial-card, .price-card, .roadmap-card, .expectation-card, .pc-card");
    if (!card) {
      activeCard = null;
      return;
    }

    activeCard = card;
    pointerX = event.clientX;
    pointerY = event.clientY;

    if (!pointerFrame) {
      pointerFrame = window.requestAnimationFrame(() => {
        pointerFrame = 0;
        if (!activeCard) return;
        const bounds = activeCard.getBoundingClientRect();
        activeCard.style.setProperty("--pointer-x", `${pointerX - bounds.left}px`);
        activeCard.style.setProperty("--pointer-y", `${pointerY - bounds.top}px`);
      });
    }
  }, { passive: true });
}

if (progressBar) {
  let progressFrame = 0;
  const updateProgress = () => {
    progressFrame = 0;
    const scrollableHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = scrollableHeight > 0 ? window.scrollY / scrollableHeight : 0;
    progressBar.style.transform = `scaleX(${Math.min(1, Math.max(0, progress))})`;
  };
  const requestProgressUpdate = () => {
    if (!progressFrame) progressFrame = window.requestAnimationFrame(updateProgress);
  };

  window.addEventListener("scroll", requestProgressUpdate, { passive: true });
  window.addEventListener("resize", requestProgressUpdate, { passive: true });
  requestProgressUpdate();
}

const revealTargets = document.querySelectorAll(
  ".proof-item, .section-head, .service-card, .editorial-card, .roadmap-card, .expectation-card, .step, .price-card, .faq-list details, .contact-line, .cta-panel, .chart"
);

if (!prefersReducedMotion && "IntersectionObserver" in window) {
  document.body.classList.add("motion-enabled");
  revealTargets.forEach((element) => {
    element.classList.add("reveal");
    const siblingIndex = Array.from(element.parentElement.children).indexOf(element);
    element.style.setProperty("--reveal-delay", `${Math.min(siblingIndex * 75, 300)}ms`);
  });

  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: "0px 0px -35px 0px" });

  revealTargets.forEach((element) => revealObserver.observe(element));
} else {
  revealTargets.forEach((element) => element.classList.add("is-visible"));
}
