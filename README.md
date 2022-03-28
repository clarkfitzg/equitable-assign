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
4. `seed` integer to seed the random number generator, ensuring the same output

The simplest way is to use it from the command line.
Here we assign 10 tasks to 5 workers, with 2 workers per task, which means each worker will be assigned 4 tasks.
We use 2022 as the random seed, but it can be any integer.

```
python -m equiassign --tasks 10 --workers 5 --pertask 2 --seed 2022 --saveas assignments.csv
```

The result saves a random assignment of workers to tasks to `assignments.csv`

```
1,4
2,5
...
2,4
```

This output means that the first task is assigned to workers 1 and 4, the second task is assigned to workers 2 and 5, and the last (10th) task is assigned to workers 2 and 4.
