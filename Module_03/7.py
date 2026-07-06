def main():
    k = 3
    t = 5

    dna = [
        "GGCGTTCAGGCA",
        "AAGAATCAGTCA",
        "CAAGGAGTTCGC",
        "CACGTCAATCAC",
        "CAATAATATTCG",
    ]
    print(GreedyMotifSearch(dna, k, t))


def GreedyMotifSearch(dna, k, t):
    # temporary champion: first k-mer from each DNA string
    best_motifs = []
    for row in dna:
        best_motifs.append(row[:k])

    # try every k-mer from the FIRST dna string as a seed
    for i in range(len(dna[0]) - k + 1):
        motifs = [dna[0][i:i+k]]   # fresh attempt

        # build this attempt using the remaining DNA strings
        for j in range(1, t):
            profile = Profile(motifs)
            next_motif = ProfileMostProbableKmer(dna[j], k, profile)
            motifs.append(next_motif)

        # only compare once motifs is complete
        if Score(motifs) < Score(best_motifs):
            best_motifs = motifs

    return best_motifs

def Score(motifs):
    consensus = Consensus(motifs)
    count = 0

    for row in motifs:
        for i in range(len(row)):
            if row[i] != consensus[i]:
                count+=1
    return count

def Count(motifs):
    
    count = {'A': [], 'C': [],'G': [],'T': []}

    for row in zip(*motifs):
        count['A'].append(row.count('A'))
        count['C'].append(row.count('C'))
        count['G'].append(row.count('G'))
        count['T'].append(row.count('T'))

    return count

def Consensus(motifs):
    consensus = ""

    counts = Count(motifs)
    
    for i in range(len(motifs[0])):
        column_counts = {
        'A': counts['A'][i],
        'C': counts['C'][i],
        'G': counts['G'][i],
        'T': counts['T'][i]
        }
        consensus += max(column_counts, key=column_counts.get)
    return consensus

def ProfileMostProbableKmer(text, k, profile):
    motifs = {}
    
    for i in range(len(text) - k + 1):
        motifs[text[i: i + k]] =(Pr(text[i:i + k], profile))
    
    return max(motifs, key=motifs.get)
        

def Pr(Text, Profile):
    score = Profile[Text[0]][0]

    for i in range(1, len(Text)):
        score *= Profile[Text[i]][i]
    
    return score

def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])

    profile = {'A': [], 'C': [], 'G':[], 'T': []}
    base_count_per_col = Count(Motifs)

    for base in base_count_per_col:
        for i in range(k):
            profile[base].append(base_count_per_col[base][i] / t)

    return profile


main()