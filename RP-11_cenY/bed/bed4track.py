from sys import argv
from tsv import read_tsv, print_tsv


out_bed = []
for line in read_tsv(argv[1]):
    if line[0] == 'track':
        continue
    score = str(int(round(float(line[4])/10, 0))) #/10 for horhap
    name = line[3]
    if len(name) > 254:
        name = 'too_long'
    out_bed.append(line[:3] + [name, score] + line[5:])
print_tsv(out_bed)

