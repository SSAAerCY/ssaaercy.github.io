---
title: "Yuan Chen 陈缘"
seo_title: "Yuan Chen 陈缘 | Astronomy & Astrochemistry"
append_site_title: false
show_beyond_astronomy: false
permalink: /
excerpt: "Yuan Chen (陈缘), astronomer and postdoctoral researcher at MPE, studying astrochemistry, star formation, and interstellar ices with JWST and ALMA."
redirect_from:
  - /about/
---

<p class="page-kicker">Astrochemistry · Observations · Star formation</p>

I am a postdoctoral researcher at the [Max Planck Institute for Extraterrestrial Physics (MPE)](https://www.mpe.mpg.de/) in the Center for Astrochemical Studies (CAS), working with Silvia Spezzano and Paola Caselli. I study how complex organic molecules form and evolve in star-forming regions, particularly how their chemistry changes between ice and gas. I use **JWST** spectra to identify molecules in interstellar ices and **ALMA** to measure their gas-phase abundances. To interpret these observations, I match ice absorption bands to laboratory spectra and compare molecular abundances with chemical models. In October 2025, I completed my PhD in astronomy at Leiden University under the supervision of Ewine van Dishoeck. My PhD thesis, *[A song of gas and ice: the formation and evolution of complex organic molecules]({{ site.thesis_pdf | relative_url }})*, is available online.

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

{% if page.show_beyond_astronomy %}
## Beyond astronomy

I enjoy traveling, photography, and drawing.
{% endif %}
