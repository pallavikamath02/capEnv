def find_missing(nums, n=None):
    if n is None:
        n = len(nums) + 1
    expected = n * (n + 1) // 2
    return expected - sum(nums)
nums = [0, 6, 12, 24, 36]  
missing_number = find_missing(nums)
print(f"The missing number is: {missing_number}")