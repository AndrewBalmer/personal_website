---
layout: page
title: CV
description: "Curriculum vitæ of Andrew Balmer — positions, education, publications, and awards."
---

{% assign cv = site.data.cv %}

<div class="cv-download-bar">
  <p class="cv-download-bar__text">
    Full curriculum vitæ available as downloadable PDF and Word documents.
  </p>
  <div class="pub-links" style="margin: 0;">
    <a href="{{ '/assets/cv/andrew_balmer_cv.pdf' | relative_url }}"
       class="btn btn--primary"
       target="_blank"
       rel="noopener">
      Download CV (PDF)
    </a>
    <a href="{{ '/assets/cv/andrew_balmer_cv.docx' | relative_url }}"
       class="btn btn--outline"
       target="_blank"
       rel="noopener">
      Download CV (DOCX)
    </a>
  </div>
</div>

<!-- ── Positions ────────────────────────────────────────────── -->
{% if cv.positions.size > 0 %}
<section class="cv-section">
  <h2 class="cv-section__title">Positions</h2>
  {% for entry in cv.positions %}
  <div class="cv-entry">
    <div class="cv-entry__year">{{ entry.year }}</div>
    <div class="cv-entry__body">
      <div class="cv-entry__title">{{ entry.title }}</div>
      <div class="cv-entry__place">{{ entry.institution }}{% if entry.location %}, {{ entry.location }}{% endif %}</div>
      {% if entry.note and entry.note != "" %}<p>{{ entry.note }}</p>{% endif %}
    </div>
  </div>
  {% endfor %}
</section>
{% endif %}

<!-- ── Education ─────────────────────────────────────────────── -->
{% if cv.education.size > 0 %}
<section class="cv-section">
  <h2 class="cv-section__title">Education</h2>
  {% for entry in cv.education %}
  <div class="cv-entry">
    <div class="cv-entry__year">{{ entry.year }}</div>
    <div class="cv-entry__body">
      <div class="cv-entry__title">{{ entry.degree }}</div>
      <div class="cv-entry__place">{{ entry.institution }}{% if entry.location %}, {{ entry.location }}{% endif %}</div>
      {% if entry.note and entry.note != "" %}<p>{{ entry.note }}</p>{% endif %}
    </div>
  </div>
  {% endfor %}
</section>
{% endif %}

<!-- ── Publications ───────────────────────────────────────────── -->
<section class="cv-section">
  <h2 class="cv-section__title">Publications</h2>
  <p style="font-size: 0.875rem; color: #64748b;">
    See the <a href="{{ '/publications/' | relative_url }}">full publications list</a>
    for details, links, and code.
  </p>
  {% assign pubs = site.data.publications | sort: "year" | reverse %}
  {% for pub in pubs %}
  <div class="cv-entry">
    <div class="cv-entry__year">{{ pub.year }}</div>
    <div class="cv-entry__body">
      <p style="margin-bottom:0.15rem;">
        {{ pub.authors | markdownify | remove: '<p>' | remove: '</p>' | strip }}.
        {% if pub.paper_url != "" %}
          "<strong><a href="{{ pub.paper_url }}" target="_blank" rel="noopener">{{ pub.title }}</a></strong>."
        {% else %}
          "<strong>{{ pub.title }}</strong>."
        {% endif %}
        <em>{{ pub.journal }}</em>{% if pub.volume %} {{ pub.volume }}{% endif %}{% if pub.pages %}: {{ pub.pages }}{% endif %}.
        {% if pub.paper_url != "" %}
          <a href="{{ pub.paper_url }}" target="_blank" rel="noopener">Paper</a>
        {% endif %}
        {% if pub.doi != "" %}
          <a href="https://doi.org/{{ pub.doi }}" target="_blank" rel="noopener">DOI</a>
        {% endif %}
        {% if pub.code_url != "" %}
          <a href="{{ pub.code_url }}" target="_blank" rel="noopener">Code</a>
        {% endif %}
      </p>
    </div>
  </div>
  {% endfor %}
</section>

<!-- ── Grants ─────────────────────────────────────────────────── -->
{% if cv.grants.size > 0 %}
<section class="cv-section">
  <h2 class="cv-section__title">Grants &amp; Funding</h2>
  {% for entry in cv.grants %}
  <div class="cv-entry">
    <div class="cv-entry__year">{{ entry.year }}</div>
    <div class="cv-entry__body">
      <div class="cv-entry__title">{{ entry.title }}</div>
      <div class="cv-entry__place">{{ entry.funder }}{% if entry.amount %} · {{ entry.amount }}{% endif %}</div>
      {% if entry.role %}<p>{{ entry.role }}</p>{% endif %}
    </div>
  </div>
  {% endfor %}
</section>
{% endif %}

<!-- ── Awards ────────────────────────────────────────────────── -->
{% if cv.awards.size > 0 %}
<section class="cv-section">
  <h2 class="cv-section__title">Awards &amp; Honours</h2>
  {% for entry in cv.awards %}
  <div class="cv-entry">
    <div class="cv-entry__year">{{ entry.year }}</div>
    <div class="cv-entry__body">
      <div class="cv-entry__title">{{ entry.title }}</div>
      {% if entry.institution %}<div class="cv-entry__place">{{ entry.institution }}</div>{% endif %}
    </div>
  </div>
  {% endfor %}
</section>
{% endif %}

<!-- ── Teaching ───────────────────────────────────────────────── -->
{% if cv.teaching.size > 0 %}
<section class="cv-section">
  <h2 class="cv-section__title">Teaching</h2>
  {% for entry in cv.teaching %}
  <div class="cv-entry">
    <div class="cv-entry__year">{{ entry.year }}</div>
    <div class="cv-entry__body">
      <div class="cv-entry__title">{{ entry.title }}</div>
      <div class="cv-entry__place">{{ entry.role }}{% if entry.institution %}, {{ entry.institution }}{% endif %}</div>
    </div>
  </div>
  {% endfor %}
</section>
{% endif %}

<!-- ── Service ────────────────────────────────────────────────── -->
{% if cv.service.size > 0 %}
<section class="cv-section">
  <h2 class="cv-section__title">Service</h2>
  {% for entry in cv.service %}
  <div class="cv-entry">
    <div class="cv-entry__year">{{ entry.year }}</div>
    <div class="cv-entry__body">
      <div class="cv-entry__title">{{ entry.title }}</div>
      {% if entry.venue %}<div class="cv-entry__place">{{ entry.venue }}</div>{% endif %}
    </div>
  </div>
  {% endfor %}
</section>
{% endif %}

<!-- ── Skills ────────────────────────────────────────────────── -->
{% if cv.skills.size > 0 %}
<section class="cv-section">
  <h2 class="cv-section__title">Skills &amp; Technologies</h2>
  <dl class="cv-skills">
    {% for group in cv.skills %}
    <div class="cv-skill-entry">
      <dt class="cv-skill-entry__label">{{ group.category }}</dt>
      <dd class="cv-skill-entry__body" style="margin:0;">
        <p style="margin:0;">{{ group.items }}</p>
      </dd>
    </div>
    {% endfor %}
  </dl>
</section>
{% endif %}
