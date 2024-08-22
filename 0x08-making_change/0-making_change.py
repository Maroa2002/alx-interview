#!/usr/bin/python3
"""Module 0-making_change"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given total
    """
    if total <= 0:
        return 0
    
    # Initialize dp array
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Compute the fewest number of coins for each amount up to total
    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    
    # If dp[total] is still inf, total can't be formed with coins available
    return dp[total] if dp[total] != float('inf') else -1
