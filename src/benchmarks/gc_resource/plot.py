#!/usr/bin/python
# Copyright 2016 Christoph Reiter
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.

import fileinput

import matplotlib
matplotlib.use('cairo')
import matplotlib.pyplot as plt
import matplotlib.ticker as tkr

impls = {}

for line in list(fileinput.input()):
    line = line.strip()
    name, time_, rss = line.split()
    impls.setdefault(name, []).append((float(time_), int(rss)))

sub = plt.subplot()

for name, data in sorted(impls.items()):
    times = []
    rss = []
    for t, r in data:
        times.append(t)
        rss.append(r)
    line = sub.plot(times, rss, label=name)

l = plt.legend(bbox_to_anchor=(0.33, 0.98))
l.legendPatch.set_alpha(1)
plt.xlabel("Time [s]")
plt.ylabel("Rss [MiB]")

def func(x, pos):
    return "%d" % (x/1024**2)

y_format = tkr.FuncFormatter(func)

sub.yaxis.set_major_formatter(y_format)

plt.grid(True)
plt.title('Memory Usage Over Time (25 x 32 MiB allocations)')
plt.xlim(0, 3)

plt.savefig("gc_resource.svg")
