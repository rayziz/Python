

def data_read(filename):
    with open(filename, mode="r") as filename:
        data = filename.read().split('\n')
    data.pop()
    return list(map(int, data))


# Function to print all distinct triplet in the list with the given sum
def printAllTriplets(nums, target = 0):

	# sort the list in ascending order
	nums.sort()

	n = len(nums)

	# check if triplet is formed by nums[i] and a pair from
	# sublist nums[i+1…n)
	for i in range(n - 2):

		# remaining sum
		k = target - nums[i]

		# maintain two indices pointing to endpoints of the
		# sublist nums[i+1…n)
		(low, high) = (i + 1, n - 1)

		# loop if `low` is less than `high`
		while low < high:

			# increment `low` index if the total is less than the remaining sum
			if nums[low] + nums[high] < k:
				low = low + 1

			# decrement `high` index if the total is more than the remaining sum
			elif nums[low] + nums[high] > k:
				high = high - 1

			# triplet with the given sum is found
			else:
				# print the triplet
				print((nums[i], nums[low], nums[high]))

				# increment `low` index and decrement `high` index
				low = low + 1
				high = high - 1


# nums = [1, 3, -4, 5, 8, -2, -6, 6, 2, -1]

print(printAllTriplets(data_read("1Kints.txt")))

# printAllTriplets(nums)

# data_read("1Kints.txt")