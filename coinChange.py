# there's apparently a better solution using DFS ????
# not sure how to solve it that way, will think about it later if I get time

class Solution:
    def coinChange(self, coins: [int], amount: int) -> int:
        """
        I know we need to solve it bottom up
        
        this actually depends on the amount that we want to calculate coins for??
        
        lets say we have coins for $1 and $2 and $5 only!!!
        
        amount: 1, 2, 3, 4, 5, 6, 7
        coins:  1, 1, 
        
        3 ---
        now how many coins for 3
        if I use 1$ coin, thats 1 coin
        now 3-1 = 2, check if there's a 2 in the dictionary, since there is, take 2's coins = 1
        so total coins is now 2
        
        If I use 2$ coin, thats 1 coin again
        now 3-2 = 1, check if there's a 1 in the dictionary, since there is, take 1's coins = 1
        so total coins is now 2 again
        
        if I use 5$ coin, its greater than 3 so answer is 2 coins
        
        4 ---
        if I use 1$ coin, thats 1 coin
        check if there's a 4-1 = 3 in the dictionary, yes there is we just assigned it 2 coins
        so total coins = 3
        
        if I use 2$ coin, thats 1 coin
        check if there's a 4-2 = 2 in the dictinoary, yes there is, its value is 1
        so total coins = 2
        
        if I use 5$ coin, its larger than 4
        so answer is min(3, 2) = 2
        
        5---
        since there is a 5$ coin, so answer is 1
        
        6---
        if I use 1$ coin, check for 5 in the dictionary, there is, its value is 1
        if I use 2$ coin, check if there's a 4 in the dictionary, there is, its value is 2, so thats 3 coins
        if I use 5$ coin, check if there's a 1 in dict, there is, its value is 1, so thats 2 coins again
        so the answer is 2 coins
        
        7--
        if I use 1$ coin, check if there is a 6, there is, its value is 2, so we get 3 coins
        if I use 2$ coin, check if there is a 5, there is, its value is 1, so we get 2 coins
        if I use 5$ coin, check if there is a 2, there is, its value is 1, so we get 2 coins again
        so the answer is 2
        
        do it for all ....
        complexity = O(n x m) n = amount and m = len(coins)
        
        """
        
        if amount <= 0:
            return 0
        
        coinChanges = {}
        
        for amt in range(1, amount+1):
            for coin in coins:
                numOfCoins = 0
                
                if coin == amt:
                    numOfCoins += 1
                else:
                    remainingAmt = amt - coin
                    numOfCoins += 1
                    
                    if remainingAmt in coinChanges:
                        numOfCoins += coinChanges[remainingAmt]
                    else:
                        continue  

                coinChanges[amt] = min(coinChanges.get(amt, float("inf")), numOfCoins)
                 
        return coinChanges[amount] if (amount in coinChanges) else -1
                        
