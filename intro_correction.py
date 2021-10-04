from ortools.sat.python import cp_model

model = cp_model.CpModel()
x = model.NewIntVar(0, 1, 'x')
y = model.NewIntVar(0, 2, 'y')
z = model.NewIntVar(0, 3, 'z')
model.Add(x != y)
model.Add(x < z)
solver = cp_model.CpSolver()
status = solver.Solve(model)
if status == cp_model.OPTIMAL:
    print("optimal")
elif status == cp_model.FEASIBLE:
    print("feasible")
elif status == cp_model.INFEASIBLE:
    print("infeasible")
elif status == cp_model.MODEL_INVALID:
    print("invalid model")
elif status == cp_model.UNKNOWN:
    print("no solution or problem can not be proven INFEASIBLE")
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print(solver.Value(x))
    print(solver.Value(y))
    print(solver.Value(z))
