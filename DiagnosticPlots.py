"""
Christopher Greene & Chris Richardson
Elon University
Description: A generalized code for generating plots of line ratios based on
simulations from CLOUDY. These line ratios will act as a test of the validity of
our model of the Spectral Energy Distribution of Seyfert Galaxies."""

#Import required modules
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os, csv

#List all the subdirectories within directory that have the data that we want
def filefind(directory): 
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.lin'):
                print file
directory= '/Users/compastro/greene/AGN_SED'
filefind(directory)


#Generate a CSV file containing all the relevant data points
columns = []
with open('SEDT4.lin', 'r') as f:
    reader = csv.reader(f,delimiter="\t")
    ind = next(reader).index('iteration')
    for row in reader:
        columns.append(row[ind])

#Plot these data points