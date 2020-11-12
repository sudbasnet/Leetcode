"""
given a list of utilization at any time/seconds i, [UT1, UT2, UT3 ... UTi].
if less than 25%, halve the number of instances, dont halve if half < 1
if more than 60%, double the number of instance, dont double if double > 2 * 10^8

if doubled or halved (taken any action), then dont do anything for next 10 seconds (next 10 utilization records)

"""

def finalInstances(instances, averageUtil):
    upperLimit = 2 * (10**8)
    pause = 0
    for i in range(len(averageUtil)):
        # take action if < 25%
        if averageUtil[i] < 25 and pause == 0 and instances > 1:
            instances = math.ceil(instances/2)
            pause = 10
        # take action if > 60%
        elif averageUtil[i] > 60 and pause == 0:
            doubled = instances * 2
            if doubled <= upperLimit:
                instances = doubled
                pause = 10
        else:
            pause = (pause - 1) if (pause > 0) else 0
    return instances