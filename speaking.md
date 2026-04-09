---
layout: page
title: Speaking & Service
description: "Talks, posters, and academic service."
---

{% assign talks_by_year = site.data.talks | sort: "year" | reverse | group_by: "year" %}

{% if talks_by_year.size > 0 %}
## Talks & Presentations

{% for year_group in talks_by_year %}
<h3 class="pubs-year">{{ year_group.name }}</h3>
<ul class="talk-list">
  {% assign sorted_talks = year_group.items | sort: "type" %}
  {% for talk in sorted_talks %}
  <li class="talk-item">
    <div class="talk-item__meta">
      <span class="pub-tag">{{ talk.type | capitalize }}</span>
      {% if talk.invited %}<span class="pub-badge pub-badge--doi" style="font-size:0.65rem;">Invited</span>{% endif %}
    </div>
    <p class="talk-item__title">
      <strong>{{ talk.title }}</strong>
    </p>
    <p class="talk-item__venue">
      {{ talk.event }}{% if talk.location %} · {{ talk.location }}{% endif %}
    </p>
    {% if talk.slides != "" or talk.video != "" %}
    <div class="pub-links" style="margin-top:0.35rem;">
      {% if talk.slides != "" %}<a href="{{ talk.slides }}" class="pub-badge" target="_blank" rel="noopener">Slides</a>{% endif %}
      {% if talk.video != ""  %}<a href="{{ talk.video  }}" class="pub-badge pub-badge--preprint" target="_blank" rel="noopener">Video</a>{% endif %}
    </div>
    {% endif %}
  </li>
  {% endfor %}
</ul>
{% endfor %}
{% endif %}

---

## Service

See the [CV page]({{ '/cv/' | relative_url }}) for a full list of reviewing and committee service.
