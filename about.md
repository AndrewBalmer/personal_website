---
layout: page
title: About
description: "Short bios, profile information, and contact details for Andrew Balmer."
---

{% assign profile = site.data.profile %}

<p style="font-size: 1rem; color: #475569; max-width: 46rem;">
  Short bio versions for press, seminars, collaborations, and job applications,
  together with current affiliations and direct contact details.
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
        <p class="project-detail__eyebrow">Bio versions</p>
        <h2 class="project-detail__title">Ready-to-use bios</h2>
      </div>
    </div>

    <div class="project-detail__meta-grid">
      <div class="project-detail__meta-card">
        <h4>Short bio</h4>
        <p>{{ profile.bios.short }}</p>
      </div>
      <div class="project-detail__meta-card">
        <h4>Press / media bio</h4>
        <p>{{ profile.bios.press }}</p>
      </div>
      <div class="project-detail__meta-card">
        <h4>Talks / seminar bio</h4>
        <p>{{ profile.bios.talks }}</p>
      </div>
      <div class="project-detail__meta-card">
        <h4>Jobs / applications bio</h4>
        <p>{{ profile.bios.jobs }}</p>
      </div>
    </div>
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
          <li>{{ item }}</li>
          {% endfor %}
        </ul>
      </div>
    </div>
  </article>
</div>
