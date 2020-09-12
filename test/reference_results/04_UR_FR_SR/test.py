"""
File to create the results with Superflex
"""

import sys
# Add the path where the Superflex module is
sys.path.append('/home/dalmo/Documents/BitBucket/superflexPython/C_so/')
from superflex import Superflex_C
import numpy as np
from os import chdir
chdir('/home/dalmo/Documents/BitBucket/superflexpy_aug2019/test/superflex_results/04_UR_FR_SR/')

# Initialize the class
sup = Superflex_C()

# Load the model
dims = sup.load_model()

# Initialize the parameters
parameters = np.array([[]])

# Get the output
output = sup.run_model(parameters)

np.savetxt('Results.csv', X = output, delimiter = ',', header = 'Q_out, E_UR, S_UR, S_FR, S_SR')