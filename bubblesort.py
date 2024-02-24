import time
def bubbleSort(arr):
	n = len(arr)
	
	for i in range(n):
		swapped = False

		for j in range(0, n-i-1):

			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = True
				print(arr)
		if (swapped == False):
			break


if __name__ == "__main__":
	arr = [5,7,2,8,1,3,4,6]

	bubbleSort(arr)

	print("Sorted array:")
	for i in range(len(arr)):
		print("%d" % arr[i], end=" ")
		

 
start = time.time()
a = 0
for i in range(1000):
    a += (i**100)
end = time.time()
print("The time of execution of above program is :",(end-start) * 10**3, "ms")