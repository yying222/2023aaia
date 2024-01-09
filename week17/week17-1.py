class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        nums.sort()#先把數字排好    
        ans=[[nums[0]]]#把最前面  最小的數字，放在裡面
        repeat=0#目前的nums裡沒重複
        N =len(nums)
        for i in range(1,N):
            if nums[i]==nums[i-1]:
                repeat+=1
                if len(ans)<=repeat:#層數不夠
                    ans.append([])#增加一層
            else:
                repeat=0
            ans[repeat].append(nums[i])
        return ans