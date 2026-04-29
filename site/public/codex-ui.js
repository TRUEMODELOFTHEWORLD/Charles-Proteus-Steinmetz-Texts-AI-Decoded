(function () {
  const root = document.documentElement;
  const storedMode = localStorage.getItem('codex-source-mode') || 'all';
  root.dataset.sourceMode = storedMode;

  function setMode(mode) {
    root.dataset.sourceMode = mode;
    localStorage.setItem('codex-source-mode', mode);
    document.querySelectorAll('[data-codex-mode]').forEach((button) => {
      button.setAttribute('aria-pressed', button.dataset.codexMode === mode ? 'true' : 'false');
    });
  }

  function buildReaderControls() {
    if (document.querySelector('.codex-reader-controls')) return;

    const panel = document.createElement('aside');
    panel.className = 'codex-reader-controls';
    panel.setAttribute('aria-label', 'Codex reader controls');
    panel.innerHTML = [
      '<div class="codex-control-row" role="group" aria-label="Reading layer filter">',
      '<button type="button" data-codex-mode="all">All layers</button>',
      '<button type="button" data-codex-mode="steinmetz-only">Steinmetz only</button>',
      '</div>',
      '<button type="button" class="codex-ask-toggle" aria-expanded="false">Ask this page</button>',
      '<label class="codex-translate">Translate',
      '<select aria-label="Translate this page">',
      '<option value="">Language</option>',
      '<option value="es">Spanish</option>',
      '<option value="fr">French</option>',
      '<option value="de">German</option>',
      '<option value="it">Italian</option>',
      '<option value="pt">Portuguese</option>',
      '<option value="ar">Arabic</option>',
      '<option value="hi">Hindi</option>',
      '<option value="zh-CN">Chinese</option>',
      '</select>',
      '</label>',
      '<form class="codex-ask-panel" hidden>',
      '<label>Ask using visible page text only',
      '<input name="q" type="search" autocomplete="off" placeholder="Try: hysteresis, ether, impedance" />',
      '</label>',
      '<div class="codex-ask-results" aria-live="polite"></div>',
      '</form>'
    ].join('');

    document.body.appendChild(panel);
    setMode(root.dataset.sourceMode || 'all');

    panel.querySelectorAll('[data-codex-mode]').forEach((button) => {
      button.addEventListener('click', () => setMode(button.dataset.codexMode));
    });

    const translate = panel.querySelector('.codex-translate select');
    translate.addEventListener('change', () => {
      if (!translate.value) return;
      const url = `https://translate.google.com/translate?sl=auto&tl=${encodeURIComponent(translate.value)}&u=${encodeURIComponent(location.href)}`;
      window.open(url, '_blank', 'noopener,noreferrer');
      translate.value = '';
    });

    const toggle = panel.querySelector('.codex-ask-toggle');
    const askPanel = panel.querySelector('.codex-ask-panel');
    toggle.addEventListener('click', () => {
      const isOpen = askPanel.hidden;
      askPanel.hidden = !isOpen;
      toggle.setAttribute('aria-expanded', String(isOpen));
      if (isOpen) askPanel.querySelector('input').focus();
    });

    setupAskPanel(askPanel);
  }

  function setupAskPanel(form) {
    const input = form.querySelector('input');
    const results = form.querySelector('.codex-ask-results');
    const contentRoot = document.querySelector('main') || document.body;

    function pageTextNodes() {
      return Array.from(contentRoot.querySelectorAll('p, li, td, blockquote, pre.source-text-loader, .source-text-loader'))
        .filter((node) => !node.closest('.codex-reader-controls'))
        .map((node) => node.textContent.replace(/\s+/g, ' ').trim())
        .filter((text) => text.length > 65);
    }

    function search() {
      const query = input.value.trim().toLowerCase();
      if (query.length < 2) {
        results.innerHTML = '<p>Type a term. Results are pulled only from this page.</p>';
        return;
      }

      const terms = query.split(/\s+/).filter(Boolean);
      const matches = pageTextNodes()
        .filter((text) => terms.every((term) => text.toLowerCase().includes(term)))
        .slice(0, 6);

      if (!matches.length) {
        results.innerHTML = '<p>No visible page passage matched that exact query.</p>';
        return;
      }

      results.innerHTML = matches
        .map((text) => `<p>${escapeHtml(text.length > 320 ? `${text.slice(0, 320)}...` : text)}</p>`)
        .join('');
    }

    input.addEventListener('input', search);
    form.addEventListener('submit', (event) => {
      event.preventDefault();
      search();
    });
  }

  function escapeHtml(value) {
    return value.replace(/[&<>"']/g, (char) => ({
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&#39;'
    })[char]);
  }

  function setupLightbox() {
    const images = Array.from(
      document.querySelectorAll(
        '.diagram-frame img, .codex-visual-card img, .home-portrait-card img, .home-portrait-grid img, .steinmetz-profile-media img'
      )
    );
    if (!images.length) return;

    const overlay = document.createElement('button');
    overlay.className = 'codex-lightbox';
    overlay.type = 'button';
    overlay.setAttribute('aria-label', 'Close diagram viewer');
    overlay.hidden = true;
    overlay.innerHTML = '<img alt="" />';
    document.body.appendChild(overlay);

    const overlayImage = overlay.querySelector('img');
    images.forEach((image) => {
      image.classList.add('codex-zoomable');
      image.addEventListener('click', () => {
        overlayImage.src = image.currentSrc || image.src;
        overlayImage.alt = image.alt || '';
        overlay.hidden = false;
        document.body.classList.add('codex-lightbox-open');
      });
    });

    overlay.addEventListener('click', () => {
      overlay.hidden = true;
      document.body.classList.remove('codex-lightbox-open');
    });

    document.addEventListener('keydown', (event) => {
      if (event.key === 'Escape') {
        overlay.hidden = true;
        document.body.classList.remove('codex-lightbox-open');
      }
    });
  }

  function setupSourceTextLoaders() {
    const loaders = Array.from(document.querySelectorAll('.source-text-loader[data-source-text-url]'));
    if (!loaders.length) return;

    loaders.forEach(async (loader) => {
      const url = loader.dataset.sourceTextUrl;
      if (!url) return;
      try {
        const response = await fetch(url);
        if (!response.ok) throw new Error(`HTTP ${response.status}`);
        const text = await response.text();
        loader.textContent = text || '[Source text asset is empty.]';
      } catch (error) {
        loader.textContent = `Could not load source text asset. Open it directly: ${url}`;
      }
    });
  }

  document.addEventListener('DOMContentLoaded', () => {
    buildReaderControls();
    setupSourceTextLoaders();
    setupLightbox();
  });
})();
