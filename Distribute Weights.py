def possible(arr, m, k):
	curr_stats = arr[0]
	stats = 1
	flag = True
	for i in range(1, len(arr)):
		if arr[i] + curr_stats > k:
			curr_stats = arr[i]
			stats += 1
		else:
			curr_stats += arr[i]
		if stats > m:
			flag = False
			break
	return flag

print("Enter elements for an Array --> ", end="")
arr = list(map(int, input().split()))
m = int(input("How many Sub-groups? --> "))

left = max(arr)
right = sum(arr)
mid = (left + right)//2
ans = []
while left <= right:
    if possible(arr, m, mid):
        ans.append(mid)
        right = mid - 1
    else:
        left = mid + 1
    mid = (left+right)//2

print("Minimum value of the maximum sub-group is --> ", min(ans))
