#!/bin/bash
# Change copy_from to any path of a directory where there are images that you'd like to process for example.
copy_from="$HOME/samsung-SATA/datasets/clothing/purl.stanford.edu--tb980qz1002/ClothingAttributeDataset/images/"
n_wanted=15
copy_to="images/"
related="thumbnails/"
[ ! -z "`ls $copy_to`" ] && rm "$copy_to"*
[ ! -z "`ls $related`" ] && rm "$related"*
ls -d "$copy_from"*.jpg | shuf | head -$n_wanted | xargs cp -t "$copy_to"
