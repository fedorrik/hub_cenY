#!/bin/bash
track=`echo $1 | awk '{split($0, name, "."); print name[1]}'`
python bed4track.py $track.bed > bed4track.bed

/home/fedor/Programs/my/fastools/fastools seqlen ../rp11.cenY.fa > chrom.sizes
~/Programs/bedToBigBed bed4track.bed chrom.sizes $track.bb
rm chrom.sizes
rm bed4track.bed
