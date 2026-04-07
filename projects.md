---
layout: page
title: Projects
description: "Software, tools, and pipelines developed by Andrew Balmer."
---

{% assign active   = site.data.projects | where: "status", "active"   | sort: "year" | reverse %}
{% assign archived = site.data.projects | where: "status", "archived" | sort: "year" | reverse %}

<p style="font-size: 0.95rem; color: #64748b; max-width: 48rem;">
  GitHub buttons are shown only for repositories that are publicly reachable without a login.
  Some ongoing analysis repositories remain private or internal, so those cards are listed without public repo links.
  Public repositories are also available on
  <a href="https://github.com/AndrewBalmer?tab=repositories" target="_blank" rel="noopener">my GitHub repositories page</a>.
</p>

{% if active.size > 0 %}
<div class="project-grid">
  {% for proj in active %}
  {% assign brief_href = '#' | append: proj.slug %}
  <article class="project-card">
    <h2 class="project-card__title">
      {% if proj.url != "" %}
        <a href="{{ proj.url }}" target="_blank" rel="noopener">{{ proj.name }}</a>
      {% elsif proj.github != "" %}
        <a href="{{ proj.github }}" target="_blank" rel="noopener">{{ proj.name }}</a>
      {% else %}
        <a href="{{ brief_href }}">{{ proj.name }}</a>
      {% endif %}
    </h2>
    <p class="project-card__desc">{{ proj.description }}</p>
    <div class="project-card__links">
      {% if proj.github != "" %}
        <a href="{{ proj.github }}" class="pub-badge pub-badge--code"
           target="_blank" rel="noopener">GitHub</a>
      {% elsif proj.repo_visibility == "private" %}
        <span class="pub-badge pub-badge--muted">Private repo</span>
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
      <a href="{{ brief_href }}" class="pub-badge pub-badge--muted">Project brief</a>
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

{% assign all_projects = active | concat: archived %}
{% if all_projects.size > 0 %}
<h2 class="pubs-year" style="margin-top: 3rem;">Project Briefs</h2>
<div class="project-detail-list">
  {% for proj in all_projects %}
  <article id="{{ proj.slug }}" class="project-detail">
    <div class="project-detail__header">
      <div>
        <p class="project-detail__eyebrow">{% if proj.status == "active" %}Active project{% else %}Background project{% endif %}</p>
        <h3 class="project-detail__title">{{ proj.name }}</h3>
      </div>
      <div class="project-card__links">
        {% if proj.github != "" %}
          <a href="{{ proj.github }}" class="pub-badge pub-badge--code"
             target="_blank" rel="noopener">GitHub</a>
        {% elsif proj.repo_visibility == "private" %}
          <span class="pub-badge pub-badge--muted">Private repo</span>
        {% endif %}
        {% if proj.paper_url != "" %}
          <a href="{{ proj.paper_url }}" class="pub-badge pub-badge--doi"
             target="_blank" rel="noopener">Paper</a>
        {% elsif proj.paper_doi != "" %}
          <a href="https://doi.org/{{ proj.paper_doi }}" class="pub-badge pub-badge--doi"
             target="_blank" rel="noopener">Paper</a>
        {% endif %}
      </div>
    </div>

    <p class="project-detail__summary">{{ proj.overview | default: proj.description }}</p>

    <div class="project-detail__meta-grid">
      {% if proj.current_status != "" %}
      <div class="project-detail__meta-card">
        <h4>Status</h4>
        <p>{{ proj.current_status }}</p>
      </div>
      {% endif %}
      {% if proj.public_access != "" %}
      <div class="project-detail__meta-card">
        <h4>Public access</h4>
        <p>{{ proj.public_access }}</p>
      </div>
      {% endif %}
      {% if proj.tooling != "" %}
      <div class="project-detail__meta-card">
        <h4>Tooling</h4>
        <p>{{ proj.tooling }}</p>
      </div>
      {% endif %}
    </div>

    {% if proj.highlights.size > 0 %}
    <ul class="project-detail__highlights">
      {% for item in proj.highlights %}
      <li>{{ item }}</li>
      {% endfor %}
    </ul>
    {% endif %}
  </article>
  {% endfor %}
</div>
{% endif %}
