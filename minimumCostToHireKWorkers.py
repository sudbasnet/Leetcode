import heapq


class Solution:
    def mincostToHireWorkers(self, quality: [int], wage: [int], K: int) -> float:
        '''
        Best Explanation:
        https://leetcode.com/problems/minimum-cost-to-hire-k-workers/discuss/141768/Detailed-explanation-O(NlogN)
        Let's read description first and figure out the two rules:

        "1. Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group."
        So for any two workers in the paid group,
        we have wage[i] : wage[j] = quality[i] : quality[j]
        So we have wage[i] : quality[i] = wage[j] : quality[j]
        We pay wage to every worker in the group with the same ratio compared to his own quality.

        "2. Every worker in the paid group must be paid at least their minimum wage expectation."
        For every worker, he has an expected ratio of wage compared to his quality.

        So to minimize the total wage, we want a small ratio.
        So we sort all workers with their expected ratio, and pick up K first worker.
        Now we have a minimum possible ratio for K worker and we their total quality.

        As we pick up next worker with bigger ratio, we increase the ratio for whole group.
        Meanwhile we remove a worker with highest quality so that we keep K workers in the group.
        We calculate the current ratio * total quality = total wage for this group.

        We redo the process and we can find the minimum total wage.
        Because workers are sorted by ratio of wage/quality.
        For every ratio, we find the minimum possible total quality of K workers.

        Time Complexity
        O(NlogN) for sort.
        O(NlogK) for priority queue.

        ============
        My Approach:
        ============
        what is the minimum wage of the worker with the least quality??
        pay that person the minimum wage. Then based on that, we could get the pay for others
        but the pay might be less than what the other workers are asking for. SO if anything 
        increases for the rest of the workers, then pay increases for the min wage worker too.

        [1, 2, 1, 5, 10, 3] -> [1, 1, 2, 3, 5,  10]
                            -> [3, 3, 6, 9, 15, 30]
        [1, 1, 3, 4, 35, 5]
        K -- want to hire K workers only

        '''
        '''
        since we are trying to minimize the money, we need to pick people with least demands.
        
        quality: [1, 2, 1, 5, 3, 10]
        demands: [1, 3, 3, 4, 5, 35]
        
        divides: [1, 3/2, 3/1, 4/5, 5/3, 35/10]
        
        sort them by division
        
        pick the kth ratio, if we pick this ratio we know that the other ratios will be less
        and the wage can only go up never down, so all wage requirements are satisfied.
        
        # Couldn't proceed after this..
        
        # Checked the explanation from above
        
        also sort the quality for each of the workers. and put them in a Heap possibly. 
        Pull the worker with the highest quality and throw them out. move the ratio to the
        next bigger one. Return the lowest price you see
        '''

        '''
        code design
        
        (ratio, wage, quality) ... sort them
        pick the first k <- put them in a maxHeap 
        move the cursor from k -> k+1 heapify stuff 
        '''
        if not quality:
            return 0

        if K > len(quality) or len(quality) != len(wage):
            return 0

        minSum = float('inf')
        ratios = []
        for i in range(len(quality)):
            ratios.append([wage[i]/quality[i], quality[i], wage[i]])

        ratios.sort()

        qualityHeap = []
        heapq.heapify(qualityHeap)

        totalQuality = 0
        for i in range(K):
            totalQuality += ratios[i][1]
            heapq.heappush(qualityHeap, - ratios[i][1])

        ratio = ratios[K-1][0]
        totalSum = totalQuality * ratio
        minSum = totalSum

        for i in range(K, len(ratios)):
            ratio = ratios[i][0]
            newQuality = ratios[i][1]

            removedQuality = - heapq.heappop(qualityHeap)
            heapq.heappush(qualityHeap, - newQuality)

            totalQuality = totalQuality - removedQuality + newQuality
            totalSum = ratio * totalQuality
            minSum = min(minSum, totalSum)

        return minSum
