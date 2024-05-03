import simplex_algorithm as simplex_algorithm
import input_reader as ir

A, b, c, base = ir.read_input()
solution, status, used_base = simplex_algorithm.solve(A, b, c, base)

if status == "unbounded":
    print("Ops... The problem is unbounded")
    exit()

simplex_algorithm.print_solution(solution, c, used_base)
