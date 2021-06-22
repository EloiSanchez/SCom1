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

## Results
### Three Bodies
The plot showing the results of the dynamics in the example directory **two_bodies** is:

![Broken link](https://github.com/EloiSanchez/SCom1/blob/main/two_species/plot.png) "Results of two species dynamics"

In this example, the two species should survive (as it can be seen) with a ratio between the two that tends to the analytical one.

### Two Bodies
The plot wich reproduces **Fig. 1** from the article is obtained in **three_bodies**.

![Broken link](https://github.com/EloiSanchez/SCom1/blob/main/three_species/populations.png) "Reproduction of Fig. 1 of the article"

### General
This code reproduces the results of **Section 7** of the paper, although the Figs. presented there are not the created by this code.

In our case, the dynamics of the conditions given in the input are returned in the plot.

**Example with `a=0.2`**

![Broken link](https://github.com/EloiSanchez/SCom1/blob/main/general_a_0.2/plot.png) "Dynamics of 7 species with `a=0.2`"


**Example with `a=0.8`**

![alt text](https://github.com/EloiSanchez/SCom1/blob/main/general_a_0.8/plot.png) "Dynamics of 7 species with `a=0.8`"

Note how different the results are when changing `a`. For more information check the paper of reference.

## Extra
Contact me _via_ eloisanchez16@gmail.com

Feel free to use this code.
