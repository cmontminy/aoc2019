# DAY 1: Fuel required to launch a given module is based on its mass. 
# Specifically, to find the fuel required for a module, take its mass, 
# divide by three, round down, and subtract 2.

f = open("input.txt", "r")

# part one
total = 0

for mass in f:
    fuel = (int(mass) // 3) - 2 # // for integer division
    total += fuel

f.close()
print("part one fuel needed: ", total)

# part two
f = open("input.txt", "r")

total = 0
for mass in f:
    fuel = (int(mass) // 3) - 2
    while fuel > 0:
        total += fuel
        fuel = (fuel // 3) - 2
        
    
f.close()
print("part two fuel needed: ", total)

