nums = (12 , 13 , 56 , 36 ,26)

x = 56

i = 0

while i < len(nums):
    if(nums[i] == x):
        print("got it", i)
    else:
        print("finding...")
    i += 1
    