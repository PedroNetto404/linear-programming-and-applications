import simplex_algorithm as simplex_algorithm
import input_reader as ir

inputs = ir.read_input()

for problem_name, A, b, c, base in inputs:
    print(f"\nProblem: {problem_name}")
           
    solution, status, used_base = simplex_algorithm.solve(A, b, c, base)
    
    if status == "unbounded":
       print(f"Ops... The problem {input.name} is unbounded")
       exit()
    
    simplex_algorithm.print_solution(solution, c, used_base)
    print("\n")