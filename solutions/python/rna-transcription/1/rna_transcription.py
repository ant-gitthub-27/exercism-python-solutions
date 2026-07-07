def to_rna(dna_strand):
    rna_strand = []
    for letter in dna_strand:
        if letter == "G":
            rna_strand.append("C")
        elif letter == "C":
            rna_strand.append("G")
        elif letter == "T":
            rna_strand.append("A")
        elif letter == "A":
            rna_strand.append("U")
    return "".join(rna_strand)