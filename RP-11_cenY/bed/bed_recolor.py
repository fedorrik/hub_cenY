# Usage: python3 <file>.bed
# Script recuirse "bed_colors" tsv file in curren dir with format:
###############
# name1	r,g,b #
# name2 r,g,b #
###############
# name1 and name2 lines will bed recolored
# other lines will bed left as they are

import tsv
from sys import argv


input_bed = argv[1]

# read color data file and fill dict
color_dict = {}
with open('bed_colors') as f:
    for line in f:
        line = line.strip().split()
        color_dict[line[0]] = line[1]

# recolor bed
recolored_bed = []
for line in tsv.read_tsv(input_bed):
    name = line[3]
    if name in color_dict:
        recolored_bed.append(line[:8] + [color_dict[name]])
    else:
        recolored_bed.append(line)

tsv.print_tsv(recolored_bed)

