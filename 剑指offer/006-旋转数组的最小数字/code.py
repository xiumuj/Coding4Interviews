def minNumberInRotateArray(rotateArray):
    # write code here
    if not rotateArray:
        return 0
    low = 0
    high = len(rotateArray) - 1
    while True:
        mid = (low + high) // 2
        if rotateArray[mid] >= rotateArray[low]:
            low = mid
        else:
            high = mid
        if rotateArray[mid] < rotateArray[mid-1]:
            return rotateArray[mid]

print(minNumberInRotateArray([3,4,5,1,2]))
print(minNumberInRotateArray([1,1,1,0,1]))
print(minNumberInRotateArray([]))




class Solution:
    def minNumberInRotateArray(self, rotateArray):
        left = 0
        right = len(rotateArray) - 1
        while right - left >1:
            mid = int((left + right)/2)
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            else:
                right = mid
        return min(rotateArray[right],rotateArray[left])
