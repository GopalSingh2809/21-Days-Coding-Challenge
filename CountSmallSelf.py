class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (self.size + 1)
    
    def update(self, index, delta=1):
        while index <= self.size:
            self.tree[index] += delta
            index += index & -index
    
    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= index & -index
        return res

class Solution:
    def countSmaller(self, nums):
        # Coordinate compression
        unique_sorted = sorted(set(nums))
        rank = {v: i + 1 for i, v in enumerate(unique_sorted)}  # 1-based indexing
        
        max_rank = len(unique_sorted)
        fenwick_tree = FenwickTree(max_rank)
        
        res = []
        # Process from right to left
        for num in reversed(nums):
            r = rank[num]
            # Query the number of elements smaller than current num
            count = fenwick_tree.query(r - 1)
            res.append(count)
            # Update the Fenwick Tree with current num's rank
            fenwick_tree.update(r)
        
        # Reverse to get the correct order
        return res[::-1]
        
        
ans=Solution()
print(ans.countSmaller([5,2,6,1]))  # Output: [2,1,1,0]
print(ans.countSmaller([-1]))         # Output: [0]
print(ans.countSmaller([-1,-1]))      # Output: [0,0]