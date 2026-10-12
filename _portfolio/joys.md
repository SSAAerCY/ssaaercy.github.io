---
kind: "project"
project: "joys"
title: "JOYS"
expanded_name: "JWST Observations of Young protoStars"
tagline: "JWST · Protostellar ices and gas"
order: 2
excerpt: "In JOYS and its JOYS+ ice studies, I identify organic molecules in protostellar ices and compare their ice abundances with gas measurements from ALMA."
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

**JOYS** is a collaborative JWST program studying the physical and chemical environments of young stars. My work in JOYS and its JOYS+ ice studies focuses on organic molecules and ions in protostellar ices. I use laboratory spectra to identify their infrared absorption features, then compare the ice abundances with gas measurements from ALMA to see how the composition changes after sublimation.

## Connecting molecular ice and gas

Complex organic molecules are thought to form in icy grain mantles before entering the gas as a protostar heats its surroundings, but the extent to which the ice composition is preserved remains uncertain. My 2024 JOYS+ study addresses this question by combining JWST ice spectroscopy and ALMA gas observations of the low-mass protostars NGC 1333 IRAS 2A and B1-c to compare their molecular inventories across the two phases.

### Identifying the complex-ice inventory

To identify the molecules contributing to B1-c's ice absorption spectrum, I compared it with laboratory ice mixtures in the molecular fingerprint region between $\mathdefault{6.8}$ and $\mathdefault{8.8\,\mu m}$. The fitted components include organic molecules and ions, among them $\mathdefault{CH\_{3}CHO}$, $\mathdefault{C\_{2}H\_{5}OH}$, $\mathdefault{CH\_{3}OCH\_{3}}$, and $\mathdefault{CH\_{3}OCHO}$. I also modeled the ALMA emission lines to measure their gas-phase column densities for comparison with the ice.

{% include research-figure.html id="chen2024-fig7" %}

### Similarities and differences across phases

When the molecular column densities are normalized to $\mathdefault{CH\_{3}OH}$, $\mathdefault{CH\_{3}OCHO}$ and $\mathdefault{CH\_{3}OCH\_{3}}$ show similar ratios in ice and gas, consistent with inheritance during sublimation or a strong chemical link to $\mathdefault{CH\_{3}OH}$. In contrast, $\mathdefault{CH\_{3}CHO}$ and $\mathdefault{C\_{2}H\_{5}OH}$ have ice ratios that exceed their gas ratios by one to two orders of magnitude, suggesting that a simple transfer of the full ice inventory cannot explain every molecule.

{% include research-figure.html id="chen2024-fig9" %}

### Chemistry and observing geometry

Gas-phase processing after sublimation is one possible explanation for these differences, but the observing geometry also matters. ALMA primarily probes molecular emission from the warm, compact inner region, whereas JWST ice absorption samples material along the line of sight through the envelope. Different molecular distributions and beam dilution can therefore change the measured ratios even without chemical destruction. These effects need to be considered alongside gas-phase chemistry when interpreting the ice–gas comparison.

{% include research-figure.html id="chen2024-fig10" %}

## A broader view of complex ices

To assess how widespread weak complex-ice features are in young stellar systems, I analyzed JWST/MIRI-MRS spectra of 21 protostars and compared their absorption-band strengths and profiles. The study focuses on bands at $\mathdefault{7.02}$, $\mathdefault{7.24}$, $\mathdefault{7.40}$, and $\mathdefault{7.67\,\mu m}$, using laboratory spectra to evaluate their possible molecular carriers.

### From band strengths to molecular carriers

The $\mathdefault{7.24}$ and $\mathdefault{7.40\,\mu m}$ bands appear together in most of the observed Class 0 and Class 0/I protostars, and their integrated areas are strongly correlated. Both features are expected from $\mathdefault{HCOO^{-}}$ ice, which has absorption bands near these wavelengths. Their co-occurrence and correlated strengths strongly suggest a contribution from this ion, although laboratory comparisons are needed to determine how much of the absorption it can explain.

The left panel of Figure 3 in Chen et al. (2026) compares the two weak bands directly, alongside new laboratory measurements of $\mathdefault{HCOO^{-}}$ in different ice mixtures. The middle and right panels compare each weak band with the stronger $\mathdefault{CH\_{4}}$ band at $\mathdefault{7.67\,\mu m}$. All three band areas increase together, suggesting that they trace common ice reservoirs in protostellar envelopes. A source with weaker ice absorption or lower signal-to-noise may therefore contain the same carriers even when its weak bands are undetected.

The laboratory comparison in the left panel indicates that the tested $\mathdefault{HCOO^{-}}$ ice mixtures do not fully reproduce the observed band-area ratios. In the laboratory mixtures, its longer-wavelength band is stronger relative to the $\mathdefault{7.24\,\mu m}$ band than it is in the observations. The excess relative absorption at $\mathdefault{7.24\,\mu m}$ points to additional contributors, such as $\mathdefault{C\_{2}H\_{5}OH}$. The correlations therefore support $\mathdefault{HCOO^{-}}$ ice, while the band-area ratios suggest overlapping contributions from other species.

{% include research-figure.html id="chen2026-fig3" %}

### What the band profiles reveal

Figure 4 in Chen et al. (2026) provides a second test by comparing the peak wavelengths and widths of the observed bands with laboratory ice analogs. The tight grouping of the $\mathdefault{CH\_{4}}$ measurements in panel (c) supports a dominant carrier in broadly similar mixing environments. The agreement at both $\mathdefault{7.24}$ and $\mathdefault{7.40\,\mu m}$ in panels (a) and (b) favors $\mathdefault{HCOO^{-}}$ mixed with $\mathdefault{H\_{2}O}$ over pure $\mathdefault{HCOO^{-}}$ ice. The larger scatter in the other features is consistent with blends, including contributions from $\mathdefault{C\_{2}H\_{5}OH}$ and $\mathdefault{CH\_{3}CHO}$, and potentially $\mathdefault{CH\_{3}COCH\_{3}}$ at $\mathdefault{7.02\,\mu m}$.

{% include research-figure.html id="chen2026-fig4" %}

## Selected publications

{% include research-publication.html bibkey="Chen2026" %}
{% include research-publication.html bibkey="Chen2024icegas" %}
