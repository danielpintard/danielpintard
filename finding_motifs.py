s = 'CGAGTCACCGAGTCAGCGAGTCACGAGTCAACCCGAGTCACATCTCGAGTCAATCCGGGCGAGTCATTGCGAGTCAGGTGATGCGAGTCACGTCGAGTCACGAGTCACGAGTCACGAGTCAAGCTCACGAGTCAGCGAGTCACGAGTCACGAGTCATCGAGTCAAGCGAGTCAAGTGCGAGTCACGCCGAGTCACGAGTCACGAGTCATCGAGTCACGAGTCAATGCGAGTCATTGGCGAGTCACGAGTCACGAGTCACGTGACCAACGAGTCACAGCGAGTCACGAGTCACGAGTCAGCGAGTCACGAGTCACGAGTCACGAGTCAGTCGCACGAGTCACTAATCGAGTCACGAGTCAGCGAGTCACGAGTCATCGGTCCGCGAGTCACCCCGAGTCAGAACGAGTCAACGAGTCACTCGAGTCAGCACGAGTCAGGGCGAGTCACGAGTCAGTCCGAGTCATCCTCGAGTCATCCGAGTCATTATACTCGAGTCATCGAGTCAATCCGAGTCATCGAGTCAGGTAGGCGAGTCAGGGGACTCGAGTCATTGGGTCGAGTCATCGAGTCACCTTTAGTTCGAGTCACGAGTCACCGAGTCAGGGTCCACCGAGTCAGGAGGAAGCGAGTCACGAGTCATTCGAGTCAAGCGAGTCACCAAGCTCACCGGCCGAGTCAATCGAGTCAACGGACGAGTCACGGCCGAGTCACGAGTCACGAGTCACCCGAGTCAACCGAGTCACGAGTCATTCATGTCGAGTCACACCGAGTCACGAGTCACGAGTCAGCGACGAGTCATCAGTCGAGTCAGTCTTGGGCGAGTCATATTTTGGCGAGTCACGAGTCACTCGAGTCAGCCGACGAGTCACCGAGTCAGTCGAGTCACGAGTCA'
t = 'CGAGTCACG'

def motif_search(s, t):
    for i in range(len(s)):
        if s[i:i+len(t)] == t:
            i +=1
            print(i)

print(motif_search(s, t))