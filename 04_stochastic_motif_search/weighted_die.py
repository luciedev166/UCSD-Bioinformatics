import random

def main():
    Probabilities = {'A': 0.25, 'C': 0.25, 'G': 0.25, 'T': 0.25}
    print(WeightedDie(Probabilities))

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
main()