import random
import math 

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

"""



def assign(A: int, N: int, K: int, verbose=True, **kwargs):
    
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
    return line_of_rev_dict

def add_values_in_dict(sample_dict, key, list_of_values):
    ''' Append multiple values to a key in 
        the given dictionary '''
    if key not in sample_dict:
        sample_dict[key] = list()
    sample_dict[key].extend(list_of_values)
    return sample_dict

    
if __name__ == "__main__":
    print(assign(60, 5, 4))

