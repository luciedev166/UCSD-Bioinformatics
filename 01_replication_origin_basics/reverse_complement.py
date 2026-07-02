# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):   
    return Complement(Reverse(Pattern))

# Copy your Reverse() function here.
def Reverse(Pattern):
    return Pattern[::-1]

# Copy your Complement() function here.
def Complement(Pattern):
    comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    string = ""
    for p in Pattern:
        string += comp[p]
    return string