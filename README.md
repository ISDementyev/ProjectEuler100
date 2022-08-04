# ProjectEuler100
My attempts at problems 1-100 from the Project Euler Archives (projecteuler.net) 

## Purpose
This repository contains my original and optimized code that I make in order to solve the Project Euler Problems 1-100 as an exercise in problem-solving and computational optimization. 

## Layout
Each directory in [problems/](https://github.com/ISDementyev/ProjectEuler100/tree/main/problems) corresponds to a problem. If the directory for a problem is available, it means I was successful in solving it.

Each directory contains at least one file - a python file which contains a function that solves the problem. Sometimes, an optimized version written by me 
will be available and distinguished clearly from the non-optimized functions within the same py file. Types of optimization include (but are not limited to) vectorizations with Numpy and just-in-time compilation.

## Package requirements
Numba and Numpy are required, the version numbers are up to the user's discretion and the versions' compatibilities. The math module (one of python's built-in modules) is also used for some problems.
