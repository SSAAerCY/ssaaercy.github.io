---
kind: "paper"
project: "coccoa"
bibkey: "Chen2023coccoa"
title: "Organic molecules in hot cores"
tagline: "CoCCoA · Chen et al. 2023"
order: 2
excerpt: "An ALMA survey of 14 high-mass protostars tests how oxygen-bearing organic chemistry compares across stellar masses."
image: "/images/research/chen2023-fig2.png"
carousel_figures: ["chen2023-fig2", "chen2023-fig4"]
image_alt: "Line-rich ALMA spectra of the 14 high-mass protostars in the CoCCoA sample."
---

Comparing organic-molecule abundances in low- and high-mass protostars lets us investigate whether stars of different masses share a similar chemical starting point. The CoCCoA survey provides a statistical sample of hot cores, the warm molecular regions around forming massive stars, for this comparison. In my 2023 study, I measured six oxygen-bearing complex organic molecules in 14 high-mass protostellar sources and compared their abundances with five low-mass protostars from the literature, as well as with chemical simulations and laboratory experiments.

## Turning rich spectra into molecular inventories

Figure 2 gives an overview of the ALMA spectra across the high-mass sample. Each spectrum is vertically offset, and the sources are ordered by their average line intensity. The crowded spectra demonstrate the richness of the gas-phase chemistry, while the highlighted $\mathdefault{CH\_{3}OCHO}$ and $\mathdefault{CH\_{3}OCH\_{3}}$ transitions show how prominent these molecules are across sources. Differences in brightness and line blending make spectral modeling essential for comparing molecular abundances.

I fitted the molecular emission to derive column densities and excitation temperatures for $\mathdefault{CH\_{3}CHO}$, $\mathdefault{C\_{2}H\_{5}OH}$, $\mathdefault{CH\_{3}OCH\_{3}}$, $\mathdefault{CH\_{3}OCHO}$, $\mathdefault{CH\_{2}OHCHO}$, and $\mathdefault{(CH\_{2}OH)\_{2}}$. Because the main $\mathdefault{CH\_{3}OH}$ lines are generally optically thick, I used the rarer $\mathdefault{CH\_{3}^{18}OH}$ isotopologue to infer its column density. This provides a more reliable reference for the abundance ratios than the saturated main-isotopologue lines.

{% include research-figure.html id="chen2023-fig2" %}

## Similar chemistry across stellar masses

Figure 4 plots the column-density ratio of each molecule to $\mathdefault{CH\_{3}OH}$ against bolometric luminosity. The red points represent high-mass CoCCoA sources and the blue points represent low-mass literature sources; arrows indicate upper limits. The gray lines and shaded regions summarize the combined sample, while the black dashed and dotted lines show modeled ratios after the cold-collapse and warm-up stages, respectively.

Across the six panels, the low- and high-mass sources occupy broadly overlapping ranges despite their very different luminosities, morphologies, and continuum brightness. There is no clear separation between the two groups. This supports formation under similar conditions, plausibly in icy grain mantles during the pre-stellar stage, before the environments around low- and high-mass stars diverge. Gas-phase formation may also contribute, so the similarity does not establish a unique formation history.

The strongest and most stable ratios are those of $\mathdefault{CH\_{3}OCH\_{3}}$ and $\mathdefault{CH\_{3}OCHO}$, typically a few percent of $\mathdefault{CH\_{3}OH}$ and scattered within roughly one order of magnitude. Their mutual ratio is also close to one, consistent with a chemical connection, such as shared precursors. The other four species have lower ratios or greater scatter, reaching one to two orders of magnitude. These differences show that a common overall inventory can coexist with molecule-specific chemistry.

{% include research-figure.html id="chen2023-fig4" %}

## What models and experiments still need to explain

The model lines in Figure 4 allow the abundance patterns to be tested against chemistry before and after the ice warms and sublimates. Many trends are reproduced, but the simulations tend to overestimate $\mathdefault{C\_{2}H\_{5}OH}$ and $\mathdefault{CH\_{2}OHCHO}$ relative to $\mathdefault{CH\_{3}OH}$. Gas-phase chemistry could affect the former, while differing emitting areas and beam dilution may contribute to discrepancies for the latter and $\mathdefault{(CH\_{2}OH)\_{2}}$.

Laboratory comparisons add another constraint: irradiation can enhance $\mathdefault{CH\_{3}OCHO}$ relative to $\mathdefault{CH\_{2}OHCHO}$ and $\mathdefault{(CH\_{2}OH)\_{2}}$, but the observed ratios can be higher still. The observations therefore provide both support for early ice chemistry and specific targets for improving reaction networks. By establishing these trends across a larger high-mass sample, the study supplies a reference for subsequent CoCCoA work and for direct ice–gas comparisons with JWST.

## Related publication

{% include research-publication.html bibkey="Chen2023coccoa" %}
