#Break and continue ------------------------

for i in range(1, 101, 1):
    if(i==5):
        print("Skip the iteration")
        continue
    if(i == 10):
        break
    else:
        print(i)
    
i =0

while True:
    print(i)
    i = i+1
    if(i%10 == 0):
        print("Skip this iteration")
        continue
    elif(i%101 == 0):
        break

