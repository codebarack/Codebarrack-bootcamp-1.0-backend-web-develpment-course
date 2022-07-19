#Implementation 1
def linearsearch(arr, x):
   for i in range(len(arr)):
      if arr[i] == x:
         return i
   return -1
arr = ['u','t','o','r','i','a','l']
x = 't'
print("element found at index "+str(linearsearch(arr,x)))

#Implementation 2

def linearSearch(array, n, x):

    # Going through array sequencially
    for i in range(0, n):
        if (array[i] == x):
            return i
    return -1


array = [2, 4, 0, 1, 9]
x = 1
n = len(array)

result = linearSearch(array, n, x)
if (result == -1):
    print("Element not found")
else:
    print("Element found at index: ", result)

#Implementation 3


def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i 
    return None

def verify(index):
    if index is not None:
        print("Target Found At Index ", index)
    else:
        return "Target not found in the list"

number = (1, 2, 3, 4, 5, 6, 7, 8)
result = linear_search(number, 3)
print(verify(result))


