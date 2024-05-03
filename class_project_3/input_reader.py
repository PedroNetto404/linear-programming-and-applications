import json
import numpy as np
import os

def read_input():
    try:
        file_path = os.path.join(os.path.dirname(__file__), "input.json")

        with open(file_path) as f:
            data = json.load(f)

            # Matrix with the coefficients of the constraints like Ax <= b, where A is the matrix and b is the vector
            A = data["MatrixOfConstraintCoefficients"]
            
            # Vector of constraints constants
            b = data["RightHandSide"]
            
            # Vector with the coefficients of the objective function
            c = data["ObjectiveFunctionCoefficients"]
            
            # This vector contains the indexes of the columns of the base
            base = data["StartingBase"]

            return np.matrix(A), np.matrix(b), np.matrix(c), base
    except FileNotFoundError:
        print("The file input.json was not found.")
        print("Please, make sure that the file exists in the current directory.")
        exit(1)
