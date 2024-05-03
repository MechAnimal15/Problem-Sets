class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split the versions by dot ('.')
        v1 = version1.split('.')
        v2 = version2.split('.')
        
        # Iterate through revisions of both versions
        for i in range(max(len(v1), len(v2))):
            # Get the integer value of revisions (or 0 if not specified)
            num1 = int(v1[i]) if i < len(v1) else 0
            num2 = int(v2[i]) if i < len(v2) else 0
            
            # Compare revisions
            if num1 < num2:
                return -1
            elif num1 > num2:
                return 1
        
        # If all revisions are equal, return 0
        return 0
