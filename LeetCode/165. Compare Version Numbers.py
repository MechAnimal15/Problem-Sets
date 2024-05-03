class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split the version strings into lists of revisions.
        v1_revisions = version1.split('.')
        v2_revisions = version2.split('.')
        
        # Determine the maximum number of revisions between the two versions.
        max_revisions = max(len(v1_revisions), len(v2_revisions))
        
        # Iterate through the revisions of both versions.
        for i in range(max_revisions):
            # Convert each revision to an integer or default to 0 if missing.
            v1_revision = int(v1_revisions[i]) if i < len(v1_revisions) else 0
            v2_revision = int(v2_revisions[i]) if i < len(v2_revisions) else 0
            
            # Compare revisions numerically.
            if v1_revision < v2_revision:
                return -1  # Return -1 if version1 < version2.
            elif v1_revision > v2_revision:
                return 1   # Return 1 if version1 > version2.
        
        # If all revisions are equal, return 0, indicating that both versions are the same.
        return 0
