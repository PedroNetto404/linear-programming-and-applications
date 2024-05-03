import json
import numpy as np

def read_input():
    with open("input.json") as f:
        data = json.load(f)
        
        return {
            # Matrix with the coefficients of the constraints like Ax <= b, where A is the matrix and b is the vector
            'MatrixOfConstraintCoefficients': np.matrix(data['MatrixOfConstraintCoefficients']),
            # Vector of constraints constants
            'RightHandSide': np.matrix(data['RightHandSide']),
            # Vector with the coefficients of the objective function
            'ObjectiveFunctionCoefficients': np.matrix(data['ObjectiveFunctionCoefficients']),
            # Base used to start the simplex algorithm. 
            # This vector contains the indexes of the columns of the base
            'StartingBase': np.matrix(data['StartingBase'])
        }
    
    