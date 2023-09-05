def findMissing(arr):
 i = 0
 missing = -1
 while i < len(arr):
  j = arr[i]
  if j != i+1:
   arr[j-1], arr[i] = arr[i], arr[j-1]
  i += 1

 for i in range(len(arr)):
  if arr[i] != i+1:
   return arr[i]
 return  -1

 def __main__():
  arr = [2,1,4,5,6]
  findMissing(arr)   
