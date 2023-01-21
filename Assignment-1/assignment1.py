state_space = {}

with open("Asxignment-1/test2.txt", "r") as f:
    # read lines from file
    d = int(f.readline())

    for i in range(1,d+1):
        line =  f.readline()
        
        neighbors = [int(x) for x in line.split()]
        state_space[i] = neighbors
        
for key, value in state_space.items():
    if(len(value) > 0):
        print(str(key) + " --> "+ str(value))
    else:
        print(str(key) + " --> " + "")