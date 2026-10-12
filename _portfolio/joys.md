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

I contribute to **JOYS**, a collaborative program exploring the environments of young stars with JWST. My work within JOYS and the JOYS+ ice studies focuses on complex organic molecules, combining infrared ice spectroscopy, laboratory measurements, and complementary ALMA gas observations. Together, these approaches trace the chemical inventory of protostars and test how it evolves between the solid and gas phases.

## Connecting molecular ice and gas

Complex organic molecules are thought to form in icy grain mantles and enter the gas as a young star heats its surroundings. Measuring both phases in the same source provides a direct way to test that connection. My 2024 JOYS+ study combines JWST ice spectroscopy and ALMA gas observations of the low-mass protostars NGC 1333 IRAS 2A and B1-c.

### Identifying the complex-ice inventory

I compared the ice absorption spectrum of B1-c with laboratory ice mixtures in the molecular fingerprint region between $\mathdefault{6.8}$ and $\mathdefault{8.8\,\mu m}$. The decomposition constrains a rich mixture of organic molecules and ions, including $\mathdefault{CH\_{3}CHO}$, $\mathdefault{C\_{2}H\_{5}OH}$, $\mathdefault{CH\_{3}OCH\_{3}}$, and $\mathdefault{CH\_{3}OCHO}$. ALMA emission-line modeling supplies the corresponding gas-phase column densities.

{% include research-figure.html id="chen2024-fig7" %}

### Similarities and differences across phases

Normalizing the molecular column densities to $\mathdefault{CH\_{3}OH}$ reveals two patterns. $\mathdefault{CH\_{3}OCHO}$ and $\mathdefault{CH\_{3}OCH\_{3}}$ have similar ratios in ice and gas, consistent with inheritance during sublimation or a strong chemical link to $\mathdefault{CH\_{3}OH}$. $\mathdefault{CH\_{3}CHO}$ and $\mathdefault{C\_{2}H\_{5}OH}$ have ice ratios that exceed their gas ratios by one to two orders of magnitude, suggesting that a simple transfer of the full ice inventory cannot explain every molecule.

{% include research-figure.html id="chen2024-fig9" %}

### Chemistry and observing geometry

Gas-phase processing after sublimation is one possible explanation for these differences, but the observing geometry also matters. ALMA primarily probes molecular emission from the warm, compact inner region, whereas JWST ice absorption samples material along the line of sight through the envelope. Different molecular distributions and beam dilution can therefore change the measured ratios even without chemical destruction. The study considers both effects rather than assigning every ice–gas difference to a single chemical mechanism.

{% include research-figure.html id="chen2024-fig10" %}

## A broader view of complex ices

How widespread are the weak signatures of complex ices in young stellar systems? In this study, I analyzed JWST/MIRI-MRS spectra of 21 protostars, measuring absorption bands at $\mathdefault{7.02}$, $\mathdefault{7.24}$, $\mathdefault{7.40}$, and $\mathdefault{7.67\,\mu m}$.

### From band strengths to molecular carriers

The $\mathdefault{7.24}$ and $\mathdefault{7.40\,\mu m}$ bands occur together and their integrated strengths are strongly correlated. Comparing these measurements with laboratory spectra tests whether a single ice species can explain both features.

{% include research-figure.html id="chen2026-fig3" %}

### What the band profiles reveal

The $\mathdefault{CH\_{4}}$ band at $\mathdefault{7.67\,\mu m}$ has remarkably uniform peak wavelengths and widths across the sample. The other bands vary more between sources. Laboratory comparisons favor $\mathdefault{HCOO^{-}}$ as the main carrier of the $\mathdefault{7.24}$ and $\mathdefault{7.40\,\mu m}$ features, but $\mathdefault{HCOO^{-}}$ alone cannot reproduce their intensity ratios. Contributions from other species, including $\mathdefault{C\_{2}H\_{5}OH}$ and $\mathdefault{CH\_{3}CHO}$, remain relevant.

{% include research-figure.html id="chen2026-fig4" %}

These results suggest that weak complex-ice features are widespread in protostars, while highlighting the need for laboratory constraints to disentangle overlapping molecular signatures.

## Selected publications

{% include research-publication.html bibkey="Chen2026" %}
{% include research-publication.html bibkey="Chen2024icegas" %}
