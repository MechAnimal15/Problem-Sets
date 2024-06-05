1002. Find Common Characters
[Problem Link](https://leetcode.com/problems/find-common-characters/submissions/1278632607?envType=daily-question&envId=2024-06-05)


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize the frequency counter with the first word's character frequencies
        common_count = Counter(words[0])
        
        # Iterate over each subsequent word
        for word in words[1:]:
            # Update the counter to keep only minimum frequencies
            word_count = Counter(word)
            for char in common_count:
                common_count[char] = min(common_count[char], word_count[char])
        
        # Construct the result list based on the common_count frequencies
        result = []
        for char, count in common_count.items():
            result.extend([char] * count)
        
        return result

  Runtime: 58 ms
  Memory: 16.6 MB
