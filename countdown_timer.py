import time

my_time = int(input("Enter the time in seconds: "))

# from 0 to whatever time you choose
# for x in range(0,my_time):
#     print (x)
#     # program will sleep for given amount of seconds, in this case 3 seconds
#     time.sleep(1)

# print ("TIMES UP")

# from whatever time you choose, but backwards
# for x in range(my_time, 0, -1):
#     print (x)
#     time.sleep(1)

# print ("TIMES UP")

# display digital clock
for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print (f"{hours}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print ("TIMES UP")