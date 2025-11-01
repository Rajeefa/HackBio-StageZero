#####To print the names, slack username, country, 1 hobby, affiliations of people on your team and the DNA sequence of the genes they love most #####
  ###Create dictionary to assign each team member with the details of slack username, country, hobby, affiliations of people on your team and the DNA sequence of the genes###
team_methionine = {
    "Rajeefa": {
        "slack_username": "Rajeefa",
        "country": "Qatar",
        "hobby": "Reading",
        "affiliation": "Sidra Medicine",
        "dna_sequence": """>BRCA1-001 ENSE00003497952 exon:protein_coding
AGGGAACCCCTTACCTGGAATCTGGAATCAGCCTCTTCTCTGATGACCCTGAATCTGATC
CTTCTGAAGACAGAGCCCCAGAGTCAGCTCGTGTTGGCAACATACCATCTTCAACCTCTG
CATTGAAAGTTCCCCAATTGAAAGTTGCAGAATCTGCCCAGAGTCCAGCTGCTGCTCATA
CTACTGATACTGCTGGGTATAATGCAATGGAAGAAAGTGTGAGCAGGGAGAAGCCAGAAT
TGACAGCTTCAACAGAAAGGGTCAACAAAAGAATGTCCATGGTGGTGTCTGGCCTGACCC
CAGAAGAATTT
"""
    },
    "Oyedele Temitayo Victoria": {
        "slack_username": "Temitayo",
        "country": "Nigeria",
        "hobby": "Poetry reading",
        "affiliation": "O.A.U.",
        "dna_sequence": """>Homo sapiens DNA topoisomerase II alpha (TOP2A), mRNA (1 - 181bp)
AACCGACGCG CGTCTGTGGA GAAGCGGCTT GGTCGGGGGT GGTCTCGTGG GGTCCTGCCT
GTTTAGTCGC TTTCAGGGTT CTTGAGCCCC TTCACGACCG TCACCATGGA AGTGTCACCA
TTGCAGCCTG TAAATGAAAA TATGCAAGTC AACAAAATAA AGAAAAATGA AGATGCTAAG
AAAAGACTGT CTGTTGAAAG AATCTATCAA AAGAAAACAC AATTGGAACA TATTTTGCTC
"""
    },
    "Oluwadamilola Adeyemi": {
        "slack_username": "Oluwadamilola Adeyemi",
        "country": "Nigeria",
        "hobby": "Watching movies",
        "affiliation": "Mountain Top University",
        "dna_sequence": """>E.coli LacZ gene
CGGCTCGTATGTTGTGTGGAATTGTGAGCGGATAACAATTTCACACAGGAAACAG
"""
    },
}

for name, info in team_methionine.items():
    print(f"Name: {name}")
    print(f"Slack Username: {info['slack_username']}")
    print(f"Country: {info['country']}")
    print(f"Hobby: {info['hobby']}")
    print(f"Affiliation: {info['affiliation']}")
    print(f"DNA Sequence: {info['dna_sequence']}")
    print("-" * 20) # Separator for readability