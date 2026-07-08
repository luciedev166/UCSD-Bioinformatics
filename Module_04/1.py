def main():
    Motifs = [
        'AACGTA',
        'CCCGTT',
        'CACCTT',
        'GGATTA',
        'TTCCGG',
    ]
    print(CountWithPseudocounts(Motifs))

def CountWithPseudocounts(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])

    base = {
        'A': [],
        'C': [],
        'G': [],
        'T': [],
    }

    for row in zip(*Motifs):
        for _ in base:
            base[_].append(row.count(_) + 1) 

    return base
main()