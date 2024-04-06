import gurobipy as gp
import data_provider as dp
from collections import namedtuple

class Solution: 
    def __init__(self) -> None:
        self.model = gp.Model()
        self.data = dp.read_file_data()
        self._def_variables()
        self._set_objective()
        self._set_constraints()
        
    def print_solution(self):
        self.model.setParam('OutputFlag', 0)
        
        print(f'Valor ótimo: {self.model.objVal}')
        
        for i in range(self.data.items_count):
            if self.variables.chosen_items[i].x:
                print(f'Item {i}: {self.variables.items_quantity[i].x} unidades')
                
    def solve(self):
        self.model.optimize()
        
    def _def_variables(self):
        chosen_items = self.model.addVars(self.data.items_count, vtype=gp.GRB.BINARY)
        items_quantity = self.model.addVars(self.data.items_count, vtype=gp.GRB.INTEGER)
        
        Variables = namedtuple('Variables', ['chosen_items', 'items_quantity'])
        
        self.variables = Variables(chosen_items, items_quantity) 
    
    def _set_objective(self):
        self.model.setObjective(
            sum(
                self.variables.chosen_items[i] * (self.variables.items_quantity[i] * self.data.items_values[i])
                for i in range(self.data.items_count)
            ), 
            sense=gp.GRB.MAXIMIZE
        )
    
    def _set_constraints(self):
        forbidden_pairs_constraint = self.model.addConstrs(
            (self.variables.chosen_items[i - 1] + self.variables.chosen_items[j - 1] <= 1 
             for i, j in self.data.forbidden_pairs)
        )
        
        max_weight_constraint = self.model.addConstr(
            sum(
                self.variables.chosen_items[i] * self.variables.items_quantity[i] * self.data.items_weights[i]
                for i in range(self.data.items_count)
            ) <= self.data.max_weight_supported
        )
        
        items_quantity_constraint = self.model.addConstrs(
            self.variables.items_quantity[i] <= self.data.items_available_quantity[i]
            for i in range(self.data.items_count)
        )
        
        return forbidden_pairs_constraint, max_weight_constraint, items_quantity_constraint
    
solution = Solution()
solution.solve()
solution.print_solution()
