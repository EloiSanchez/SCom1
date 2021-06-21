# Complex Systems Project

This code was made for the subject **Complex Systems** of the **Computational Modelling** master in 2021.

## What does it do
This code simulates the evolution of different communities of populations with different addaptability to an environmental cycle. The equations and models used where taken from *[Hiroaki Daido, J Theor Biol (2002) __217__ 425-442](https://doi.org/10.1006/jtbi.2002.3050)*.

## Aims
1. Numerically reproduce the behaviour found analytically in **Section 3** of the article regarding the dynamics of two species.
2. Reproduce **Fig. 1** of the article showing the stable points of the dynamics of three species.
3. Provide the possibility of performing a general simulation with any number of species of random phases and frequencies.

## Usage
### Two species
Modify the `input.py` ensuring that `N=2` and the `deltas` variable has length two. Execute `python3 two_species.py`. The results will be saved in the `results_dir` given in input.

### Three species
Modify the `input.py` ensuring that `N=3` and the `deltas` variable has length three. Execute `python3 three_species.py`. The results will be saved in the `results_dir` given in `input.py`.

### General
Modify the `input.py` at will. Note that the `deltas` variable will be ignored and overwritten by random values between 0 and 2pi. Execute `python3 general.py`. The results will be saved in the `results_dir` given in `input.py`.