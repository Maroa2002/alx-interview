#!/usr/bin/python3
"""
0-prime_game
"""


def isWinner(x, nums):
    """
    Determines the overall winner after x rounds of the game.

    Parameters:
    x (int): The number of rounds to play.
    nums (list of int): An array containing the value of n for each round.

    Returns:
    str: The name of the player who won the most rounds ("Maria" or "Ben").
         Returns None if there is a tie.
    """

    def sieve_of_eratosthenes(max_n):
        """
        Generates all prime numbers up to and including max_n.

        Parameters:
        max_n (int): The maximum number up to which to generate primes.

        Returns:
        list: A list of prime numbers up to and including max_n.
        """
        primes = [True] * (max_n + 1)
        p = 2
        while (p * p <= max_n):
            if primes[p] is True:
                for i in range(p * p, max_n + 1, p):
                    primes[i] = False
            p += 1
        prime_list = [p for p in range(2, max_n + 1) if primes[p]]
        return prime_list

    def simulate_game(n):
        """
        Simulates a single round of the game and determines the winner.

        Parameters:
        n (int): The size of the set (1 to n) used in this round.

        Returns:
        int: The winner of the round (0 for Maria, 1 for Ben).
        """
        primes = sieve_of_eratosthenes(n)
        remaining_numbers = set(range(1, n + 1))
        current_player = 0  # Maria = 0, Ben = 1
        while primes:
            prime = primes.pop(0)
            multiples = set(range(prime, n + 1, prime))
            remaining_numbers -= multiples
            if not remaining_numbers.intersection(primes):
                return current_player
            current_player = 1 - current_player
        return 1 - current_player

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n < 2:
            ben_wins += 1
        else:
            winner = simulate_game(n)
            if winner == 0:
                maria_wins += 1
            else:
                ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
