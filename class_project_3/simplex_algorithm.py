ZERO = 1e-4

import numpy as np

def solve(A, b, c, base):
    # Applying base to the matrix A
    B = np.matrix(A[:, base])

    # Basic solution. xB = B^-1 * b. This is a solution for the problem, but it may not be optimal
    xB = np.linalg.inv(B) * b

    # Relative cost. cT - cB * B^-1 * A. This is the cost of the non-basic variables
    # We want to find a non-basic variable that can enter the base and improve the solution
    s = c.T - (c[base].T * np.linalg.inv(B)) * A

    # If all relative costs are greater than or equal to zero, the solution is optimal
    min_s = s.min()
    if min_s >= -ZERO:
        return xB, "optimal", base
    
    # Choosing the variable that will enter the base
    p1 = s.argmin()

    # Here we will find the variable that will leave the base
    y = np.linalg.inv(B) * A[:, p1]
    r = xB / y
    r[r < 0] = np.inf

    # The min non-negative value of r is value that your index will leave the base
    r_min = r.min()
    r_min_index = r.argmin()

    # If r_min is infinity, the problem is unbounded
    if r_min == np.inf:
        return None, "unbounded", base

    # Updating the base
    base[r_min_index] = p1

    # Recursive call to the simplex algorithm
    return solve(A, b, c, base)

def print_solution(solution, c, used_base):
    array_from_matrix = lambda matrix: [x[0] for x in matrix.tolist()]
    
    c = array_from_matrix(c)
    solution = array_from_matrix(solution)
    
    print("Solution:")
    
    optimal_value = 0
    for i in range(len(c)):
        if i in used_base:
            print(f"x{i + 1} = {solution[used_base.index(i)]:.3f};")    
        
            optimal_value += c[i] * solution[used_base.index(i)]
        else:
            print(f"x{i + 1} = 0.000;")

    print(f"Optimal value: {optimal_value:.3f}")
    