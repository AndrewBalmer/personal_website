/* ============================================================
   Andrew Balmer — Personal Website JS
   - ORCID API: live publications feed
   - Figures gallery with lightbox
   - Nav / misc
   ============================================================ */

// ── Configuration ────────────────────────────────────────────
const CONFIG = {
  ORCID_ID: '0000-0002-7146-0448',        // Update if ORCID ID changes
  ORCID_API: 'https://pub.orcid.org/v3.0', // Base URL for ORCID public API
  LINKEDIN_VANITY: 'andrewbalmer',          // LinkedIn profile vanity URL slug

  // Figures — add filenames and captions here.
  // The first entry (figure1_elife) is also shown on the homepage hero.
  FIGURES: [
    {
      file:    'figures/figure1_elife.png',
      label:   'Figure 1 — eLife',
      caption: 'Featured figure from eLife publication.'
    },
    {
      file:    'figures/figure2.png',
      label:   'Figure 2',
      caption: 'Figure from published work.'
    },
    {
      file:    'figures/figure3.png',
      label:   'Figure 3',
      caption: 'Figure from published work.'
    },
    {
      file:    'figures/figure4.png',
      label:   'Figure 4',
      caption: 'Figure from published work.'
    },
    {
      file:    'figures/figure5.png',
      label:   'Figure 5',
      caption: 'Figure from published work.'
    },
  ],
};

// ── Utility ──────────────────────────────────────────────────
const $ = (sel, ctx = document) => ctx.querySelector(sel);
const $$ = (sel, ctx = document) => [...ctx.querySelectorAll(sel)];

// ── Footer year ──────────────────────────────────────────────
const yearEl = $('#year');
if (yearEl) yearEl.textContent = new Date().getFullYear();

// ── Mobile nav toggle ────────────────────────────────────────
const navToggle = $('.nav-toggle');
const navLinks  = $('#nav-links');

if (navToggle && navLinks) {
  navToggle.addEventListener('click', () => {
    const expanded = navToggle.getAttribute('aria-expanded') === 'true';
    navToggle.setAttribute('aria-expanded', String(!expanded));
    navLinks.classList.toggle('open', !expanded);
  });

  // Close nav on link click (mobile)
  $$('a', navLinks).forEach(link => {
    link.addEventListener('click', () => {
      navLinks.classList.remove('open');
      navToggle.setAttribute('aria-expanded', 'false');
    });
  });
}

// ── ORCID Publications ────────────────────────────────────────
async function loadPublications() {
  const loading   = $('#pub-loading');
  const errorBox  = $('#pub-error');
  const list      = $('#pub-list');

  if (!list) return;

  try {
    const worksUrl = `${CONFIG.ORCID_API}/${CONFIG.ORCID_ID}/works`;
    const res = await fetch(worksUrl, {
      headers: { 'Accept': 'application/json' },
    });

    if (!res.ok) throw new Error(`ORCID API returned ${res.status}`);

    const data = await res.json();
    const groups = data.group || [];

    if (groups.length === 0) throw new Error('No works returned');

    // Build publication entries from work-summary groups
    const pubs = groups
      .map(group => {
        const summary = group['work-summary']?.[0];
        if (!summary) return null;

        const title   = summary.title?.title?.value || 'Untitled';
        const journal = summary['journal-title']?.value || '';
        const year    = summary['publication-date']?.year?.value || '';
        const type    = summary.type || '';
        const url     = summary.url?.value || '';

        // Prefer DOI link from external-ids
        let doiUrl = '';
        const extIds = summary['external-ids']?.['external-id'] || [];
        const doi = extIds.find(id => id['external-id-type'] === 'doi');
        if (doi) {
          const doiVal = doi['external-id-value'];
          doiUrl = doiVal.startsWith('http') ? doiVal : `https://doi.org/${doiVal}`;
        }

        return { title, journal, year, type, url: doiUrl || url };
      })
      .filter(Boolean)
      // Sort descending by year
      .sort((a, b) => (parseInt(b.year) || 0) - (parseInt(a.year) || 0));

    // Render list
    list.innerHTML = pubs.map(pub => {
      const typeClass = getTypeClass(pub.type);
      const typeLabel = formatType(pub.type);
      const titleHtml = pub.url
        ? `<a href="${escapeHtml(pub.url)}" target="_blank" rel="noopener">${escapeHtml(pub.title)}</a>`
        : escapeHtml(pub.title);

      return `
        <li class="pub-item">
          <span class="pub-year">${escapeHtml(pub.year)}</span>
          <div class="pub-content">
            <h4>${titleHtml}${typeLabel ? `<span class="pub-type ${typeClass}">${typeLabel}</span>` : ''}</h4>
            ${pub.journal ? `<p class="pub-journal">${escapeHtml(pub.journal)}</p>` : ''}
          </div>
        </li>`;
    }).join('');

    if (loading) loading.classList.add('hidden');
    list.classList.remove('hidden');

  } catch (err) {
    console.error('Failed to load ORCID publications:', err);
    if (loading)  loading.classList.add('hidden');
    if (errorBox) errorBox.classList.remove('hidden');
  }
}

