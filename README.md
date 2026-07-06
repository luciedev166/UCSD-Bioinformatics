# UCSD Bioinformatics Learning Repository

This repository documents my progress through the UCSD Bioinformatics for Beginners course.

It contains Python implementations of foundational bioinformatics algorithms, especially those related to DNA replication, pattern matching, k-mer analysis, GC skew, origin of replication prediction, and greedy motif search.

## Topics Covered

- DNA replication and origin of replication
- Pattern counting and pattern matching
- Frequent k-mer detection
- Reverse complements
- Symbol arrays for circular genomes
- GC skew analysis
- Minimum skew positions
- Hamming distance
- Approximate pattern matching
- Motif count matrices
- Profile matrices
- Consensus strings
- Motif scoring
- Profile-based k-mer probability
- Profile-most probable k-mers
- Greedy motif search

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
├── motif_count_matrix.py
├── motif_profile_matrix.py
├── motif_consensus.py
├── motif_score.py
├── kmer_profile_probability.py
├── profile_most_probable_kmer.py
└── greedy_motif_search.py
