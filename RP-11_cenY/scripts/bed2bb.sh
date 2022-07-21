#!/bin/bash
# fastools is my scripts for workong with fasta files https://github.com/fedorrik/fastools
~/Programs/my/fastools/fastools seqlen ../rp11.cenY.fa > chrom.sizes
for bed in ../bed/*.bed
do
  track=`echo $bed | awk '{split($0, name, "/"); print name[3]}' | awk '{split($0, name, "."); print name[1]}'`
  python bed4track.py ../bed/$track.bed > bed4track.bed
  bedToBigBed bed4track.bed chrom.sizes ../bb/$track.bb
  rm bed4track.bed
done
rm chrom.sizes
