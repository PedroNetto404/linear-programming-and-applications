import simplex_algorithm as simplex_algorithm
import input_reader as ir

inputs = ir.read_input()

for problem_name, A, b, c, base in inputs:
   try: 
      print(f"\nProblem: {problem_name}")
            
      solution, status, used_base = simplex_algorithm.solve(A, b, c, base)
      
      if status == "unbounded":
         print("Ops... The problem is unbounded.")
         continue; 
      
      simplex_algorithm.print_solution(solution, c, used_base)
   except Exception as e:
      print(f"An error occurred while solving the problem: {e}.")
      continue