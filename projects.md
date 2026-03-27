---
layout: page
title: Projects
description: "Software, tools, and pipelines developed by Andrew Balmer."
---

{% assign active   = site.data.projects | where: "status", "active"   | sort: "year" | reverse %}
{% assign archived = site.data.projects | where: "status", "archived" | sort: "year" | reverse %}

{% if active.size > 0 %}
<div class="project-grid">
  {% for proj in active %}
  <article class="project-card">
    <h2 class="project-card__title">
      {% if proj.url != "" %}
        <a href="{{ proj.url }}" target="_blank" rel="noopener">{{ proj.name }}</a>
      {% elsif proj.github != "" %}
        <a href="{{ proj.github }}" target="_blank" rel="noopener">{{ proj.name }}</a>
      {% else %}
        {{ proj.name }}
      {% endif %}
    </h2>
    <p class="project-card__desc">{{ proj.description }}</p>
    <div class="project-card__links">
      {% if proj.github != "" %}
        <a href="{{ proj.github }}" class="pub-badge pub-badge--code"
           target="_blank" rel="noopener">GitHub</a>
      {% endif %}
      {% if proj.paper_url != "" %}
        <a href="{{ proj.paper_url }}" class="pub-badge pub-badge--doi"
           target="_blank" rel="noopener">Paper</a>
      {% elsif proj.paper_doi != "" %}
        <a href="https://doi.org/{{ proj.paper_doi }}" class="pub-badge pub-badge--doi"
           target="_blank" rel="noopener">Paper</a>
      {% endif %}
      {% if proj.url != "" %}
        <a href="{{ proj.url }}" class="pub-badge"
           target="_blank" rel="noopener">Website</a>
      {% endif %}
    </div>
    {% if proj.tags.size > 0 %}
    <div class="pub-tags" aria-label="Tags">
      {% for tag in proj.tags %}<span class="pub-tag">{{ tag }}</span>{% endfor %}
    </div>
    {% endif %}
  </article>
  {% endfor %}
</div>
{% endif %}

{% if archived.size > 0 %}
<h2 class="pubs-year" style="margin-top: 3rem;">Past &amp; Archived</h2>
<div class="project-grid">
  {% for proj in archived %}
  <article class="project-card" style="opacity: 0.75;">
    <h2 class="project-card__title">
      {% if proj.github != "" %}
        <a href="{{ proj.github }}" target="_blank" rel="noopener">{{ proj.name }}</a>
      {% else %}
        {{ proj.name }}
      {% endif %}
    </h2>
    <p class="project-card__desc">{{ proj.description }}</p>
    <div class="project-card__links">
      {% if proj.github != "" %}
        <a href="{{ proj.github }}" class="pub-badge pub-badge--code"
           target="_blank" rel="noopener">GitHub</a>
      {% endif %}
      {% if proj.paper_url != "" %}
        <a href="{{ proj.paper_url }}" class="pub-badge pub-badge--doi"
           target="_blank" rel="noopener">Paper</a>
      {% elsif proj.paper_doi != "" %}
        <a href="https://doi.org/{{ proj.paper_doi }}" class="pub-badge pub-badge--doi"
           target="_blank" rel="noopener">Paper</a>
      {% endif %}
    </div>
  </article>
  {% endfor %}
</div>
{% endif %}
