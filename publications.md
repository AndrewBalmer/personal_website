---
layout: page
title: Publications
description: "Peer-reviewed publications by Andrew Balmer in computational biology, genomics, and machine learning."
---

{% assign pubs_by_year = site.data.publications | group_by: "year" | sort: "name" | reverse %}

{% for year_group in pubs_by_year %}
<h2 class="pubs-year">{{ year_group.name }}</h2>
<div class="pub-list">
  {% for pub in year_group.items %}
    {% include pub_card.html pub=pub %}
  {% endfor %}
</div>
{% endfor %}
