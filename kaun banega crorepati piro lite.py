import time 
print("Lets play kaun banega crorepati")
list=["what is the capital of india?","which is the hottest planet?"]
time.sleep(1)
print(list[0])
option=["delhi","kolkata","bihar"]
print(option)
answer=str(input("Enter your choice:"))
if answer=="delhi":
    print("Your answer is correct ")
else:
    print("You lost")
    exit()

time.sleep(1)    
print("Next question on your screen")
time.sleep(1)
print(list[1])
option2=["venus","mercury","jupiter"]
print(option2)
answer=str(input("Enter your choice:"))
if answer=="venus":
    print("your answer is correct")
else:
    print("your answer is incorrect")
    exit()
