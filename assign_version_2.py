import random
import math 

"""
This will be the new approach to assign. 

Veriables (all positive integers):
    - A application
    - N reviewers
    - K size of committee

We intend to build a function that will be have A vectors of length K.
These vectors will initially all be set to zero. 
For each vector we will randomly select K indices and then flip them to ones.
We will also calculate the workload per person (wpp = (A*K)/N), keep track of 
how much work each reviewer has done, and only assign reviewers that have 
workloads below the ceiling of wpp.
"""

def assign(A: int, N: int, K: int, verbose=True, **kwargs):
    
    #determine the workload per person and cieling the value
    wpp = math.ceil((A*K)/N) 
    
    #make an array that keeps track of workload
    workload = N*[0]

    #generate A arrays of size K of all zeros and store them in a dictionary
    d_of_arrays = {}
    for i in range(0,A):
        d_of_arrays["a{0}".format(i)] = [0]*N

    #create a loop that goes through the workload array and randomly 
    #flips K different indices per array, it should only flip indices
    #that have workloads less than wpp
 

    for value in d_of_arrays.items():
        good = good_indices(workload,wpp)
        #make a list to be used for sorting
        sorting_list = [None] * len(good)
        for i in range(0,len(good)):
            sorting_list[i] = workload[good[i]]
        #sort good by using sorting_list to get the indices by workload in 
        #ascending order. That means, the indices that we found were below 
        #wpp by using the function good_indices() will be sorted into a list
        #where the indices which have the lowest values will appear at the 
        #begining of the list
        sample = [x for _,x in sorted(zip(sorting_list,good))]
        """
        NOT WORKING:this was an approach I took to try and fix 
        the problem with the overlap
        choose the max workload
        max = workload[sample[K-1]]
        randomly take values from sample under max 
        arr = []
        for i in sample:
            if(workload[i] <= max):
                arr.append(i)
        
        sample = [lambda x: workload[x] <= max, sample]
        sample = random.sample(arr,K) 
        go through an flip on the values sample wants us to flip and increment
        workload
        """
        #since sample is already sorted in ascending order we can just take 
        #the first K indices from it
        sample = sample[:K] 
        #flip the indices to one
        for i in sample:
            value[1][i] = 1
            workload[i] += 1

    print(d_of_arrays)
    print("**********")
    print(workload) 

#a function that determines which indices are below the workload and returns those indices
def good_indices(workload,wpp):
    good_indices = []
    for i in range(0,len(workload)):
        if(workload[i]<wpp):
            good_indices.append(i)
    return good_indices


if __name__ == "__main__":

        assign(6, 5, 3)






