"""
a CPU task is defined as Task(id, queued_time, exec_time). Id is the task's id; queued_time is the time when the 
task joins the queue; exec_time is the time needed to execuate the task. Given a collection of CPU tasks return 
the order of task ids thats been executed by one-core evil CPU. For example (1, 2, 2), (2, 5, 15), (3, 5, 10) would 
return 1, 3, 2. The reason is that at 2nd second, task#1 joined the queue and it's the only one in the queue. 
It's been executed first. At 4th second, task#1 is finished. CPU is in idling state. At 5th second, task#2 and 
task#3 joined the queue. CPU will first execute task#3 as task#3 has smaller exec_time. At 15th second, task#3 is 
finished. Task #2 is still in the queue. Task#2 will be execuated. So the order of execuation is 1, 3, 2.
"""

class Task:
    def __init__(self, id, queued_time, exec_time):
        self.id = id
        self.queued_time = queued_time
        self.exec_time = exec_time

