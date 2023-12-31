#!/usr/bin/env python3

import time

from numpy import add, copyto, multiply, zeros

from roll_add import roll_add

try:
    profile
except NameError:
    profile = lambda x: x

grid_shape = (640, 640)

def laplacian(grid, out):
    copyto(out, grid)
    multiply(out, -4.0, out)
    roll_add(grid, +1, 0, out)
    roll_add(grid, -1, 0, out)
    roll_add(grid, +1, 1, out)
    roll_add(grid, -1, 1, out)


@profile
def evolve(grid, dt, out, D=1):
    laplacian(grid, out)
    multiply(out, D * dt, out)
    add(out, grid, out)


def run_experiment(num_iterations):
    scratch = zeros(grid_shape)
    grid = zeros(grid_shape)

    block_low = int(grid_shape[0] * 0.4)
    block_high = int(grid_shape[0] * 0.5)
    grid[block_low:block_high, block_low:block_high] = 0.005

    start = time.time()
    for i in range(num_iterations):
        evolve(grid, 0.1, scratch)
        grid, scratch = scratch, grid
    return time.time() - start


if __name__ == "__main__":
    run_experiment(500)