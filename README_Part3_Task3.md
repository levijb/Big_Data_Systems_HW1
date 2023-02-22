# Big_Data_Systems_HW1
# Part 3: PageRank, Task 3

In the step we run the same program as in task 2, but halfway through the process kill one of the two workers to examine its impact on the runtime.
- Keeping partitions active for faster runtime

To kill a worker:
- Clear the memory cache using sudo sh -c "sync; echo 3 > /proc/sys/vm/drop_caches" on vm2;
- Kill the Worker process on vm2: Use jps to get the process ID (PID) of the Spark Worker on vm2 and then use the command kill -9 <Worker_PID> to kill the Spark Worker process.

