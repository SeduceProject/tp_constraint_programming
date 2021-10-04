from ortools.linear_solver import pywraplp

# Variables
serverCapacity = [ 10, 20 ]
nbServers = len(serverCapacity)
vmConso = [ 5, 5, 3, 10, 7]
nbVms = len(vmConso)

solver = pywraplp.Solver.CreateSolver('SCIP')

# Solver Variables
# y[j] = 1 if bin j is used.
servers = {}
for j in range(nbServers):
    servers[j] = solver.IntVar(0, 1, 'server_%i' % j)
# x[i, j] = 1 if item i is packed in bin j.
vms = {}
for i in range(nbVms):
    for j in range(nbServers):
        vms[(i, j)] = solver.IntVar(0, 1, 'vm_%i_%i' % (i, j))

# Constraints
# Each item must be in exactly one bin.
for i in range(nbVms):
    solver.Add(sum(vms[i, j] for j in range(nbServers)) == 1)
# The amount packed in each bin cannot exceed its capacity.
for j in range(nbServers):
    solver.Add(sum(
        [ vms[(i, j)] * vmConso[i] for i in range(nbVms)]
        ) <= servers[j] * serverCapacity[j])
status = solver.Solve()
if status == pywraplp.Solver.OPTIMAL:
    vmPlacement = []
    for j in range(nbServers):
        vmPlacement.append([])
    for i in range(nbVms):
        for j in range(nbServers):
            if vms[i, j].solution_value() == 1:
                vmPlacement[j].append(i)
    for idx, content in enumerate(vmPlacement):
        print("On server%d (capacity: %d):" % (idx, serverCapacity[idx]))
        for i in content:
            print("  vm%d (weight: %d)" % (i, vmConso[i]))
