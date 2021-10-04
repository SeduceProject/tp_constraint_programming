from ortools.sat.python import cp_model
from s_printer_correction import VarArraySolutionPrinterWithLimit


vmCosts = [ 10, 3, 5, 1, 9 ]
nbVm = len(vmCosts)
nbRunning = 2
# Constraint programming model
model = cp_model.CpModel()
# CP Variables
x = [ model.NewIntVar(0, 1, 'vm%i' % i) for i in range(nbVm) ]
# Constraints
model.Add(sum(x) == nbRunning)
# Solve the problem
solver = cp_model.CpSolver()
# Display solutions
solution_printer = VarArraySolutionPrinterWithLimit(x, 5, vmCosts)
status = solver.SearchForAllSolutions(model, solution_printer)
# Compute the cost
last_result = solution_printer.last_solution()
cost = 0
for i in range(nbVm):
    if last_result[i] == 1:
        cost += vmCosts[i]
print("cost: %d" % cost)
