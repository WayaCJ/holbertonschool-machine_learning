#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt


def scatter():
    """Generates and plots a scatter plot of height vs weight."""

    # Define mean and covariance for the multivariate normal distribution
    mean = [69, 0]
    cov = [[15, 8], [8, 15]]

    # Set the random seed for reproducibility
    np.random.seed(5)

    # Generate 2000 samples from a multivariate normal distribution
    x, y = np.random.multivariate_normal(mean, cov, 2000).T

    # Adjust the y-values (weight)
    y += 180

    # Create a figure with a specified size
    plt.figure(figsize=(6.4, 4.8))

    # Scatter plot with magenta points
    plt.scatter(x, y, color='magenta')

    # Label the x-axis
    plt.xlabel("Height (in)")

    # Label the y-axis
    plt.ylabel("Weight (lbs)")

    # Set the title of the plot
    plt.title("Men's Height vs Weight")

    # Display the plot
    plt.show()
