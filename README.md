## Equitable random assignment

Suppose you are a member of a committee charged with reviewing many applications.
How do you randomly assign committee members to applications as equitably as possible?

In this talk, we define what equitable random assignment means, explain why it's desirable, and propose an algorithm to solve the problem.
More generally, the problem is to randomly assign a combination of workers to tasks such that each worker has the same load, and each task is equally likely to have any combination of workers.
We have incorporated equitable random assignment in our department's hiring process to improve equity, which was the original motivation for this work.
We conclude with a demonstration of our freely available open source software implementation, which is ready for public use.

keywords: equity, diversity, algorithm, software, randomization, workload

## Installation

TODO: Upload to Pypi, figure out how to install on a fresh machine.

## Usage

Options:

1. `tasks` number of tasks (required)
2. `workers` number of workers, default to 2
3. `pertask` number of workers per task, default to 1
4. `viewtype` whether you want worker view (0) or task view (1), defualt to worker view (0) 
5. `seed` integer to seed the random number generator, ensuring the same output
6. `allworkers` csv file where ouput will be printed

Viewtype:

This provides the user with the option of storing their output in either worker view or taskview.
Worker view has the first entry of each line as which worker, from 1 to the value of `workers`, and is followed by the tasks that that worker needs to do.
Task view has the first entry of each line as which task, from 1 to the value of `tasks`, and is followed by the workers that correspond to that task.  

The simplest way is to use it from the command line.
Here we assign 10 tasks to 5 workers, with 2 workers per task, which means each worker will be assigned 4 tasks.
We use 2022 as the random seed, but it can be any integer.

Task view:

once we have it on pi py
```
python -m equiassign --tasks 10 --workers 5 --pertask 2 --viewtype 1 --seed 2022 --allworkers assignments.csv
```

this is if you run it locally
```
python equiassign.py --tasks 10 --workers 5 --pertask 2 --viewtype 1 --seed 2022 --allworkers assignments.csv
```

The result saves a random assignment of workers to tasks to `assignments.csv`

```
task1,1,4
task2,2,5
...
task10,2,4
```

This output means that the first task is assigned to workers 1 and 4, the second task is assigned to workers 2 and 5, and the last (10th) task is assigned to workers 2 and 4.

Worker view:

once we have it on pi py
```
python -m equiassign --tasks 10 --workers 5 --pertask 2 --viewtype 0 --seed 2022 --allworkers assignments.csv
```

this is if you run it locally
```
python equiassign.py --tasks 10 --workers 5 --pertask 2 --viewtype 0 --seed 2022 --allworkers assignments.csv
```

The result saves a random assignment of workers to tasks to `assignments.csv`

```
worker1,1,3,4,9
worker2,2,7,8,10
worker3,4,6,7,8
worker4,1,5,6,10
worker5,2,3,5,9
```

This output means that the first worker is assigned to tasks 1,3,4,9, the second worker is assigned to tastks 2,7,8,10, and the last worker (5th) is assigned to tasks 2,3,5,9.
