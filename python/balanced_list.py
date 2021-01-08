def compare(element1,element2):
	'''
	Function to compare where is balance
	'''
    if element1 > element2:
        return "left"
    elif element1 < element2:
        return "right"
    else:
        return "leftright"

# The algorithm using loops
def balanced1(arr):
    left = 0
    right = 0
    for i in range(len(arr)//2):
        left += arr[i]
    for i in range(len(arr)//2,len(arr)):
        right += arr[i]

    return compare(left,right)

# The algorithm using slices
def balanced2(arr):
    left = sum(arr[:len(arr)//2])
    right = sum(arr[len(arr)//2:])
    return compare(left,right)

#The algorithm using generators
def balanced3(arr):
    return compare([sum([arr[i] for i in range(len(arr)) if (i >= len(arr)//2) == r]) for r in range(2)])

# Lambda try
# lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]

test = [6,7,8,9,10,11,15,16,17]
balanced1(test)
balanced2(test)
balanced3(test)