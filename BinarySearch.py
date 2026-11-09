shk
#Second modify
# Find x in the list a
while left <= right:
    middle = (left + right) // 2
  
    if a[middle] == int(x):  # Success
        print('There is {:3} at a[{:2}] in the list.'.format(x, middle))
        break   
    elif a[middle] < int(x):
        left = middle + 1    
    else:
        right = middle - 1

if left > right: # Fail
    print('There is not {:3} in this list.'.format(x))
