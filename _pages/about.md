---
title: "Yuan Chen 陈缘"
append_site_title: false
permalink: /
excerpt: "Astrochemistry from interstellar ices to complex organic molecules."
redirect_from:
  - /about/
---

<p class="page-kicker">Astrochemistry · Observations · Star formation</p>

I am a postdoctoral researcher at the [Max Planck Institute for Extraterrestrial Physics (MPE)](https://www.mpe.mpg.de/) in the Center for Astrochemical Studies (CAS), working with Silvia Spezzano and Paola Caselli. My research focuses on the formation and evolution of complex organic molecules in star-forming regions and the chemical connections between interstellar ices and gas. I combine **JWST** and **ALMA** observations with chemical models and laboratory spectra to study these processes. In October 2025, I completed my PhD in astronomy at Leiden University under the supervision of Ewine van Dishoeck. My PhD thesis, *[A song of gas and ice: the formation and evolution of complex organic molecules]({{ site.thesis_pdf | relative_url }})*, is available online.

I was born and raised in Guangzhou, a subtropical city in southern China known for its food and flowers. I “met” astronomy at fifteen through my high school’s astronomy club and have been an amateur astronomer ever since. I'm always proud of being an astronomer who really knows the stars in the sky. You can read more about my journey into astronomy [here]({{ '/cv/story/' | relative_url }}).

<div class="profile-actions">
  <a class="btn btn--primary" href="{{ '/research/' | relative_url }}">Explore my research</a>
  <a class="btn" href="{{ site.cv_pdf | relative_url }}">Download CV <span aria-hidden="true">↗</span></a>
</div>

## Research interests

- **Complex organic molecules (COMs):** their formation and chemical evolution in protostellar environments.
- **Interstellar ices:** infrared spectroscopy and the identification of molecular ice features with JWST.
- **The ice–gas connection:** comparing JWST ice measurements with ALMA observations of gas-phase molecules.

## Selected work

{% assign citation_metrics = site.data.citation_metrics %}
{% if citation_metrics.summary.h_index != nil %}
<div class="citation-summary">
  <span class="citation-h-index">h-index: <strong>{{ citation_metrics.summary.h_index }}</strong></span>
  <p class="citation-source"><a href="{{ citation_metrics.source_url }}">{{ citation_metrics.source }}</a> · {{ citation_metrics.date_label }}<br>{{ citation_metrics.summary.paper_count }} refereed publications · Includes self-citations</p>
</div>
{% endif %}

{% assign selected_papers = site.publications | where: 'featured', true | sort: 'date' | reverse %}
{% for paper in selected_papers %}
<div class="selected-paper">
  {% include publication-meta.html paper=paper author_label="Chen et al." %}
  <h3><a href="{{ paper.url | relative_url }}">{{ paper.title }}</a></h3>
</div>
{% endfor %}

[View all publications →]({{ '/publications/' | relative_url }})

## Beyond astronomy

I enjoy traveling, photography, and drawing.
