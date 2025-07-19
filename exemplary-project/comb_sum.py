def combinationSum(candidates, target):
    result = []
    
    def backtrack(start, current_combination, current_sum):
        # If we reach the target sum, add the combination to the result
        if current_sum == target:
            result.append(list(current_combination))  # Make a copy
            return
        
        # If the sum exceeds the target, stop exploring this path
        if current_sum > target:
            return
        
        # Try all candidates starting from the current index
        for i in range(start, len(candidates)):
            current_combination.append(candidates[i])  # Choose
            backtrack(i, current_combination, current_sum + candidates[i])  # Explore
            current_combination.pop()  # Undo choice (Backtrack)
    
    backtrack(0, [], 0)
    return result

# Example usage:
candidates = [2, 3, 6, 7]
target = 7

print(candidates,target)
print(combinationSum(candidates, target))
