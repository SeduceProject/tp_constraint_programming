### 1. Profit for a Cloud provider
We are a cloud provider. We have already sold 5 VMs to ours clients. Each VM has
a cost (between 1 to 10 dollars) for our client (ex [10,3,5,1,9]).

Print on the screen our profit. You need construct a vmCost array and compute
the sum of each cost.

### 2. Profit with Contention for a Cloud provider
We have 5 VMs. Each VM has a State (0=Off, 1=On). Our data center is very
limited, so we cant host all clients VMs. In our new problem, we want exactly
nbRunning VMs On.
Every VM can have the value 0 (off VM) or 1 (on VM). The sum of every VM state
must be equal to nbRunning.

**NOTE**: We can use the VarArraySolutionPrinterWithLimit() solution printer to
display only N solutions. For example, VarArraySolutionPrinterWithLimit(x, 3)
displays the 3 solutions of the problem. We can use the function last_solution()
to retrieve the variable values of the last solution in an array.

1. Write a code to compute the state of the 5 VM. Print all VM States and
   compute the cost.
2. Use one variable nbVM to define the number of VM of our datacenter. Define
   the number of the model variables from the nbVM variable. For example,
   ```
   variables = []
   for i in range(nbVM):
       variables.append(model.NewIntVar(0, X, 'vm%i'))
   ```
   Display 5 solutions of our problem and compute the cost for one of them.
3. Create the class VarArraySolutionPrinterWithLimitAndCost that displays the
   cost of every solution. The __init__ method shoud have the following
   arguments: __init__(self, variables, limit, vmCosts)
4. Now, we want exactly nbRunning VM while maximizing our profit. Compute and
   display the optimal solution using the model.Maximize() function.

### 3. BinPacking
1. We have 5 objects with [2, 2, 5, 8, 5] for their capacities. We have 4 bins
   of 8. By using the [google
   example](https://developers.google.com/optimization/bin/bin_packing), write a
   code that solves this problem.
2. Comment the line `solver.Minimize()`. Explain the purpose of the Minimize()
   objective.

### 4. BinPacking and VM Placement
1. We add the server concept in our data center. Each server has a capacity.
   Each VM a consumption. So, we add 2 servers with 10 and 20 for their
   capacities. Our 5 VMs have [10,5,3,5,7] for their consumption. All VM are On.
   Each VM On must be placed on a server. So, if the VM1 is placed on Server1,
   the VM1 will consume all Server1 capacities. Find a correct placement. 
2. We want exactly nbRunning VM On. For that, we define a ghost server (like a
   trash). This ghost server has a big capacity, each All Vm Off must be placed
   on the Ghost server. 
3. Same as previous question, but we want maximize our profit.
4. Each server has a VM power consumption, for each VM placed on it, the server
   consumes Xw. (ex: if the VM power consumption on Server1 is equal to 100,
   then, if 2 VMs are placed on Server1, the Server1 power consumption is equal
   to 200. If the server is unused (no VM), it’s power consumption is equal to
   0). We want exactly nbRunning VM. We want to maximize our profit.
   Unfortunately, 1 W cost 1 dollar. So our profit is the sum of VM On minus the
   total power consumption. In this question, We want exactly nbRunning VM On
   and maximize our profit.
