import matplotlib.pyplot as plt
import numpy as np
import random

##############################################################################################################

for k in [2,4,8,16,32,64]: # number of processors
    waits = []
    memory_modules = [m for m in range(1,2048+1)]
    for m in range(1,2048+1): # for each requested_memory module

        wait_times_array = []
        for i in range(k):
            # [processor ID, wait time, memory module index, list of averages of wait time, 
            # memory module allocated(boolean)]
            wait_times_array.append([i,0,0,[],False]) 
        mem_cycle_cnt = 1
        old_avg = None
        while(True): # memory cycle

            # sorts the wait_times_array in reverse order based on the wait time. 
            # This is to make sure the processors which did not get a memory module in the last memory cycle, 
            # get higher priority in the next cycle
            # Prevents starvation
            wait_times_array.sort(key=lambda x: x[1],reverse=True) 

            requested_mem = [] # Re-initializing the memory modules after each cycle 
            for each_item in wait_times_array:
                if(each_item[4] == True):
                    r = int(round(random.uniform(0,m))) # Uniform Distribution --- selection of memory modules.
                else:
                    each_item[4] = True
                    r = each_item[2]

                each_item[2] = r

                # If, the requested memory module has been requested by another processing element in this cycle.
                if r in requested_mem:
                    # Increment the wait time, if the requested memory module has already been allocated to another 
                    # processing element, and toggle the boolean value.
                    each_item[1] += 1 
                    each_item[4] = False
                else:
                    requested_mem.append(r) # Create the requested memory list
                    each_item[4] = True

                each_item[3].append(float(each_item[1])/mem_cycle_cnt) # list of running avgs.

                
            mem_cycle_cnt += 1
        val = float(0)
        
        for each_item in wait_times_array:
            val += float(sum(each_item[3]))/len(each_item[3])
        new_avg = float(val)/k

        if(old_avg == None):
            old_avg = new_avg
            # termination condition --- when the current value differs from the previous one by less than 0.02%. 
            elif ((old_avg - new_avg) < 0.0002* old_avg): 
                waits.append(new_avg)
                break
            else:
                old_avg = new_avg
        # import pdb;pdb.set_trace() --- for debugging

    plt.title("Uniform Destribution; Number of Processors: {}".format(k))
    plt.plot(memory_modules, waits)
    plt.xlabel('Number of memory modules')
    plt.ylabel('Average number of memory cycles for each request')
    plt.show()


##########################################################################################################

for k in [2,4,8,16,32,64]: # number of processors
    waits = []
    memory_modules = [m for m in range(1,2048+1)]
    for m in range(1,2048+1): # for each requested_memory module

        wait_times_array = []
        for i in range(k):
            # [processor ID, wait time, memory module index, list of averages of wait time, 
            # memory module allocated(boolean)]
            wait_times_array.append([i,0,0,[],False]) 
        mem_cycle_cnt = 1
        old_avg = None
        while(True): # memory cycle

            # sorts the wait_times_array in reverse order based on the wait time. 
            # This is to make sure the processors which did not get a memory module in the last memory cycle, 
            # get higher priority in the next cycle
            # Prevents starvation
            wait_times_array.sort(key=lambda x: x[1],reverse=True) 

            requested_mem = [] # Re-initializing the memory modules after each cycle 
            for each_item in wait_times_array:
                if(each_item[4] == True):
                    mean = int(random.uniform(0,m))
                    sd = float(mean)/10
                    # Gaussian Distribution --- selection of memory modules.
                    # with mean value coming from a uniform distribution
                    # and the standard deviation being calculated as (mean/10)
                    r = int(np.random.normal(mean, sd)) 
                else:
                    each_item[4] = True
                    r = each_item[2]

                each_item[2] = r

                # If, the requested memory module has been requested by another processing element in this cycle.
                if r in requested_mem:
                    # Increment the wait time, if the requested memory module has already been allocated to another 
                    # processing element, and toggle the boolean value.
                    each_item[1] += 1 
                    each_item[4] = False
                else:
                    requested_mem.append(r) # Create the requested memory list
                    each_item[4] = True

                each_item[3].append(float(each_item[1])/mem_cycle_cnt) # list of running avgs.

                
            mem_cycle_cnt += 1
        val = float(0)
        
        for each_item in wait_times_array:
            val += float(sum(each_item[3]))/len(each_item[3])
        new_avg = float(val)/k

        if(old_avg == None):
            old_avg = new_avg
            # termination condition --- when the current value differs from the previous one by less than 0.02%. 
            elif ((old_avg - new_avg) < 0.0002* old_avg): 
                waits.append(new_avg)
                break
            else:
                old_avg = new_avg
        # import pdb;pdb.set_trace() --- for debugging

    plt.title("Gaussian Destribution; Number of Processors: {}".format(k))
    plt.plot(memory_modules, waits)
    plt.xlabel('Number of memory modules')
    plt.ylabel('Average number of memory cycles for each request')
    plt.show()