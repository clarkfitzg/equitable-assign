import random
import math
import argparse
import csv
import os.path

"""
This approach is very simple
Veriables (all positive integers):
        - A application
        - N reviewers
        - K size of committee

We are going to think of this in a manner of how we could assign 
reviewers to a comittee if we were all in-person.

First, we will make K slips for each application and label them. Thus, we will
have A*K slips in total.

Second, we will take all these slips, put them in a hat, and shake them up.

Third, we will line up all the reviewers in a single file line and then go
one by one giving them a single slip and then wrap back around once we have
gone to the end of the line. If the reviewer already has one of the slips we
assign them we will give them a new slip and put that one back in the hat.

It is possible that towards the end some of the reviewers will already have all the slips that are in the remaining hat so they will be skipped and another reviewer could be given more. Hence, an unoptimal assignment. We address this by having the reviewer with the most assignments give one of their assigments to the reviewer with the fewest. 
"""



def assign(A: int, N: int, K: int, verbose=True, **kwargs):

    #if the user inputed a larger number of reviewers per application than there are reviewers 
    if(N<K):  
        raise ValueError("pertask needs to be smaller than workers")
    #if any are negative 
    if(A <= 0 or N<= 0 or K<= 0):
        raise ValueError("need postive integers for all arguments")
    
    #make the A*K slips in an array
    slips = []
    for i in range(1,A+1):
        for j in range(0,K): #we could probably do this with numpy too
             slips.append(i)

    #shake up the hat
    random.shuffle(slips)

    #line the people up i.e. make a dictionary with an array
    #to store many values 
    line_of_rev_dict = {}
    for i in range(1,N+1):
        line_of_rev_dict["reviewer{0}".format(i)] = []

    #go through each reviewer and give them something from the hat
    #QUESTION:do we need to go further than len(slips)+1? Maybe use a while loop
    #dog = len(slips)+1
    for i in range(1,1000000000): #big number
        i = i%N
        if(i==0):
            i = N
        #print(line_of_rev_dict["reviewer{0}".format(i)])
        #hand them the slip if they don't have it 
        for j in range(0,len(slips)):
            if slips[j] not in line_of_rev_dict["reviewer{0}".format(i)]:
                line_of_rev_dict = add_values_in_dict(line_of_rev_dict,"reviewer{0}".format(i), [slips[j]])
                slips.pop(j)
                break

        if not slips:
            break

    #trade until they are at equatiably assigned 

    #if they can be perfectly assigned 
    if(((A*K)%N)==0):
        while(len({len(x) for x in line_of_rev_dict.values()}) > 1):
            trade(line_of_rev_dict)
    #if they can't be perfectly assigned 
    if(((A*K)%N)!=0):
        while(len({len(x) for x in line_of_rev_dict.values()}) > 2):
            trade(line_of_rev_dict)
    
    #put the dictionary into a list of tuples 
    alpha = list(tuple(sub) for sub in line_of_rev_dict.values()) 
    
    #sort the list of tuples
    for i in range(0,len(alpha)):
        alpha[i] = tuple(sorted(alpha[i]))

    #make the list into a tuple 
    alpha = tuple(alpha)

    return alpha  

#make a function that takes the person with the most slips and 
#donates one to the lowest 
def trade(d):
    #find the key with longest array 
    mx = 0
    for key in d:
        if(len(d[key])>=mx):
                mx = len(d[key])
                mx_key = key
    #find the key with the shortest arrayi
    mn = 10000000
    for key in d:
        if(len(d[key])<=mn):
                mn = len(d[key])
                mn_key = key
    #take an element from the array of the key with the most 
    #assignment and give one of those assignments to the lowest 
    for i in range(0,len(d[mx_key])):
        if d[mx_key][i] not in d[mn_key]:
            #print(d[mx_key][i])
            d[mn_key].append(d[mx_key][i])
            d[mx_key].pop(i)
            break     
    return list(d.values())


def add_values_in_dict(sample_dict, key, list_of_values):
    ''' Append multiple values to a key in 
        the given dictionary '''
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--tasks',type=int,required=True)
    parser.add_argument('--workers',type=int,default=2)
    parser.add_argument('--pertask',type=int,default=1)
    parser.add_argument('--viewtype',type=int,default=0) #0 for worker view and #1 for task view
    parser.add_argument('--seed',type=int,default=None)
    parser.add_argument('--allworkers',type=str,default=True)

    args = parser.parse_args()

    A = args.tasks
    N = args.workers
    K = args.pertask
    random.seed(args.seed)
    #data = list(assign(A,N,K))
    #data = [(1,2,3),(4,5,6),(7,8,9)]
    
    #put an error if assignments.csv already exists
    file_exists = os.path.exists(args.allworkers)
    if(file_exists):
        print("The csv file already exists so please delete or rename it") 

    
    #convert the tuple of tuples into a list of list
    data = assign(A,N,K)
    data = [list(x) for x in data]


    #worker view
    if(not file_exists and args.viewtype == 0):
        
 
        #add a None to all the lists that are less than the longest one 
        dataMaxLen = max([len(x) for x in data])
        for i in data:
            if(len(i) < dataMaxLen):
                i.append(None)  

        #I would add a reviewer to each list so we can identify them
        for i in range(0,len(data)):
            data[i].insert(0,i+1)


        #make a fields label which will first have worker then the max of how many tasks there will be per worker    
        fields = ["worker"]
        for i in range(1,max([len(x) for x in data])):
            fields.append("task{0}".format(i))

        #put them in a csv file
        with open(args.allworkers,'w') as out:
            file_writer=csv.writer(out)
            file_writer.writerow(fields)
            file_writer.writerows(data)

         
     #task view
    if(not file_exists and args.viewtype == 1):
         #tranform data from being lists of tasks and the task they need to do to lists of tasks and their corresponding worker
         
        tasksArr = [[] for x in range(A)]

         #loop through data and see which workers have the tasks and then assign them to that array in tasksArr
        for i in range(1,A+1):
            for j in range(0,len(data)):
                if(i in data[j]):
                    tasksArr[i-1].append(j+1) 

        for i in range(0,len(tasksArr)):
            tasksArr[i].insert(0,i+1)

        #make a fields label which will first have worker then the max of how many tasks there will be per worker    
        fields = ["task"]
        for i in range(1,K+1):
            fields.append("worker{0}".format(i))

        with open(args.allworkers,'w') as out:
            file_writer=csv.writer(out)
            file_writer.writerow(fields)
            file_writer.writerows(tasksArr) 


    
