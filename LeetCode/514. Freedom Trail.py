class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # Find the minimum steps between two indexes of ring
        def count_steps(curr, next):
            steps_between = abs(curr - next)
            steps_around = len(ring) - steps_between
            return min(steps_between, steps_around)

        # Create a dictionary to store the indices of each character in the ring
        char_indices = {}
        for i, char in enumerate(ring):
            if char not in char_indices:
                char_indices[char] = []
            char_indices[char].append(i)
        
        # Initialize the memoization table to store minimum steps
        memo = [[float('inf')] * len(ring) for _ in range(len(key))]

        # Initialize the starting position of the ring
        start_pos = 0

        # Initialize the first row of the memoization table
        for idx in char_indices[key[0]]:
            memo[0][idx] = count_steps(0, idx)

        # Spell the keyword using the metal dial
        for i in range(1, len(key)):
            for j in char_indices[key[i]]:
                for k in char_indices[key[i - 1]]:
                    if k < len(memo[i - 1]) and j < len(memo[i]):
                        memo[i][j] = min(memo[i][j], memo[i - 1][k] + count_steps(k, j))

        # Return the minimum steps to spell the entire keyword
        return min(memo[-1]) + len(key)
