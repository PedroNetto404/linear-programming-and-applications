import json
import numpy as np
import os


def read_input():
    try:
        file_path = os.path.join(os.path.dirname(__file__), "inputs.json")

        with open(file_path) as f:
            inputs = json.load(f)

            def mapInput(input):
                problem_name = input["problemName"]
                A = input["MatrixOfConstraintCoefficients"]
                b = input["RightHandSide"]
                c = input["ObjectiveFunctionCoefficients"]
                base = input["StartingBase"]
                
                return problem_name, np.matrix(A), np.matrix(b), np.matrix(c), base
            
            return list(map(mapInput, inputs))
            
    except FileNotFoundError:
        print("The file input.json was not found.")
        print("Please, make sure that the file exists in the current directory.")
        exit(1)
