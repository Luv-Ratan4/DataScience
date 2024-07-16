import time

a =input("Hi! What is your name? ")
timestamp = int(time.strftime('%H'))
#timestamp = int(time.strftime('%M')) - For Minutes
#timestamp = int(time.strftime('%S')) - For Seconds

# timestamp2 = time.strftime()

print(timestamp)

if(timestamp < 12):
    print("Hey" , a, "Good Morning", )
elif(timestamp > 12):
    if(timestamp < 18):
        print("Hey" , a, "Good Afternoon" )
    elif(timestamp < 9):
        print("Hey" , a, "Good Evening", )
    else:
        print("Hey" , a, "Good Night", )
