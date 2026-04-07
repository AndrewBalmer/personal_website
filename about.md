---
layout: page
title: About
description: "Short bio, profile information, and contact details."
---

{% assign profile = site.data.profile %}

<p style="font-size: 1rem; color: #475569;">
  Short bio, current affiliations, and direct contact details.
</p>

<div class="pub-links" style="margin: 0 0 2rem;">
  <a href="{{ '/assets/cv/andrew_balmer_cv.pdf' | relative_url }}" class="pub-badge pub-badge--pdf" target="_blank" rel="noopener">CV (PDF)</a>
  <a href="{{ '/assets/cv/andrew_balmer_cv.docx' | relative_url }}" class="pub-badge pub-badge--code" target="_blank" rel="noopener">CV (DOCX)</a>
  <a href="mailto:{{ profile.contact.professional_email }}" class="pub-badge pub-badge--doi">{{ profile.contact.professional_email }}</a>
</div>

<div class="project-detail-list">
  <article class="project-detail">
    <div class="project-detail__header">
      <div>
        <p class="project-detail__eyebrow">Profile</p>
        <h2 class="project-detail__title">Current role and affiliations</h2>
      </div>
    </div>

    <div class="project-detail__meta-grid">
      <div class="project-detail__meta-card">
        <h4>Current role</h4>
        <p>{{ profile.current_role.title }}, <a href="{{ profile.current_role.institution_url }}" target="_blank" rel="noopener">{{ profile.current_role.institution }}</a></p>
      </div>
      <div class="project-detail__meta-card">
        <h4>Current group</h4>
        <p><a href="{{ profile.current_role.group_url }}" target="_blank" rel="noopener">{{ profile.current_role.group }}</a></p>
      </div>
      <div class="project-detail__meta-card">
        <h4>Training</h4>
        <p>{{ profile.education.degree }}, <a href="{{ profile.education.institution_url }}" target="_blank" rel="noopener">{{ profile.education.institution }}</a> ({{ profile.education.years }})</p>
      </div>
      <div class="project-detail__meta-card">
        <h4>Location</h4>
        <p>{{ profile.contact.location }}</p>
      </div>
    </div>
  </article>

  <article class="project-detail">
    <div class="project-detail__header">
      <div>
        <p class="project-detail__eyebrow">Bio</p>
        <h2 class="project-detail__title">Short bio</h2>
      </div>
    </div>

    <p class="project-detail__summary">{{ profile.bio }}</p>
  </article>

  <article class="project-detail">
    <div class="project-detail__header">
      <div>
        <p class="project-detail__eyebrow">Collaboration</p>
        <h2 class="project-detail__title">Themes and contact</h2>
      </div>
    </div>

    <p class="project-detail__summary">{{ profile.currently_open_to }}</p>
    <div class="project-detail__meta-grid">
      <div class="project-detail__meta-card">
        <h4>Collaboration themes</h4>
        <ul class="project-detail__highlights">
          {% for item in profile.collaboration_themes %}
          <li>{{ item }}</li>
          {% endfor %}
        </ul>
      </div>
      <div class="project-detail__meta-card">
        <h4>Contact links</h4>
        <p><a href="mailto:{{ profile.contact.professional_email }}">{{ profile.contact.professional_email }}</a></p>
        <p><a href="{{ profile.contact.github_url }}" target="_blank" rel="noopener">GitHub</a></p>
        <p><a href="{{ profile.contact.linkedin_url }}" target="_blank" rel="noopener">LinkedIn</a></p>
        <p><a href="{{ profile.contact.scholar_url }}" target="_blank" rel="noopener">Google Scholar</a></p>
        <p><a href="{{ profile.contact.orcid_url }}" target="_blank" rel="noopener">ORCID</a></p>
      </div>
      <div class="project-detail__meta-card">
        <h4>Selected collaborators</h4>
        <ul class="project-detail__highlights">
          {% for item in profile.selected_collaborators %}
          <li><a href="{{ item.url }}" target="_blank" rel="noopener">{{ item.name }}</a></li>
          {% endfor %}
        </ul>
      </div>
    </div>
  </article>
</div>
