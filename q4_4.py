from ortools.linear_solver import pywraplp

# Variables
serverCapacity = [ 10, 20, 10000 ]
serverCons = [ 100, 200, 10000 ]
nbServers = len(serverCapacity)
# We define the trash server as the last server of the list
trashServerIdx = nbServers - 1
vmConso = [ 5, 5, 3, 10, 7]
vmCosts = [ 10, 3, 5, 1, 9 ]
nbVms = len(vmConso)
nbRunning = 2

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
# Each VM must be in exactly one server.
for i in range(nbVms):
    solver.Add(sum(vms[i, j] for j in range(nbServers)) == 1)
# The amount packed in each server cannot exceed its capacity.
for j in range(nbServers):
    solver.Add(sum(
        [ vms[i, j] * vmConso[i] for i in range(nbVms)]) <= servers[j] * serverCapacity[j])
# Off VM are hosted on the third server (trash server)
solver.Add(sum([ vms[i, trashServerIdx] for i in range(nbVms)]) == nbVms - nbRunning)
# Compute the cost of all VM hosted on a different server than the trash server
total_cost = []
for i in range(nbVms):
    for j in range(nbServers - 1):
        isRunning = sum([vms[i, j]])
        total_cost.append(isRunning * (vmCosts[i] - serverCons[j]))
solver.Maximize(sum(total_cost))

status = solver.Solve()
if status == pywraplp.Solver.INFEASIBLE:
    print("No Solution")
if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
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
            print("  vm%d (cons: %d, cost: %d, power: %d)" % (
                i, vmConso[i], vmCosts[i], serverCons[idx]))
    print("Profit: %d" % solver.Objective().Value())
