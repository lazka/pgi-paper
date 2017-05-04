#!/usr/bin/python
# Copyright 2013 Christoph Reiter
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

import numpy as np
import matplotlib
matplotlib.use('cairo')
import matplotlib.pyplot as plt
import fileinput


def generate_png(data, output_name, max_y=None, bbox_to_anchor=None):
    colors = [
        '#729fcf', '#3465a4', '#204a87',
        '#8ae234', '#73d216', '#4e9a06',
        '#ad7fa8', '#75507b', '#5c3566',
    ]

    cats = {}

    for line in filter(None, data.splitlines()):
        impl, api, name, dur, err = line.split()
        cat_key = impl + " " + name.split("_")[-1]
        cats.setdefault(cat_key, []).append((api, float(dur), float(err)))
    cats = sorted(cats.items())

    N = len(cats[0][1])
    ind = np.arange(N)
    width = 0.09
    offset = width

    fig = plt.figure()
    ax = fig.add_subplot(111)

    ax.grid(True, which='both')

    for i, (cat, values) in enumerate(cats):
        durs = [a[1] * 1000 for a in values]
        ax.bar(ind + i * width + offset, durs, width, color=colors[i])

    title = 'Called 1000 times, avg of 3000 (3000 warmup)'

    plt.ylim(ymax=max_y)
    ax.set_ylabel('Duration [ms]')
    ax.set_title(title)
    ax.set_xticks(ind + (width * N * 2) + offset)
    ax.set_xticklabels([a[0] for a in cats[0][1]])

    l = ax.legend([a[0] for a in cats], bbox_to_anchor=bbox_to_anchor)
    l.legendPatch.set_alpha(0.5)

    for i, (cat, values) in enumerate(cats):
        durs = [a[1] * 1000 for a in values]
        errs = [a[2] * 1000 for a in values]
        ax.errorbar(ind + i * width + offset, durs, yerr=errs,
                    fmt="o", color="0.2", marker="_")

    plt.savefig(output_name)


if __name__ == "__main__":
    data = "".join(list(fileinput.input()))
    generate_png(data, "ffi_bench.svg")
    generate_png(data, "ffi_bench_zoom.svg",
                 0.7, bbox_to_anchor=(0.85, 1.0))
