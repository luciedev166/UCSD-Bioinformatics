def main():
    p = "CTTGAAGTGGACCTCTAGTTCCTCTACAAAGAACAGGTTGACCTGTCGCGAAG"
    q = "ATGCCTTACCTAGATGCAATGACGGACGTATTCCTTTTGCCTCAACGGCTCCT"
# Input:  Two strings p and q
# Output: An integer value representing the Hamming Distance between p and q.
    print(HammingDistance(p, q))
def HammingDistance(p, q):
    count = 0
    
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    
    return count

main()