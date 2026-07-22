#1. maximum sub array sum in an array
# def max_subarray_sum(arr,k):
#     left = 0
#     max_sum = 0
#     window_sum = 0
#     for right in range(len(arr)):
#         window_sum+=arr[right]
#
#         if right >= k - 1:
#             max_sum = max(max_sum,window_sum)
#
#             window_sum -= arr[left]
#
#             left+=1
#     return max_sum
# # arr=[2,1,5,1,3,2]
# arr = [1,2,3,4,5]
# k=3
# print(max_subarray_sum(arr,k))

#2. Longest Substring with At Most K Distinct Characters

# def longest_substring(s, target):
#     left = 0
#     max_len = 0
#     freq = {}
#
#     for right in range(len(s)):
#         # freq[s[right]] = freq.get(s[right], 0)+1
#         if s[right] in freq:
#             freq[s[right]]+=1
#         else:
#             freq[s[right]] = 1
#
#         while len(freq) > target :
#             freq[s[left]] -= 1
#             if freq[s[left]] == 0 :
#                 del freq[s[left]]
#             left += 1
#
#         max_len = max(max_len, right - left + 1)
#     return max_len
# # s='eceba'
# s='abcabcbb'
# target = 2
# print(longest_substring(s,target))

#3. Longest Substring Without Repeating Characters

# Maximum Subarray Sum problem, solved optimally using Kadane’s Algorithm.
# def maxSubarraySum(arr, n):
#     current_sum = 0
#     max_sum = 0
#
#     for num in arr:
#         current_sum += num
#
#         if current_sum > max_sum:
#             max_sum = current_sum
#
#         if current_sum < 0:
#             current_sum = 0
#
#     return max_sum
# arr= list(map(int,input().split()))
# n=int(input())
# print(maxSubarraySum(arr, n))


#42. Trapping Rain Water
# height = [0,1,0,2,1,0,1,3,2,1,2,1]
# s=0
# for i in range(0,len(height)):
#     print(i,s)
#     s+=min(max(height[0:i+1]),max(height[i:len(height)]))-height[i]
# print(s)

#TC: O(n**2)
#SC: O(2n)

