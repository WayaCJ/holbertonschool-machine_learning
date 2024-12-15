#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def two():
    """exponential decay of C-14 and Ra-226 with the specified line styles."""

    # Define the x-values as years, spaced by 1000 years
    x = np.arange(0, 21000, 1000)

    # Define the decay rate for both C-14 and Ra-226
    r = np.log(0.5)

    # Half-lives for C-14 and Ra-226
    t1 = 5730
    t2 = 1600

    # Calculate the fraction remaining for C-14 and Ra-226
    y1 = np.exp((r / t1) * x)
    y2 = np.exp((r / t2) * x)

    # Create the figure with a specified size
    plt.figure(figsize=(6.4, 4.8))

    # Plot y1 (C-14) with a dashed red line
    plt.plot(x, y1, 'r--', label="C-14")

    # Plot y2 (Ra-226) with a solid green line
    plt.plot(x, y2, 'g-', label="Ra-226")

    # Label the x-axis
    plt.xlabel("Time (years)")

    # Label the y-axis
    plt.ylabel("Fraction Remaining")

    # Set the title of the plot
    plt.title("Exponential Decay of Radioactive Elements")

    # Set the x-axis range from 0 to 20,000
    plt.xlim(0, 20000)

    # Set the y-axis range from 0 to 1
    plt.ylim(0, 1)

    # Add a legend in the upper right corner
    plt.legend(loc="upper right")

    # Display the plot
    plt.show()
