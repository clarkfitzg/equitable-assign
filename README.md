## Equitable random assignment

Suppose you are a member of a committee charged with reviewing many applications.
How do you randomly assign committee members to applications as equitably as possible?

In this talk, we define what equitable random assignment means, explain why it's desirable, and propose an algorithm to solve the problem.
More generally, the problem is to randomly assign a combination of workers to tasks such that each worker has the same load, and each task is equally likely to have any combination of workers.
We have incorporated equitable random assignment in our department's hiring process to improve equity, which was the original motivation for this work.
We conclude with a demonstration of our freely available open source software implementation, which is ready for public use.

keywords: equity, diversity, algorithm, software, randomization, workload

## Installation

```
python3 -m pip install equitable_assign
```

## Usage

Options:

1. `tasks` number of tasks (required)
2. `workers` number of workers, default to 2
3. `pertask` number of workers per task, default to 1
4. `viewtype` whether you want worker view (0), task view (1), or directory (2), defualt to worker view (0) 
5. `seed` integer to seed the random number generator, ensuring the same output
6. `allworkers` csv file where ouput will be printed
7. `dirname` this will make a directory and the csv files of the directory will be the tasks that each individual worker needs to complete

## Viewtype:

This provides the user with the option of storing their output in either worker view or taskview.
Worker view has the first entry of each line as which worker, from 1 to the value of `workers`, and is followed by the tasks that that worker needs to do.
Task view has the first entry of each line as which task, from 1 to the value of `tasks`, and is followed by the workers that correspond to that task.  
Directory creates a directory with csv files for each worker that contain the tasks that the worker needs to complete. 

The simplest way is to use it is from the command line.
Here we assign 11 tasks to 5 workers, with 3 workers per task, which means that some workers will have more tasks than others since there is not a perfectly equitable assignment. 
We use 2022 as the random seed, but it can be any integer.

### Task view:

once we have it on pi py
```
python3 -m equiassign.equiassign --tasks 11 --workers 5 --pertask 3 --viewtype 1 --seed 2022 --allworkers assignments.csv
```

this is if you run it locally
```
python3 equiassign.py --tasks 11 --workers 5 --pertask 3 --viewtype 1 --seed 2022 --allworkers assignments.csv
```

The result saves a random assignment of workers to tasks to `assignments.csv`

```
task,worker1,worker2,worker3
1,2,3,4
2,1,3,5
3,2,4,5
4,1,4,5
5,1,3,5
6,1,2,3
7,1,2,4
8,2,3,5
9,1,2,4
10,2,3,4
11,1,4,5
```

This output means that the first task is assigned to workers 1,2, and 3, the second task is assigned to workers 1,3, and 5, and the last (11th) task is assigned to workers 1,4, and 5.

### Worker view:

once we have it on pi py
```
python3 -m equiassign --tasks 11 --workers 5 --pertask 3 --viewtype 0 --seed 2022 --allworkers assignments.csv
```

this is if you run it locally
```
python3 equiassign.py --tasks 11 --workers 5 --pertask 3 --viewtype 0 --seed 2022 --allworkers assignments.csv
```

The result saves a random assignment of workers to tasks to `assignments.csv`

```
worker,task1,task2,task3,task4,task5,task6,task7
1,2,4,5,6,7,9,11
2,1,3,6,7,8,9,10
3,1,2,5,6,8,10,
4,1,3,4,7,9,10,11
5,2,3,4,5,8,11,
```

This output means that the first worker is assigned to tasks 2,4,5,6,7,9,and 11, the second worker is assigned to tasks 1,3,6,7,8,9, and 10 , and the last worker (5th) is assigned to tasks 2,3,4,5,8, and 11.
Note that it was not possible to give every worker an equal number of tasks thus some have more than others. 

### Directory: 

once we have it on pi py
```
python3 -m equiassign --tasks 11 --workers 5 --pertask 3 --viewtype 2 --seed 2022 --dirname assignments
```

this is if you run it locally
```
python3 equiassign.py --tasks 11 --workers 5 --pertask 3 --viewtype 2 --seed 2022 --dirname assignments
```
The directory `assignments` with 5 files corresponding to each worker. Every file contains the tasks that the worker would need to do.

Below is an example of what one of the files would appear as. 

`assignments/worker1`
```
2
4
5
6
7
9
11
```
