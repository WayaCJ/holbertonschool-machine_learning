#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def frequency():
    """Plots a histogram of student grades with specified labels and styling."""
    
    # Set random seed for reproducibility
    np.random.seed(5)
    
    # Generate 50 student grades from a normal distribution
    student_grades = np.random.normal(68, 15, 50)
    
    # Create the figure with a specified size
    plt.figure(figsize=(6.4, 4.8))
    
    # Plot the histogram with bins every 10 units, and black edges for the bars
    plt.hist(student_grades, bins=range(0, 101, 10), edgecolor='black')
    
    # Label the x-axis
    plt.xlabel("Grades")
    
    # Label the y-axis
    plt.ylabel("Number of Students")
    
    # Set the title of the plot
    plt.title("Project A")
    
    # Display the plot
    plt.show()
