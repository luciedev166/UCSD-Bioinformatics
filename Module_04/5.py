def main():

    Profile = {
        'A': [0.8, 0.0, 0.0, 0.2,],
        'C': [0.0, 0.6, 0.2, 0.0,],
        'G': [0.2, 0.2, 0.8, 0.0,],
        'T': [0.0, 0.2, 0.0, 0.8,],
    }

    Dna = [
        "TTACCTTAAC",
        "GATGTCTGTC",
        "ACGGCGTTAG",
        "CCCTAACGAG",
        "CGTCAGAGGT",
    ]
    print(Motifs(Profile, Dna))

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
main()