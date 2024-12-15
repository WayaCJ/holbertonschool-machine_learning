#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

def bars():
    """Plots a stacked bar graph showing the number of fruit each person has."""
    
    # Set random seed for reproducibility
    np.random.seed(5)
    
    # Generate a 4x3 matrix representing the number of fruits (rows = fruit types, columns = people)
    fruit = np.random.randint(0, 20, (4, 3))
    
    # Fruit types and their respective colors
    fruit_types = ['Apples', 'Bananas', 'Oranges', 'Peaches']
    colors = ['red', 'yellow', '#ff8000', '#ffe5b4']  # colors corresponding to each fruit type
    
    # Create the figure and set the size
    plt.figure(figsize=(6.4, 4.8))
    
    # Plot the stacked bar graph
    plt.bar([0, 1, 2], fruit[0], label=fruit_types[0], color=colors[0], width=0.5)  # Apples
    plt.bar([0, 1, 2], fruit[1], label=fruit_types[1], color=colors[1], width=0.5, bottom=fruit[0])  # Bananas
    plt.bar([0, 1, 2], fruit[2], label=fruit_types[2], color=colors[2], width=0.5, bottom=fruit[0] + fruit[1])  # Oranges
    plt.bar([0, 1, 2], fruit[3], label=fruit_types[3], color=colors[3], width=0.5, bottom=fruit[0] + fruit[1] + fruit[2])  # Peaches
    
    # Add labels and title
    plt.xlabel("People", fontsize='x-small')
    plt.ylabel("Quantity of Fruit", fontsize='x-small')
    plt.title("Number of Fruit per Person", fontsize='x-small')
    
    # Set y-axis range and ticks
    plt.ylim(0, 80)
    plt.yticks(np.arange(0, 81, 10), fontsize='x-small')
    
    # Add a legend to show which fruit corresponds to which color
    plt.legend(fruit_types, loc="upper left", fontsize='x-small')
    
    # Display the plot
    plt.show()
