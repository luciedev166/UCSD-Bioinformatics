# Input:  A string Text and an integer k
def main():
    Text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
    k = 4
    words = FrequentWords(Text, k)
    
    for w in words:
        print(w)
# Output: A list containing all most frequent k-mers in Text
def FrequentWords(Text, k):
    words = []
    freq = FrequencyMap(Text, k)
    m = max(freq.values())
    
    for i in freq:
        if freq[i] == m and i not in words:
            words.append(i)
    return words

# Copy your FrequencyMap() function here.
def FrequencyMap(Text, k):
    freq = {}
    for i in range(len(Text) - k + 1):
        pattern = Text[i:i + k]
        if pattern in freq:
            freq[pattern] = freq[pattern] + 1
        else:
            freq[pattern] = 1
    return freq
        