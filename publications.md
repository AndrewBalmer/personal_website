---
layout: page
title: Publications
description: "Peer-reviewed publications by Andrew Balmer in computational biology, genomics, and machine learning."
---

{% assign pubs = site.data.publications %}
{% assign pubs_by_year = site.data.publications | group_by: "year" | sort: "name" | reverse %}

<p style="font-size: 1rem; color: #475569; max-width: 46rem;">
  Publications and preprints across pathogen genomics, antimicrobial
  resistance, and quantitative biology. Entries below include short summaries,
  project context, and direct links to paper, DOI, PDF, code, and data where
  available.
</p>

<div class="pub-links" style="margin: 0 0 2rem;">
  <a href="https://scholar.google.com/citations?user={{ site.author.google_scholar }}"
     class="pub-badge pub-badge--doi" target="_blank" rel="noopener">Google Scholar</a>
  <a href="{{ '/cv/' | relative_url }}" class="pub-badge pub-badge--muted">View CV</a>
  <span class="pub-badge pub-badge--muted">{{ pubs.size }} listed publications</span>
</div>

{% for year_group in pubs_by_year %}
<h2 class="pubs-year">{{ year_group.name }}</h2>
<div class="pub-list">
  {% for pub in year_group.items %}
    {% include pub_card.html pub=pub detailed=true %}
  {% endfor %}
</div>
{% endfor %}
