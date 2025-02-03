def solve():
    numheads = int(input("Input number of heads:"))
    numlegs = int(input("Input number of legs:"))
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens 
        if(chickens * 2 + rabbits * 4) == numlegs:
            print("Chickens:", chickens, "Rabbits:", rabbits)
            return
    print("No solution")
solve()