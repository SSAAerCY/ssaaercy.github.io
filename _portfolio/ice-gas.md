---
kind: "paper"
project: "joys"
bibkey: "Chen2024icegas"
title: "Connecting ice and gas"
tagline: "JWST × ALMA · Chen et al. 2024"
order: 2
excerpt: "Comparing organic molecules in the ices and gas of IRAS 2A and B1-c reveals both chemical inheritance and differences between phases."
image: "/images/research/chen2024-fig7.png"
carousel_figures: ["chen2024-fig7", "chen2024-fig1", "chen2024-fig9", "chen2024-fig10"]
image_alt: "JWST ice spectra of IRAS 2A and B1-c with a laboratory-based molecular decomposition of the B1-c spectrum."
---

Complex organic molecules are thought to form in icy grain mantles before entering the gas as a protostar heats its surroundings. How much of the ice composition survives this transition is still uncertain. In my 2024 JOYS+ study, I compared JWST ice spectra with high-resolution ALMA gas observations of the low-mass protostars NGC 1333 IRAS 2A and B1-c, looking for molecules whose relative abundances remain similar across the two phases and those that may undergo substantial chemical processing.

## Following molecules from grains to warm gas

Figure 1 in Chen et al. (2024) places the comparison within the evolution of a protostellar system. Ice mantles grow on cold dust grains, with changing compositions as the cloud becomes denser and molecules such as $\mathdefault{CO}$ freeze out. Heating by the young star eventually releases volatile material into the gas in the compact inner region, where ALMA can detect its molecular emission. JWST measures ice absorption against the infrared continuum, sampling material along the line of sight through the surrounding envelope.

With these observations, I can compare material still stored in cold ices with gas released near the protostar. The two telescopes do not necessarily sample the same parcel of material, however, so differences in measured abundances can reflect observing geometry as well as chemistry.

{% include research-figure.html id="chen2024-fig1" %}

## Identifying the complex-ice inventory

The top panel of Figure 7 in Chen et al. (2024) shows the isolated ice fingerprint spectra of IRAS 2A and B1-c between $\mathdefault{6.8}$ and $\mathdefault{8.8\,\mu m}$. Their similar absorption patterns suggest comparable inventories, despite differences in individual features. To identify the carriers in B1-c, I compared the observed spectrum with laboratory ice mixtures and used least-squares and Markov Chain Monte Carlo fitting to constrain their contributions and uncertainties.

The lower panel separates the combined absorption into molecular components. The strongest feature is due to $\mathdefault{CH\_{4}}$, while weaker, overlapping bands constrain species including $\mathdefault{HCOO^{-}}$, $\mathdefault{CH\_{3}CHO}$, $\mathdefault{C\_{2}H\_{5}OH}$, $\mathdefault{CH\_{3}OCH\_{3}}$, $\mathdefault{CH\_{3}OCHO}$, and $\mathdefault{CH\_{3}COCH\_{3}}$. The residual spectrum shows where the selected laboratory components reproduce the observations and where mismatches remain. In this analysis, $\mathdefault{CH\_{3}OCH\_{3}}$ and $\mathdefault{CH\_{3}COCH\_{3}}$ are considered firmly detected in B1-c, whereas their identifications in the earlier IRAS 2A analysis were tentative.

Most of the complex-ice profiles favor $\mathdefault{H\_{2}O}$-rich mixtures, although $\mathdefault{CH\_{3}OH}$-rich environments cannot always be excluded. $\mathdefault{CH\_{3}OCHO}$ is an exception: a mixture containing $\mathdefault{CO}$, $\mathdefault{H\_{2}CO}$, and $\mathdefault{CH\_{3}OH}$ matches its bands better, consistent with a possible connection to $\mathdefault{CO}$ hydrogenation. The band shapes constrain mixing environments more readily than temperature because many laboratory profiles remain similar over a broad temperature range before crystallization.

{% include research-figure.html id="chen2024-fig7" %}

## Similarities and differences across phases

I modeled the ALMA emission lines to derive gas-phase column densities and normalized the molecular inventories in both phases to $\mathdefault{CH\_{3}OH}$. Figure 9 in Chen et al. (2024) compares the gas measurements, shown as points, with the ice measurements, shown as shaded regions and dashed lines. Literature gas data from low- and high-mass protostars provide context for the two target sources; ice measurements are available for far fewer objects, with comet 67P/C-G included as a comparison.

The upper panels show that $\mathdefault{CH\_{3}OCHO}$ and $\mathdefault{CH\_{3}OCH\_{3}}$ have broadly consistent ratios in ice and gas. This is compatible with direct inheritance during sublimation, but a strong chemical connection to $\mathdefault{CH\_{3}OH}$ could also preserve similar ratios as the molecules evolve. The abundance agreement alone cannot distinguish these explanations.

In the lower panels, the ice ratios of $\mathdefault{CH\_{3}CHO}$ and $\mathdefault{C\_{2}H\_{5}OH}$ exceed typical gas ratios by one to two orders of magnitude. Destruction or conversion after sublimation could reduce their gas-phase abundances relative to $\mathdefault{CH\_{3}OH}$. A simple picture in which all molecules retain their relative ice abundances therefore does not explain the full comparison.

{% include research-figure.html id="chen2024-fig9" %}

## Chemistry and observing geometry

Figure 10 in Chen et al. (2024) illustrates how different molecular distributions can alter measured ratios. In the upper panel, emission from a compact gas component is diluted more strongly if it is unresolved by the ALMA beam. In the lower panel, JWST integrates ice absorption through the envelope; a molecule present over a more extended region can contribute a larger column density even if its local abundance is unchanged.

Our high-resolution ALMA data help limit beam dilution. In a simple envelope model, differences in the ice distributions alone cannot account for the full order-of-magnitude discrepancies under the assumed density distributions and formation and desorption boundaries. This leaves gas-phase reprocessing as a plausible explanation, although the model assumptions and the small ice sample prevent a unique interpretation. More sources with measurements in both phases, together with better-constrained chemical models, are needed to determine how much of the ice inventory survives into warm protostellar gas.

{% include research-figure.html id="chen2024-fig10" %}

## Related publication

{% include research-publication.html bibkey="Chen2024icegas" %}
