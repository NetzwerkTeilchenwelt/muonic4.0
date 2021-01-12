
#! /usr/bin/env python3
# converter script to generate xy points in log scale
# to fit with external software
#
# reads in muonic "L" file
#

import sys

import numpy as n


def convert():
    # set this to desired binning
    BINS = n.linspace(0, 10, 11)  # 11 bins from 0-> 10

    infile = sys.argv[1]
    outfile = infile + "_xy_to_fit"

    vals = []

    with open(infile) as f:
        for line in f.readlines():
            vals.append(float(line.split()[2]))

    print(vals)

    bincontent, __ = n.histogram(vals, bins=BINS)
    # bincontent = n.log(bincontent)
    bincenters = .5 * (BINS[1:] + BINS[:-1])

    with open(outfile, "w") as f:
        for item in zip(bincenters[:-1], bincontent):
            f.write(str(item[0]) + "\t" + str(item[1]) + "\n")

    print("Histogram xy points written to %s" % outfile)


if __name__ == "__main__":
    convert()
