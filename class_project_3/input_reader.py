import json
import numpy as np
import os


def read_input():
    try:
        file_path = os.path.join(os.path.dirname(__file__), "inputs.json")

        with open(file_path) as f:
            inputs = json.load(f)

            return list(
                map(
                    lambda input: (
                        input["name"],
                        np.matrix(input["A"]),
                        np.matrix(input["b"]),
                        np.matrix(input["c"]),
                        input["base"],
                    ),
                    inputs,
                )
            )

    except FileNotFoundError:
        print("The file input.json was not found.")
        print("Please, make sure that the file exists in the current directory.")
        exit(1)
