import gurobipy as gp
import data_provider as dp

class Solution: 
    def __init__(self, data) -> None:
        self.model = gp.Model()
        self.data = dp.read_file_data()
        self._def_variables()
        self._set_objective()
        self._set_constraints()
        
    def _def_variables(self):
        chosen_items = self.model.addVars(self.data.items_count, vtype=gp.GRB.BINARY)
        items_quantity = self.model.addVars(self.data.items_count, vtype=gp.GRB.INTEGER)
        
        self.variables = (chosen_items, items_quantity)
    
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
            (self.variables.chosen_items[i] + self.variables.chosen_items[j] <= 1 
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
    
    def print_solution(self):
        self.model.setParam('OutputFlag', 0)
        
        print(f'Valor ótimo: {self.model.objVal}')
        
        for i in range(self.data.items_count):
            if self.variables.chosen_items[i].x:
                print(f'Item {i}: {self.variables.items_quantity[i].x} unidades')
                
    def solve(self):
        self.model.optimize()
        self.print_solution()
        

solution = Solution()
solution.solve()

