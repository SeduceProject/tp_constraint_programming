from ortools.sat.python import cp_model
from s_printer import VarArraySolutionPrinter


vmCosts = [ 10, 3, 5, 1, 9 ]
nbRunning = 2
# Constraint programming model
model = cp_model.CpModel()
# CP Variables
vm1 = model.NewIntVar(0, 1, 'vm1')
vm2 = model.NewIntVar(0, 1, 'vm2')
vm3 = model.NewIntVar(0, 1, 'vm3')
vm4 = model.NewIntVar(0, 1, 'vm4')
vm5 = model.NewIntVar(0, 1, 'vm5')
# Constraints
model.Add(vm1 + vm2 + vm3 + vm4 + vm5 == nbRunning)
# Solve the problem
solver = cp_model.CpSolver()
status = solver.Solve(model)
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("vm1: %d" % solver.Value(vm1))
    print("vm2: %d" % solver.Value(vm2))
    print("vm3: %d" % solver.Value(vm3))
    print("vm4: %d" % solver.Value(vm4))
    print("vm5: %d" % solver.Value(vm5))
    cost = 0
    if solver.Value(vm1) == 1:
        cost += vmCosts[0]
    if solver.Value(vm2) == 1:
        cost += vmCosts[1]
    if solver.Value(vm3) == 1:
        cost += vmCosts[2]
    if solver.Value(vm4) == 1:
        cost += vmCosts[3]
    if solver.Value(vm5) == 1:
        cost += vmCosts[4]
    print("cost: %d" % cost)

"""
# Display all solutions
solution_printer = VarArraySolutionPrinter([vm1, vm2, vm3, vm4, vm5])
status = solver.SearchForAllSolutions(model, solution_printer)
"""
