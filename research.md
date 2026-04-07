---
layout: page
title: Research Gallery
description: "Figure-led gallery of my recent research across genomics, resistance surveillance, and quantitative biology."
---

{% assign highlights = site.data.research_highlights %}

<p style="font-size: 1rem; color: #475569; max-width: 46rem;">
  A figure-led gallery of recent work across pathogen genomics, malaria
  surveillance, and antimicrobial resistance modelling. Each snapshot links to
  the paper and, where possible, a public project brief or code repository.
</p>

{% if highlights.size > 0 %}
<div class="snapshot-grid">
  {% for item in highlights %}
  <article class="snapshot-card">
    <div class="snapshot-card__media{% if item.media_style == 'banner' %} snapshot-card__media--banner{% endif %}">
      <img src="{{ item.image | relative_url }}" alt="{{ item.alt }}" loading="lazy">
    </div>
    <div class="snapshot-card__body">
      <div class="snapshot-card__topline">
        <p class="snapshot-card__eyebrow">{{ item.category }}</p>
        {% if item.metric_value %}
        <div class="snapshot-card__metric" aria-label="{{ item.metric_label }}">
          <strong>{{ item.metric_value }}</strong>
          <span>{{ item.metric_label }}</span>
        </div>
        {% endif %}
      </div>
      <h2 class="snapshot-card__title">{{ item.title }}</h2>
      <p class="snapshot-card__summary">{{ item.summary }}</p>
      <div class="snapshot-card__links">
        {% if item.paper_url %}
        <a href="{{ item.paper_url }}" class="pub-badge pub-badge--doi" target="_blank" rel="noopener">{{ item.paper_label | default: "Paper" }}</a>
        {% endif %}
        {% if item.code_url %}
        <a href="{{ item.code_url }}" class="pub-badge pub-badge--code" target="_blank" rel="noopener">Code</a>
        {% endif %}
        {% if item.project_url %}
        <a href="{{ item.project_url | relative_url }}" class="pub-badge pub-badge--muted">{{ item.project_label | default: "Project brief" }}</a>
        {% endif %}
      </div>
      <p class="snapshot-card__source">{{ item.source_note }}</p>
    </div>
  </article>
  {% endfor %}
</div>
{% endif %}
