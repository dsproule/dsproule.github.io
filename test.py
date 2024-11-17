t = ['a', 'b', 'c']
def run(arr):
	arr[0] = 'b'
	print(arr)
run(t[:])
print(t[:0] + t[1:])