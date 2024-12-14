#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def line():
    """
    Plots the graph of y = x^3 for x in the range from 0 to 10.
    The plot will be a solid red line with the x-axis labeled from 0 to 10.
    """
    # Generate the data
    x = np.arange(0, 11)
    y = x ** 3

    # Create a figure with specific size
    plt.figure(figsize=(6.4, 4.8))

    # Plot y = x^3 as a solid red line
    plt.plot(x, y, 'r-', label='y = x^3')

    # Set the x-axis limits from 0 to 10
    plt.xlim(0, 10)

    # Label the x-axis and y-axis
    plt.xlabel("x-axis")
    plt.ylabel("y-axis")

    # Set the title of the graph
    plt.title("Plot of y = x^3")

    # Display the plot
    plt.show()


# Call the function to display the plot
line()
