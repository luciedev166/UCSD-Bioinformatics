def main():
    print(Complement("AAAACCCGGT"))
def Complement(Pattern):
    comp = ""
    for n in Pattern:
        if n == "A":
            comp += "T"
        elif n == "T":
            comp += "A"
        elif n == "C":
            comp += "G"
        elif n == "G":
            comp += "C"
    return comp