from ortools.sat.python import cp_model
from s_printer_correction import VarArraySolutionPrinterWithLimit


STATES = [ "off", "on" ]
vmCosts = [ 10, 3, 5, 1, 9 ]
nbVm = len(vmCosts)
nbRunning = 2
# Constraint programming model
model = cp_model.CpModel()

# CP Variables
x = [ model.NewIntVar(0, 1, 'vm%i' % i) for i in range(nbVm) ]

# Constraints
model.Add(sum(x) == nbRunning)
total_cost = []
for i in range(nbVm):
    total_cost.append(x[i] * vmCosts[i])
model.Maximize(sum(total_cost))
# Short way to write the same code
# model.Maximize(sum([x[i] * vmCosts[i] for i in range(nbVm)]))

# Solve the problem
solver = cp_model.CpSolver()

# Display solutions
status = solver.Solve(model)

# Compute the cost
if status == cp_model.OPTIMAL:
    print("Maximum profit: %d" % solver.ObjectiveValue())
    for idx, vm in enumerate(x):
        print("vm%d: %s" % (idx, STATES[solver.Value(vm)]))
