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

Stars of different masses develop very different environments, but their organic molecules may originate under similar conditions before a protostar forms. I investigated this possibility using the CoCCoA survey of hot cores, the warm molecular regions around forming massive stars. In my 2023 study, I measured six oxygen-bearing complex organic molecules in 14 high-mass protostellar sources and compared their abundances with those in five low-mass protostars from the literature. I also compared the abundance patterns with chemical simulations and laboratory experiments to examine their possible origins.

## Turning rich spectra into molecular inventories

The ALMA spectra in Figure 2 in Chen et al. (2023) contain many molecular emission lines. Each spectrum is vertically offset, and the sources are ordered by their average line intensity. The highlighted $\mathdefault{CH\_{3}OCHO}$ and $\mathdefault{CH\_{3}OCH\_{3}}$ transitions are prominent across the sample. Differences in line brightness and blending mean that the spectra need to be modeled before molecular abundances can be compared.

I fitted the molecular emission to derive column densities and excitation temperatures for $\mathdefault{CH\_{3}CHO}$, $\mathdefault{C\_{2}H\_{5}OH}$, $\mathdefault{CH\_{3}OCH\_{3}}$, $\mathdefault{CH\_{3}OCHO}$, $\mathdefault{CH\_{2}OHCHO}$, and $\mathdefault{(CH\_{2}OH)\_{2}}$. Because the main $\mathdefault{CH\_{3}OH}$ lines are generally optically thick, I used the rarer $\mathdefault{CH\_{3}^{18}OH}$ isotopologue to infer its column density. This provides a more reliable reference for the abundance ratios than the saturated main-isotopologue lines.

{% include research-figure.html id="chen2023-fig2" %}

## Similar chemistry across stellar masses

Figure 4 in Chen et al. (2023) plots the column-density ratio of each molecule to $\mathdefault{CH\_{3}OH}$ against bolometric luminosity. The red points represent high-mass CoCCoA sources and the blue points represent low-mass literature sources; arrows indicate upper limits. The gray lines and shaded regions summarize the combined sample, while the black dashed and dotted lines show modeled ratios after the cold-collapse and warm-up stages, respectively.

Across the six panels, the abundance ratios of the low- and high-mass sources broadly overlap despite their very different luminosities, morphologies, and continuum brightness. The lack of a clear separation is consistent with formation under similar conditions, plausibly in icy grain mantles during the pre-stellar stage, before the environments around low- and high-mass stars diverge. Gas-phase formation may also contribute, so similar ratios do not establish a unique formation history.

The highest and most consistent ratios are those of $\mathdefault{CH\_{3}OCH\_{3}}$ and $\mathdefault{CH\_{3}OCHO}$, typically a few percent of $\mathdefault{CH\_{3}OH}$ and scattered within roughly one order of magnitude. Their mutual ratio is also close to one, consistent with a chemical connection, such as shared precursors. The other four species have lower ratios or greater scatter, reaching one to two orders of magnitude. The broadly similar inventories therefore still leave room for differences in how individual molecules form and evolve.

{% include research-figure.html id="chen2023-fig4" %}

## What models and experiments still need to explain

The model lines in Figure 4 in Chen et al. (2023) show how the predicted ratios change as the ice warms and sublimates. The simulations reproduce many trends but tend to overestimate $\mathdefault{C\_{2}H\_{5}OH}$ and $\mathdefault{CH\_{2}OHCHO}$ relative to $\mathdefault{CH\_{3}OH}$. Gas-phase chemistry could affect the former, while differing emitting areas and beam dilution may contribute to discrepancies for the latter and $\mathdefault{(CH\_{2}OH)\_{2}}$.

Laboratory experiments show that irradiation can enhance $\mathdefault{CH\_{3}OCHO}$ relative to $\mathdefault{CH\_{2}OHCHO}$ and $\mathdefault{(CH\_{2}OH)\_{2}}$, yet the observed ratios can be higher still. Reproducing this contrast, along with the lower-than-predicted abundances of $\mathdefault{C\_{2}H\_{5}OH}$ and $\mathdefault{CH\_{2}OHCHO}$, will require further work on the reaction networks. The measured abundances across 14 high-mass sources also serve as a reference for later CoCCoA studies and direct ice–gas comparisons with JWST.

## Related publication

{% include research-publication.html bibkey="Chen2023coccoa" %}
