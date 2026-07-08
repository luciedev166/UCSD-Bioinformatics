def main():
    text = "AAGTTC"
    profile = {
        'A':[0.4,  0.3,  0.0,  0.1,  0.0,  0.9,],
        'C':[0.2,  0.3,  0.0,  0.4,  0.0,  0.1,],
        'G':[0.1,  0.3,  1.0,  0.1,  0.5,  0.0,],
        'T':[0.3,  0.1,  0.0,  0.4,  0.5,  0.0,],
    }

    print(Pr(text, profile))
def Pr(Text, Profile):
    score = Profile[Text[0]][0]

    for i in range(1, len(Text)):
        score *= Profile[Text[i]][i]
    
    return score
main()