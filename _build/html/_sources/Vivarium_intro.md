# Vivarium

## Vivarium is a software tool
Vivarium is an "interface protocol" for connecting separate models,
simulators, and data into a large, complex, and open-ended network
that anyone can contribute to.

## Vivarium allow you to modularize your modeling
![image](vivarium_short_slides/slide-2.png)

In Comp bio you will a single simulator for a single type of mechanism,
but you very quickly see what you can't do with your simulator.
By embracing modularity you can add new modules, plug them in, and 
run them.
Imagine a multiscale system, where you have simulations within
simulations within simulations. Each of these is uspported by some
computaions processes which you can  then plug in.

## Vivarium offers an intuitive, modular design
The basic elements on Vivarium are:
1. Processes
2. Stores

### Processes
* **Processes**: Consist of parameters, ports, and an update function

#### Minimal Process: Transcription
![image](vivarium_short_slides/slide-4.png)

### Stores
* **Stores**: Hold the state variables, map the variable names to their values,
and apply the updates

### Composites: Combining Modules
* **Composites**: Bundles of processes and stores, wired together by
their ports, and run together in time
![image](vivarium_short_slides/slide-3.png)

### Minimal Composite: Transcription + Translation
![image](vivarium_short_slides/slide-5.png)

## The Vivarium Engine Supports Multiple Timescales
![image](vivarium_short_slides/slide-6.png)

## "Steps" run between time-dependent processes
![image](vivarium_short_slides/slide-7.png)

## Modularity makes it easy to wire in different processes
![image](vivarium_short_slides/slide-8.png)

## Hierarchical embedding enables multiple scales
![image](vivarium_short_slides/slide-9.png)
![image](vivarium_short_slides/slide-10.png)

## Hierarchical Updates allow subgraphs to be added/removed/moved during simulation runtime
![image](vivarium_short_slides/slide-11.png)

### Hierarchical Update Example: Division
![image](vivarium_short_slides/slide-12.png)

## Tools
### vivarium-cobra: Dynamic Flux Balance Analysis
```bash
pip install vivarium-cobra
```
![image](vivarium_short_slides/slide-15-a.png)
![image](vivarium_short_slides/slide-15-b.png)

### vivarium-bioscrape: Chemical Reaction Networks
```bash
pip install vivarium-bioscrape
```
![image](vivarium_short_slides/slide-16-a.png)
![image](vivarium_short_slides/slide-16-b.png)

### vivarium-multibody: Solid Body Physics + Diffusion
```bash
pip install vivarium-multibody
```
![image](vivarium_short_slides/slide-17-a.png)
![image](vivarium_short_slides/slide-17-b.png)

### Wiring it all together
![image](vivarium_short_slides/slide-18.png)

### Simulation results blend properties of all the input simulators
![image](vivarium_short_slides/slide-19.png)

## Biosimulators
![image](vivarium_short_slides/slide-20.png)

## Vivarium-ecoli
![image](vivarium_short_slides/slide-21.png)
![image](vivarium_short_slides/slide-22.png)
### Mass fractions
![image](vivarium_short_slides/slide-23.png)

