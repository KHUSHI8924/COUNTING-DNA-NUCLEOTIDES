i=input(str("Enter the nucleotide of DNA for counting:"))
a=i.upper()
for sequence in a:
    a_count=0
    c_count=0
    g_count=0
    t_count=0
    for base in a:
        if base=='A':
            a_count+=1
        elif base=="C":
            c_count+=1
        elif base=="G":
            g_count+=1
        elif base=='T':
            t_count+=1
print(str(a_count) + ' ' + str(c_count) + ' ' + str(g_count) + ' ' + str(t_count))
        