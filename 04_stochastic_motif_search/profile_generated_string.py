import random
def main():
    Text = "AAACCCAAACCC"
    profile = {'A': [0.5, 0.1], 'C': [0.3, 0.2], 'G': [0.2, 0.4], 'T': [0.0, 0.3]}
    k = 2
    print(ProfileGeneratedString(Text, profile, k))
    
def ProfileGeneratedString(Text, profile, k):
    n = len(Text)
    probabilities = {}

    for i in range(0,n-k+1):
        probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)

    return WeightedDie(probabilities)

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
main()
