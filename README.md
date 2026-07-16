# UCSD Bioinformatics Learning Repository

This repository documents my completed coursework for UC San Diego's **Biology Meets Programming: Bioinformatics for Beginners** course.

It contains Python implementations of foundational bioinformatics algorithms related to DNA replication, pattern matching, k-mer analysis, GC skew, origin of replication prediction, motif discovery, randomized motif search, and Gibbs sampling.

## Course Status

**Completed**

## Topics Covered

### DNA Replication and Pattern Analysis

- DNA replication and origins of replication
- Pattern counting and pattern matching
- Frequent k-mer detection
- Reverse complements
- Circular genome analysis
- DnaA box identification

### GC Skew and Origin Prediction

- Symbol arrays
- Optimized symbol arrays
- GC skew arrays
- Minimum skew positions
- Hamming distance
- Approximate pattern matching
- Approximate pattern counting

### Greedy Motif Search

- Motif count matrices
- Profile matrices
- Consensus strings
- Motif scoring
- k-mer profile probability
- Profile-most probable k-mers
- Greedy motif search

### Stochastic Motif Search

- Pseudocounts
- Profiles with pseudocounts
- Greedy motif search with pseudocounts
- Random motif generation
- Randomized motif search
- Probability normalization
- Weighted random selection
- Profile-generated strings
- Gibbs sampling

## Repository Structure

```text
01_replication_origin_basics/
├── reverse_complement.py
├── thermotoga_dnaa_box_counter.py
├── todo_identify_step_1_4_07.py
├── Vibrio_cholerae.txt
├── vibrio_frequent_kmers.py
├── vibrio_ori_length.py
├── vibrio_pattern_count.py
└── vibrio_pattern_matching.py

02_gc_skew_origin_prediction/
├── approximate_pattern_count.py
├── approximate_pattern_matching.py
├── circular_genome_symbol_array.py
├── gc_skew_array.py
├── gc_skew_walk_example.py
├── hamming_distance.py
├── minimum_gc_skew_positions.py
└── optimized_symbol_array.py

03_greedy_motif_search/
├── greedy_motif_search.py
├── greedy_motif_search_dosr.py
├── kmer_profile_probability.py
├── motif_consensus.py
├── motif_count_matrix.py
├── motif_profile_matrix.py
├── motif_score.py
└── profile_most_probable_kmer.py

04_stochastic_motif_search/
├── count_with_pseudocounts.py
├── profile_with_pseudocounts.py
├── greedy_motif_search_with_pseudocounts.py
├── greedy_motif_search_dosr_with_pseudocounts.py
├── profile_most_probable_motifs.py
├── random_motifs.py
├── randomized_motif_search.py
├── normalize_probabilities.py
├── weighted_die.py
├── profile_generated_string.py
└── gibbs_sampler.py
```

## Technologies Used

- Python
- Visual Studio Code
- Git
- GitHub

## Notes

The implementations in this repository were written as part of my learning process. Some files contain experimental code, comments, and intermediate approaches used to understand the algorithms step by step.
