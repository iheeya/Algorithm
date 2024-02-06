nums =[]
for i in range(9):
    tc = int(input())
    nums.append(tc)

mx = 0
index = 0

for i in range(9):
    if nums[i] > mx:
        mx = nums[i]
        idx = i+1


print(mx)
print(idx)