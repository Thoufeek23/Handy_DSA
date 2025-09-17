#Matrix transpose
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
for i in range(len(matrix)):
    for j in range(i+1, len(matrix[0])):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

print("Matrix transpose: ", matrix)


#Subsets
def substring(n):
    subs = []
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            subs.append(n[i:j+1])
    return subs

nums = [1, 2, 3, 4, 5]
s = "abcde"

nums_subs = substring(nums)
string_subs = substring(s)

print("List subs: ", nums_subs)
print("Sting subs: ", string_subs)


#Permutations in List
def permutation_list(index, nums, ans):
    if index == len(nums):
        ans.append(nums[:])
        return
    seen = set()
    for i in range(index, len(nums)):
        if nums[i] in seen:
            continue
        seen.add(nums[i])
        nums[index], nums[i] = nums[i], nums[index]
        permutation_list(index+1, nums, ans)
        nums[index], nums[i] = nums[i], nums[index]

#Permutations in String
def permutation_str(index, s, ans):
    if index == len(s):
        ans.append("".join(s))
        return
    seen = set()
    for i in range(index, len(s)):
        if s[i] in seen:
            continue
        seen.add(s[i])
        s[index], s[i] = s[i], s[index]
        permutation_str(index+1, s, ans)
        s[index], s[i] = s[i], s[index]


ans_li, ans_str = [], []
nums = [1, 2, 3]
permutation_list(0, nums, ans_li)
s = "abc"
permutation_str(0, list(s), ans_str)
print("List permutations: ", ans_li)
print("String permutations: ", ans_str)

#Combinations
def comb(arr, k):
    ret = []
    def helper(start, path):
        if len(path) == k:
            ret.append(path[:])
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            helper(i+1, path)
            path.pop()
    helper(0, [])
    return ret

nums = [1, 2, 3, 4]
ans = comb(nums, 2)
print("List combination: ", ans)

#Create a Hashtable
def hash_table(nums):
    h = {}
    for val in nums:
        if val in h:
            h[val] += 1
        else:
            h[val] = 1
    return h

nums = [1, 1, 1, 2, 2, 2, 2 ,2 ,2, 3, 3 ,3, 4, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6]
print("Hash Table: ", hash_table(nums))