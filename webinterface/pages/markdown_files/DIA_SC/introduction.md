This module compares the MS1-level quantification tools for
data-independent acquisition (DIA), specifically for low input samples. 
The raw files provided for this module are presented in the preprint
showcasing the performance of the Astral on low-input samples 
[Julia A. Bubis et al., 2024](https://www.biorxiv.org/content/10.1101/2024.02.01.578358v2.full.pdf).

The samples contain tryptic peptides from Homo sapiens, and Saccharomyces cerevisiae,
mixed in different ratios (condition A and condition B), with three replicates
for each condition at 250pg. With these samples, we calculate
three metrics:
- To esimate the sensitivity of the workflows, we report the number
of unique precursors (charge modified sequence) quantified in a minimum
of 1 to 6 runs.
- To estimate the accuracy of the workflows, we report the mean 
absolute difference between measured and expected log2-transformed 
fold changes between conditions for proteins of the same species.


ProteoBench plots these three metrics to visualize workflow outputs
    from different tools, with different versions, and/or different
sets of parameters for the search and quantification.
The full description of the pre-processing steps and metrics
calculation is available [here](https://proteobench.readthedocs.io/en/stable/available-modules/3-DIA-Quantification-ion-level/).
