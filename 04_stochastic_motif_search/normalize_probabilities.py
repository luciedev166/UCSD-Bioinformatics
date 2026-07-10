def main():
    Probabilities = {'A': 0.1, 'C': 0.1, 'G': 0.1, 'T': 0.1}
    print(Normalize(Probabilities))

def Normalize(Probabilities):
    total = sum(Probabilities.values())
    for key in Probabilities:
        Probabilities[key] = Probabilities[key] / total

    return Probabilities
main()