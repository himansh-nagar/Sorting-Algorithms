# #####  bubble sort

def bubble_sort(arr):
	l=len(arr)
	for i in range(l-1,-1,-1):
		for j in range(i):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]
	return arr

L = [9,-3,6,-1,1,-4,-6]

print(bubble_sort(L))