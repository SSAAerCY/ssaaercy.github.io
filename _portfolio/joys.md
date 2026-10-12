---
kind: "project"
project: "joys"
title: "JOYS"
expanded_name: "JWST Observations of Young protoStars"
tagline: "JWST · Protostellar ices and gas"
order: 2
excerpt: "Within JOYS and its JOYS+ ice studies, I investigate the molecular inventories of young stellar systems and the connection between complex ices and gas."
image: "/images/research/chen2026-fig3.png"
image_alt: "Correlations between protostellar ice bands, compared with laboratory ice measurements."
project_website: "https://miri.strw.leidenuniv.nl/"
project_logo: "/images/research/joys-logo.png"
---

<div class="project-resource">
  <a class="project-resource-logo" href="{{ page.project_website }}" aria-label="Visit the JOYS project website">
    <img src="{{ page.project_logo | relative_url }}" alt="JOYS: JWST Observations of Young protoStars" width="1147" height="1245">
  </a>
  <a href="{{ page.project_website }}">Visit the JOYS project website <span aria-hidden="true">↗</span></a>
</div>

**JOYS** is a collaborative JWST program investigating the physical and chemical environments of young stars. Within JOYS and its JOYS+ ice studies, my work focuses on complex organic molecules and the connection between their solid and gas phases. I combine infrared ice spectroscopy, laboratory measurements, and complementary ALMA observations to trace the molecular inventory of protostars and investigate how it changes as ices sublimate into the gas.

## Connecting molecular ice and gas

Complex organic molecules are thought to form in icy grain mantles before entering the gas as a protostar heats its surroundings, but the extent to which the ice composition is preserved remains uncertain. My 2024 JOYS+ study addresses this question by combining JWST ice spectroscopy and ALMA gas observations of the low-mass protostars NGC 1333 IRAS 2A and B1-c to compare their molecular inventories across the two phases.

### Identifying the complex-ice inventory

To identify the molecules contributing to B1-c's ice absorption spectrum, I compared it with laboratory ice mixtures in the molecular fingerprint region between $\mathdefault{6.8}$ and $\mathdefault{8.8\,\mu m}$. The decomposition constrains a rich mixture of organic molecules and ions, including $\mathdefault{CH\_{3}CHO}$, $\mathdefault{C\_{2}H\_{5}OH}$, $\mathdefault{CH\_{3}OCH\_{3}}$, and $\mathdefault{CH\_{3}OCHO}$. Complementary modeling of the ALMA emission lines provides gas-phase column densities for comparison with these ice measurements.

{% include research-figure.html id="chen2024-fig7" %}

### Similarities and differences across phases

When the molecular column densities are normalized to $\mathdefault{CH\_{3}OH}$, $\mathdefault{CH\_{3}OCHO}$ and $\mathdefault{CH\_{3}OCH\_{3}}$ show similar ratios in ice and gas, consistent with inheritance during sublimation or a strong chemical link to $\mathdefault{CH\_{3}OH}$. In contrast, $\mathdefault{CH\_{3}CHO}$ and $\mathdefault{C\_{2}H\_{5}OH}$ have ice ratios that exceed their gas ratios by one to two orders of magnitude, suggesting that a simple transfer of the full ice inventory cannot explain every molecule.

{% include research-figure.html id="chen2024-fig9" %}

### Chemistry and observing geometry

Gas-phase processing after sublimation is one possible explanation for these differences, but the observing geometry also matters. ALMA primarily probes molecular emission from the warm, compact inner region, whereas JWST ice absorption samples material along the line of sight through the envelope. Different molecular distributions and beam dilution can therefore change the measured ratios even without chemical destruction. The study considers both effects rather than assigning every ice–gas difference to a single chemical mechanism.

{% include research-figure.html id="chen2024-fig10" %}

## A broader view of complex ices

To assess how widespread weak complex-ice features are in young stellar systems, I analyzed JWST/MIRI-MRS spectra of 21 protostars and compared their absorption-band strengths and profiles. The study focuses on bands at $\mathdefault{7.02}$, $\mathdefault{7.24}$, $\mathdefault{7.40}$, and $\mathdefault{7.67\,\mu m}$, using laboratory spectra to evaluate their possible molecular carriers.

### From band strengths to molecular carriers

The $\mathdefault{7.24}$ and $\mathdefault{7.40\,\mu m}$ bands occur together and have strongly correlated integrated strengths, motivating a comparison with laboratory spectra to test whether both features can be explained by a single ice species.

{% include research-figure.html id="chen2026-fig3" %}

### What the band profiles reveal

Although the $\mathdefault{CH\_{4}}$ band at $\mathdefault{7.67\,\mu m}$ has remarkably uniform peak wavelengths and widths across the sample, the other bands vary more between sources. Laboratory comparisons favor $\mathdefault{HCOO^{-}}$ as the main carrier of the $\mathdefault{7.24}$ and $\mathdefault{7.40\,\mu m}$ features, but $\mathdefault{HCOO^{-}}$ alone cannot reproduce their intensity ratios. Contributions from other species, including $\mathdefault{C\_{2}H\_{5}OH}$ and $\mathdefault{CH\_{3}CHO}$, therefore remain relevant.

{% include research-figure.html id="chen2026-fig4" %}

These results suggest that weak complex-ice features are widespread in protostars, while highlighting the need for laboratory constraints to disentangle overlapping molecular signatures.

## Selected publications

{% include research-publication.html bibkey="Chen2026" %}
{% include research-publication.html bibkey="Chen2024icegas" %}
