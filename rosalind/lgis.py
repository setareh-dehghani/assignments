def LIS(nums, n):
    dp = [] 
    dp_list = []

    for i in range(n):
        dp.append(1)
        dp_list.append([nums[i]])
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
                if len(dp_list[i]) <= len(dp_list[j]):
                    dp_list[i] = dp_list[j] + [nums[i]]
    
    print(max(dp), dp_list[dp.index(max(dp))])
    return dp, dp_list

def LDS(nums, n):
    dp = [] 
    dp_list = [] 

    for i in range(n):
        dp.append(1)
        dp_list.append([nums[i]])
        for j in range(i):
            if nums[j] > nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
                if len(dp_list[i]) <= len(dp_list[j]):
                    dp_list[i] = dp_list[j] + [nums[i]]
    
    print(max(dp), dp_list[dp.index(max(dp))])
    return dp, dp_list

if __name__ == "__main__":
    with open("C:/Users/setareh/Documents/rosalind/rosalind_lgis.txt", "r") as f:
        n = int(f.readline().strip())
        nums = [int(i) for i in f.readline().strip().split(" ")]

    LIS(nums, n)
    LDS(nums, n)