import random

def main():
    k = 8
    t = 5

    dna = [
        "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA",
        "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG",
        "TAGTACCGAGACCGAAAGAAGTATACAGGCGT",
        "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC",
        "AATCCACCAGCTCCACGTGCAATGTTGGCCTA",
    ]
    print(RandomizedMotifSearch(dna, k, t))

def RandomizedMotifSearch(Dna, k, t):
    M = RandomMotifs(Dna, k, t)
    BestMotifs = M

    while True:
        Profile = ProfileWithPseudocounts(M)
        M = Motifs(Profile, Dna) # M is replaced with most probable kmers
        if Score(M) < Score(BestMotifs):
            BestMotifs = M
        else:
            return BestMotifs 


def RandomMotifs(Dna, k, t):
    
    set_motifs = []
    for row in Dna:
        i = random.randint(0, len(row) - k)
        set_motifs.append(row[i:i + k])

    return set_motifs
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
def ProfileWithPseudocounts(Motifs):
    counts = CountWithPseudocounts(Motifs)
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {
        'A': [],
        'C': [],
        'G': [],
        'T': [],
    }

    for key in counts:
        for _ in range(k):
            profile[key].append(counts[key][_] / (t + 4))
    return profile

def Motifs(Profile, Dna):
    motifs = []
    k = len(Profile['A'])

    for row in Dna:
        motifs.append(ProfileMostProbableKmer(row, k, Profile))

    return motifs

def ProfileMostProbableKmer(text, k, profile):
    motifs = {}
    
    for i in range(len(text) - k + 1):
        motifs[text[i: i + k]] =(Pr(text[i:i + k], profile))
    

    return max(motifs, key=motifs.get) # = getting the motifs with the highest score
        

def Pr(Text, Profile):
    score = Profile[Text[0]][0] # gets first base score

    for i in range(1, len(Text)):
        score *= Profile[Text[i]][i]
    
    return score

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

def Score(motifs):
    consensus = Consensus(motifs)
    count = 0

    for row in motifs:
        for i in range(len(row)):
            if row[i] != consensus[i]:
                count+=1
    return count
main()