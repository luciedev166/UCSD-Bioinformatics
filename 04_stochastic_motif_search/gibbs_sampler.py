import random
def main():
    Dna = [
        "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
        "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
        "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
        "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
        "AATCCACCAGCTCCACGTGCAATGTTGGCCTA",
    ]

    N = 100
    k = 8
    t = 5
    print(GibbsSampler(Dna, k, t, N))
def GibbsSampler(Dna, k, t, N):
    BestMotifs = []

    # Fill with random starting motifs
    for row in range(t):
        i = random.randint(0, len(Dna[row]) - k)
        BestMotifs.append(Dna[row][i:i + k])

    Motifs = BestMotifs.copy()  # current working motifs

    for _ in range(N):
        i = random.randint(0, t - 1)

        # Build profile without row i
        motifs_without_i = []
        for row in range(t):
            if row != i:
                motifs_without_i.append(Motifs[row])

        profile = Profile(motifs_without_i)

        # Always replace the current motif
        Motifs[i] = ProfileGeneratedString(Dna[i], profile, k)

        # Only save it as the best if its score improved
        if Score(Motifs) < Score(BestMotifs):
            BestMotifs = Motifs.copy()

    return BestMotifs

def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}

    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)

    return WeightedDie(probabilities)



def Count(motifs):
    
    count = {'A': [], 'C': [],'G': [],'T': []}

    for row in zip(*motifs):
        count['A'].append(row.count('A') + 1)
        count['C'].append(row.count('C') + 1)
        count['G'].append(row.count('G') + 1)
        count['T'].append(row.count('T') + 1)

    return count
def Profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])

    profile = {'A': [], 'C': [], 'G':[], 'T': []}
    base_count_per_col = Count(Motifs)

    for base in base_count_per_col:
        for i in range(k):
            profile[base].append(base_count_per_col[base][i] / (t + 4))

    return profile

def Normalize(Probabilities):
    total = sum(Probabilities.values())
    for key in Probabilities:
        Probabilities[key] = Probabilities[key] / total

    return Probabilities

def WeightedDie(Probabilities):
    Probabilities = Normalize(Probabilities)
    p = random.uniform(0, sum(Probabilities.values()))
    current = 0
    for key in Probabilities:
        current += Probabilities[key]
        if p <= current:
            return key
    
def Pr(Text, Profile):
    score = Profile[Text[0]][0] # gets first base score

    for i in range(1, len(Text)):
        score *= Profile[Text[i]][i]
    
    return score

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

def Score(motifs):
    consensus = Consensus(motifs)
    count = 0

    for row in motifs:
        for i in range(len(row)):
            if row[i] != consensus[i]:
                count+=1
    return count
main()