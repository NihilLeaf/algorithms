def searchMinor(arr):
  minor = arr[0]
  minor_index = 0
  for i in range(1, len(arr)):
    if arr[i] < minor:
      minor = arr[i]
      minor_index = i
  return minor_index

def orderSelection(arr):
  newArr = []
  for i in range(len(arr)):
    minor = searchMinor(arr)
    newArr.append(arr.pop(minor))
  return newArr

print(orderSelection([5, 3, 6, 2, 10]))