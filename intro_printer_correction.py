from ortools.sat.python import cp_model
from s_printer import VarArraySolutionPrinter

model = cp_model.CpModel()
# Variables
x = model.NewIntVar(0, 1, 'x')
y = model.NewIntVar(0, 2, 'y')
z = model.NewIntVar(0, 3, 'z')
# Constraints
model.Add(x != y)
model.Add(x < z)
# Solve the problem
solver = cp_model.CpSolver()
solution_printer = VarArraySolutionPrinter([x, y, z])
status = solver.SearchForAllSolutions(model, solution_printer)
if status != cp_model.OPTIMAL and status != cp_model.FEASIBLE:
    print("No solution")
