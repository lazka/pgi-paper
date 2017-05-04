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

nojit, jit = list(fileinput.input())
nojit = map(float, nojit.split())
jit = map(float, jit.split())
lim = max(max(nojit), max(jit)) * 1.05

nojit_avg = float(sum(nojit)) / len(nojit)
bx_values = range(len(nojit))
px_values = [v + 0.5 for v in bx_values]

fig = plt.figure()

ax = plt.subplot(2, 1, 1)
ax.bar(bx_values, nojit, width=1)
f = ax.plot(px_values, [nojit_avg] * len(nojit), 'k-')

plt.legend(["Average Runtime"], fontsize="small")


ax.set_ylabel('Runtime [s]')
ax.set_xlabel('Iterations')
plt.ylim((0, lim))
plt.grid(True)
plt.title('PyPy without JIT')

avg = []
sum_ = 0
slower = []
for i, v in enumerate(jit):
    sum_ += v
    current_avg = float(sum_) / (i + 1)
    avg.append(current_avg)
    if current_avg > nojit_avg:
        slower.append(i)

ax = plt.subplot(2, 1, 2)
for i in slower:
    ax.axvspan(i, i + 1.0, color='red', linewidth=0, alpha=0.25)
ax.bar(bx_values, jit, width=1)
ax.set_ylabel('Runtime [s]')
ax.set_xlabel('Iterations')
ax.plot(px_values, avg, 'k-')

plt.legend([
    "Cumulative Moving Average Runtime",
    "Higher Average than without JIT"],
    fontsize="small")

plt.subplots_adjust(hspace=0.5)
plt.ylim((0, lim))
plt.grid(True)
plt.title('PyPy with JIT')

plt.savefig("jit_warmup.png")
