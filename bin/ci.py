#!/usr/bin/env python
from data_morph.shapes.factory import ShapeFactory
from data_morph.data.loader import DataLoader
import sys

new_files = sys.argv[1:]

args = []

for dataset, filename in DataLoader._DATASETS.items():
    for new_file in new_files:
        if filename in new_file:
            args.append(dataset)

print(" ".join(args))
#print(ShapeFactory._SHAPE_MAPPING)
