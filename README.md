# Distributed-Systems-simulation
This program simulates how multiple processors request access to multiple memory modules (via an Interconnection Network).


The main goal of this program is to use computer simulation to characterize the access time of processing elements to memory modules under certain workload
assumptions.

Two workloads assumptions will be assumed.
• Each processing element issues a memory module request at the beginning of each
memory cycle using a uniform distribution.
• Each processing element issues a memory module request at the beginning of each
memory cycle using a Gaussian distribution with a different mean for each processing
element.

The result of this simulation has been plotted in a graph of the average processing elements memory access times when keeping the number of processing
elements fixed and varying the number of memory modules.

• One plot per each fixed number of processors k for k ∈ {2, 4, 8, 16, 32, 64}.
• In each plot, the X − axis represents the number of memory modules varying from 1
to 2048.
• In each plot, the Y − axis represents the average, in time and across the processing
elements, of the number of memory cycles that requests take. (The average memory
access time is the sum of all the waiting times divided by the total number of requests
so far.)
