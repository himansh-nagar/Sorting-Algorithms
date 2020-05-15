### selection sort

def selection_sort(arr):
	l=len(arr)
	for i in range(l):
		for j in range(i,l):
			if arr[j]<arr[i]:
				arr[i],arr[j]=arr[j],arr[i]
	return arr

L=[-9,6,-4,5,-3,-8,0]
print(selection_sort(L))
