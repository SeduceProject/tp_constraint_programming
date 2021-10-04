from ortools.linear_solver import pywraplp

# Variables
nbBins = 4
binCapacity = 8
objectWeights = [2, 2, 5, 5, 8]

solver = pywraplp.Solver.CreateSolver('SCIP')

# Solver Variables
# y[j] = 1 if bin j is used.
bins = {}
for j in range(nbBins):
    bins[j] = solver.IntVar(0, 1, 'bin_%i' % j)
# x[i, j] = 1 if item i is packed in bin j.
objects = {}
for i in range(len(objectWeights)):
    for j in range(nbBins):
        objects[(i, j)] = solver.IntVar(0, 1, 'object_%i_%i' % (i, j))

# Constraints
# Each item must be in exactly one bin.
for i in range(len(objectWeights)):
    solver.Add(sum(objects[i, j] for j in range(nbBins)) == 1)
# The amount packed in each bin cannot exceed its capacity.
for j in range(nbBins):
    solver.Add(sum(
        [ objects[(i, j)] * objectWeights[i] for i in range(len(objectWeights))]
        ) <= bins[j] * binCapacity)
solver.Minimize(solver.Sum([bins[j] for j in range(nbBins)]))
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    binObjects = []
    for j in range(nbBins):
        binObjects.append([])
    for i in range(len(objectWeights)):
        for j in range(nbBins):
            if objects[i, j].solution_value() == 1:
                binObjects[j].append(i)
    for idx, content in enumerate(binObjects):
        print("Inside bin%d:" % idx)
        for i in content:
            print("  object%d (weight: %d)" % (i, objectWeights[i]))


