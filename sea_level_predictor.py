import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df= pd.read_csv("epa-sea-level.csv")
    future = range(1880, 2051, 1)
    new_future= range(2000, 2051, 1)
    # Create scatter plot
    fig, ax =plt.subplots(figsize=(20, 5))
    plt.scatter(x=df["Year"], y=df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    slope = linregress(df["Year"], df["CSIRO Adjusted Sea Level"]).slope
    intercept = linregress(df["Year"], df["CSIRO Adjusted Sea Level"]).intercept
    plt.plot(future, slope*future+intercept, linestyle= "dashed")
    # Create second line of best fit
    new_slope=linregress(df[df["Year"]>=2000]["Year"], df[df["Year"]>=2000]["CSIRO Adjusted Sea Level"]).slope
    new_intercept = linregress(df[df["Year"]>=2000]["Year"], df[df["Year"]>=2000]["CSIRO Adjusted Sea Level"]).intercept
    plt.plot(new_future, new_slope*new_future+new_intercept, linestyle= "dashed")
    # Add labels and title
    ax.set_title("Rise in Sea Level")
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()