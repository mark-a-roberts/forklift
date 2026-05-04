# Advent of Code - Forklift example

## Introduction

This program is a Python solution to the [Advent of Code: 2025 day 4][2] problem

Given a stacks of paper on a grid, identify how many can be removed.

A roll can be removed if it has less than 4 neighbours.

The program outputs the modified grid with 'x' denoting removed rolls 
and the number of rolls removed.

The program is similar to [John Conway's "Game of Life"][1] 
where cells lived, died or were born depending on the number of neighbours

### Run

    python3 forklift.py < (name of input file)

Data can optionally be entered from the keyboard

[1]: https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
[2]: https://adventofcode.com/2025/day/4
