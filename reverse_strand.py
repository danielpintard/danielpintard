seq = "CCATGAATCCCTGTGACAACGCGGAACCCATTTTAAGCGTCAGCTCGACACTCCAGAATTTGCACACACGCGAGATTGTGCAATGAAATGGAACACGACAGTTCCGGCTACAATTCAGTTAGGACCGAAAGAGTGCGTGCGTACCCACGGGTTTGCGCGCATTAGCGTCTTTCTGCTCCACCGCCCCGCATGCAGAGACCTGAAGAGCTTGTCAAACCCGTCGAGACTTACAAATTTACGTTGCCAATATTCTAAAATTGGAGTGGCGAAGATATTAACCCTCCTTCGGTCGCTCATGATGTCGCGGACATTACGGCGTTTAAGAACTGCACGCTCAGCTAGGGGACCTCCACAGCATTACCACGGGGAGCTTAGGTCACACTCTTCAAATTGACGCGCCCGGTGTTGGGTGCGTACGATCGACGATAAGATTCCCTTTGGGTGTCGGTATCGTTGGTGGAGTATCGGGGAGACACCCATTAGCTCTTGCAGTGAAACCGAATTCTTCGTAGAAGATATCTCCGTCTCAGGGGTTAAATTCGAAGCACCGATTAAAGGTGGGGTCATCCCTTAACAGTTAGCTGTTCATCGTCATGGCACGCGTTACAACTGACCTTTGTCCCAGCCGAATACTAGTGGAAACACATTCATCTTGTAATAGCTTTGAGTTATAGGAGCCATAGTAGGCCTTACACCCTAGTCGGATGCTCAAGTTCAGTACGTAAGACTAGTTCTTATACTGGGCCGATGCTGATTTCTCGGACCAAGGATTGAGTGGGAGTTCTAAAGTCAGCCGTAGGACATCTAAGCATGCTCATTAAG"
mod_strn = seq[::-1] 
sec_strn = mod_strn.replace('A', 't').replace('T', 'a').replace('G', 'c').replace('C', 'g').upper()

print(sec_strn)

#expected result is ACCGGGTTTT


