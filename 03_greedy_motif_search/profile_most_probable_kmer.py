def main():
    text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
    profile = {
        'A':[0.2, 0.2, 0.3, 0.2, 0.3,],
        'C':[0.4, 0.3, 0.1, 0.5, 0.1,],
        'G':[0.3, 0.3, 0.5, 0.2, 0.4,],
        'T':[0.1, 0.2, 0.1, 0.1, 0.2,],
    }
    k = 5
    print(ProfileMostProbableKmer(text, k, profile))

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

main()