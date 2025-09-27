# multithreading: used to perform multiple tasks concurrently (multitasking)
#                 good for I/O bound tasks like reading files or fetching data from APIs
#          threading.Thread(target=my_function)

import threading
import time

def walk_dog(name):
    time.sleep(8) # takes 8 seconds to walk the dog
    print(f"you finish walking {name}")

def take_out_trash():
    time.sleep(2) # takes 2 seconds to take out the trash
    print("you take out the trash")

def get_mail():
    time.sleep(4) # takes 4 seconds to get the mail
    print("you get the mail")

# all three exist on the same thread
# walk_dog()
# take_out_trash()
# get_mail()
    
# execute these methods concurrently (fastest gets done first)
chore1 = threading.Thread(target=walk_dog, args=("Scooby",)) # comma lets python know its a tuple
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_mail)
chore3.start()

# waits for all three chores to finish before printing final message
chore1.join()
chore2.join()
chore3.join()

print("all chores are complete")