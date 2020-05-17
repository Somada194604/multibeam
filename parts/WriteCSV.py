import csv
import itertools
import numpy as np

fname = "Multibeam_list.csv"

with open(fname, "w") as f:
    writer = csv.writer(f)
    writer.writerow(["num_beam", "same freq.", "x", "y"])

with open(fname, "a") as f:
    writer = csv.writer(f)
    for m in Multibeam_list:
        writer.writerow(m)