function getTypeClass(type) {
  if (!type) return 'pub-type-other';
  const t = type.toLowerCase();
  if (t.includes('book') && !t.includes('chapter')) return 'pub-type-book';
  if (t.includes('journal') || t.includes('article')) return 'pub-type-article';
  if (t.includes('chapter')) return 'pub-type-chapter';
  return 'pub-type-other';
}

function formatType(type) {
  if (!type) return '';
  return type.replace(/_/g, ' ').toLowerCase().replace(/\b\w/g, c => c.toUpperCase());
}

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

// ── Figures Gallery ──────────────────────────────────────────
function buildFiguresGallery() {
  const grid = $('#figures-grid');
  if (!grid) return;

  grid.innerHTML = CONFIG.FIGURES.map((fig, i) => `
    <div class="fig-card">
      <img
        src="${fig.file}"
        alt="${fig.label}"
        loading="lazy"
        onerror="this.replaceWith(makePlaceholder('${fig.label}'))"
        data-index="${i}"
      />
      <div class="fig-info">
        <p class="fig-label">${fig.label}</p>
        <p class="fig-caption">${fig.caption}</p>
      </div>
    </div>
  `).join('');

  // Click to open lightbox
  grid.addEventListener('click', e => {
    const img = e.target.closest('img[data-index]');
    if (img) openLightbox(img.src, img.alt);
  });
}

window.makePlaceholder = function(label) {
  const div = document.createElement('div');
  div.className = 'fig-placeholder';
  div.textContent = `${label} — image not yet uploaded`;
  return div;
};

// ── Lightbox ─────────────────────────────────────────────────
function buildLightbox() {
  const lb = document.createElement('div');
  lb.id = 'lightbox';
  lb.innerHTML = `
    <button id="lightbox-close" aria-label="Close">&times;</button>
    <img id="lightbox-img" src="" alt="" />
  `;
  document.body.appendChild(lb);

  lb.addEventListener('click', e => {
    if (e.target === lb || e.target.id === 'lightbox-close') closeLightbox();
  });

  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') closeLightbox();
  });
}

function openLightbox(src, alt) {
  const lb  = $('#lightbox');
  const img = $('#lightbox-img');
  if (!lb || !img) return;
  img.src = src;
  img.alt = alt || '';
  lb.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeLightbox() {
  const lb = $('#lightbox');
  if (!lb) return;
  lb.classList.remove('open');
  document.body.style.overflow = '';
}

// ── Update hero figure caption from config ────────────────────
function setHeroFigureCaption() {
  const el = $('#hero-figure-caption');
  if (el && CONFIG.FIGURES[0]) {
    el.textContent = CONFIG.FIGURES[0].caption;
  }
}

// ── Init ─────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  loadPublications();
  buildLightbox();
  buildFiguresGallery();
  setHeroFigureCaption();
});
