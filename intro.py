from ortools.sat.python import cp_model

model = cp_model.CpModel()
x = model.NewIntVar(0, 1, 'x')
y = model.NewIntVar(0, 2, 'y')
z = model.NewIntVar(0, 3, 'z')
model.Add(x != y)
solver = cp_model.CpSolver()
status = solver.Solve(model)
print(status)
