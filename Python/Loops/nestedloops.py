# One loop inside other Loop
for x in range(6):           # Outer loop executes till 0,1,2,3,4,5 and executed 5 times cause of inner loop range set to 5
    for y in range(5):       # Inner loop executes till 0,1,2,3,4 and executed 5 times cause of range 5 
        print(f"{x},{y}")    # formatted write to get the coordinates as (x,y)