import simplex_algorithm as sa
import input_reader as ir

data = ir.read_input()

solved_problem = sa.simplex(*data.values())

if(solved_problem['status'] == 'unbounded'):
    print('Ops... The problem is unbounded')
    exit()

used_base = solved_problem['used_base']
solution = solved_problem['solution']

optimal_value = 0
for i in range(len(data['ObjectiveFunctionCoefficients'][0])):
    if i in used_base:
        value = solution[used_base.index(i)]
        optimal_value = optimal_value + value * data['ObjectiveFunctionCoefficients'][0, i]
        print(f"x{i+1} = {value}")
    else:
        print(f"x{i+1} = 0")

print(f"Optimal value: {optimal_value}")