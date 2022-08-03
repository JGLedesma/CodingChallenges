def sevenBoom(arr):
    for x in arr:
        if "7" in str(x):
            print("Boom!")
            return
    print("There is no seven.")
    
arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8, 9, 10]
arr3 = [14, 15, 16, 17, 18]

sevenBoom(arr1)
sevenBoom(arr2)
sevenBoom(arr3)
