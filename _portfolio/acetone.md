---
kind: "paper"
project: "coccoa"
bibkey: "Chen2025acetone"
title: "The chemical evolution of CH₃COCH₃"
tagline: "CoCCoA · Chen et al. 2025"
order: 1
excerpt: "ALMA measurements and chemical models explore why CH₃COCH₃ is abundant and how its chemistry changes from ice to gas."
image: "/images/research/chen2025-fig7.png"
carousel_figures: ["chen2025-fig7", "chen2025-fig5", "chen2025-fig8"]
image_alt: "A chemical network illustrating proposed formation pathways of CH3COCH3 and related organic molecules."
---

$\mathdefault{CH\_{3}COCH\_{3}}$ is among the most abundant three-carbon oxygen-bearing molecules detected in space, yet its chemistry is less well understood than that of many smaller organic molecules. In my 2025 CoCCoA study, I measured its abundance in 12 high-mass protostars with ALMA and compared the observations with formation pathways proposed in laboratory experiments and theoretical work. Chemical simulations helped test how these pathways might affect its abundance as material moves from ice into the gas.

## A surprisingly abundant three-carbon molecule

I modeled $\mathdefault{CH\_{3}COCH\_{3}}$ emission alongside $\mathdefault{C\_{2}H\_{5}CHO}$, $\mathdefault{CH\_{2}CO}$, and $\mathdefault{CH\_{3}CCH}$, which may be linked to its chemistry. $\mathdefault{CH\_{3}COCH\_{3}}$, $\mathdefault{CH\_{2}CO}$, and $\mathdefault{CH\_{3}CCH}$ are firmly detected throughout the sample. $\mathdefault{C\_{2}H\_{5}CHO}$ remains tentative because the data contain too few unblended diagnostic lines, so its abundances are treated as upper limits. The excitation and emission morphology place the oxygen-bearing species mainly in hot cores, while $\mathdefault{CH\_{3}CCH}$ can trace more extended outflow material.

Figure 5 in Chen et al. (2025) compares the mean column-density ratios relative to $\mathdefault{CH\_{3}OH}$ in low- and high-mass protostars. Blue and red bars distinguish the two samples; the hatched regions show their dispersion, and the numbers beneath the bars indicate how many sources contribute. Despite having an extra carbon atom, $\mathdefault{CH\_{3}COCH\_{3}}$ is not necessarily less abundant than the two-carbon species and can exceed $\mathdefault{CH\_{3}CHO}$ and $\mathdefault{CH\_{2}OHCHO}$.

The aldehydes in this comparison are less abundant than several other oxygen-bearing molecules with the same number of carbon atoms, while $\mathdefault{CH\_{3}OCH\_{3}}$ and $\mathdefault{CH\_{3}OCHO}$ are particularly abundant. These differences could arise because formation pathways favor ethers, esters, and ketones, or because aldehydes are destroyed or converted more efficiently after entering the gas. The observed abundances alone cannot distinguish between these possibilities.

{% include research-figure.html id="chen2025-fig5" %}

## Proposed formation pathways

Figure 7 in Chen et al. (2025) summarizes the proposed routes to $\mathdefault{CH\_{3}COCH\_{3}}$ formation. Solid and dashed arrows distinguish ice and gas reactions, and the different colors identify the simulations, calculations, or experiments behind each proposal. In the MAGICKAL network, one solid-phase route builds $\mathdefault{CH\_{3}COCH\_{3}}$ through $\mathdefault{CH\_{2}CO}$ and $\mathdefault{CH\_{3}CHO}$. Other routes involve hydrogen abstraction from radicals related to $\mathdefault{i\text{-}C\_{3}H\_{7}OH}$ or gas-phase reactions of $\mathdefault{2\text{-}C\_{3}H\_{7}}$ with atomic oxygen.

Additional proposals connect $\mathdefault{CH\_{3}COCH\_{3}}$ to reactions of $\mathdefault{CH\_{2}CO}$ with $\mathdefault{CH\_{3}}$, and to oxygen addition to $\mathdefault{CH\_{3}CH{=}CH\_{2}}$ in irradiated ices. Because these reactions can also produce other isomers, their relative yields could help distinguish between pathways. Some theoretical calculations assume conditions unlike interstellar environments, however, and the reaction efficiencies and branching ratios remain poorly constrained. It is therefore still unclear how much each route contributes in protostars.

{% include research-figure.html id="chen2025-fig7" %}

## Testing the network with abundance ratios

Figure 8 in Chen et al. (2025) compares $\mathdefault{CH\_{3}COCH\_{3}}$ with four related species as a function of source luminosity. Within the high-mass CoCCoA sample, its gas-phase ratios relative to $\mathdefault{CH\_{3}CHO}$, $\mathdefault{CH\_{2}CO}$, and $\mathdefault{CH\_{3}CCH}$ generally vary by about an order of magnitude without a clear dependence on luminosity. Many low-mass measurements are comparable, although IRAS 16293 has particularly low ratios relative to $\mathdefault{CH\_{3}CHO}$ and $\mathdefault{CH\_{2}CO}$. Differences in the spatial distribution of molecular emission may contribute to these outliers.

MAGICKAL reproduces several of the observed abundance relationships, consistent with the proposed chemical connections. This agreement does not identify a dominant pathway, since different networks can yield similar ratios and errors in two modeled abundances can partly cancel.

The clearest disagreement is in panel (c), where $\mathdefault{CH\_{3}COCH\_{3}}$ is at least an order of magnitude more abundant than $\mathdefault{C\_{2}H\_{5}CHO}$ in the gas, whereas the models predict much more comparable amounts. The upward triangles are lower limits on this ratio because $\mathdefault{C\_{2}H\_{5}CHO}$ itself is constrained by upper limits. The discrepancy suggests missing or underestimated destruction pathways for aldehydes, or differences in the formation efficiencies of the two isomers.

Panel (d) uses $\mathdefault{CH\_{3}CCH}$ as an indirect probe because it is a hydrogenation precursor of $\mathdefault{CH\_{3}CH{=}CH\_{2}}$. Its abundance relative to $\mathdefault{CH\_{3}COCH\_{3}}$ is suggestive of a chemical connection, but direct observations of $\mathdefault{CH\_{3}CH{=}CH\_{2}}$ and additional products are needed to test that pathway. The potentially different emitting regions of $\mathdefault{CH\_{3}CCH}$ and $\mathdefault{CH\_{3}COCH\_{3}}$ also complicate the comparison.

{% include research-figure.html id="chen2025-fig8" %}

## Evolution after sublimation

JWST measurements in the two available low-mass targets suggest that $\mathdefault{CH\_{3}COCH\_{3}/CH\_{3}OH}$ is about an order of magnitude higher in ice than in typical protostellar gas. If the ice abundances are reliable, this points to processing after sublimation that reduces $\mathdefault{CH\_{3}COCH\_{3}}$ relative to $\mathdefault{CH\_{3}OH}$. The small ice sample and the tentative identification in IRAS 2A remain important limitations.

To explain these observations, chemical models need formation and destruction pathways that account for both the high gas-phase abundance of $\mathdefault{CH\_{3}COCH\_{3}}$ and the much lower abundance of related aldehydes. Its behavior across the two phases also tests how well these networks describe the survival of larger organic molecules after sublimation.

## Related publication

{% include research-publication.html bibkey="Chen2025acetone" %}
