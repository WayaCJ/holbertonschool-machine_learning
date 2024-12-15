#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def change_scale():
    """Plots the exponential decay of C-14 with logarithmic scale for y-axis."""
    
    # Define the x-values as years, spaced by 5730 years
    x = np.arange(0, 28651, 5730)
    
    # Define the decay rate for C-14
    r = np.log(0.5)
    
    # Define the half-life of C-14
    t = 5730
    
    # Calculate the fraction remaining using the exponential decay formula
    y = np.exp((r / t) * x)
    
    # Create the figure with a specified size
    plt.figure(figsize=(6.4, 4.8))
    
    # Plot the data
    plt.plot(x, y)
    
    # Label the x-axis
    plt.xlabel("Time (years)")
    
    # Label the y-axis
    plt.ylabel("Fraction Remaining")
    
    # Set the title of the plot
    plt.title("Exponential Decay of C-14")
    
    # Set the y-axis to be logarithmic
    plt.yscale('log')
    
    # Display the plot
    plt.show()
