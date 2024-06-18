import random
l=["R","P","S"]
while True:
    ch=input("Enter the choice (R/P/S):")
    bot=random.choice(l)
    print(f"Your choice--{ch.upper()} computer choice--{bot}")
    if ch.upper()==bot:
        print("Both did same")
        continue
    elif ch.upper()=="R":
        x=0 if bot=="P" else 1
    elif ch.upper()=="P":
        x=1 if bot=="R" else 0
    elif ch.upper()=="S":
        x=1 if bot=="P" else 0
    else:
        print("Invalid input")
        continue
    print("Sorry you lost") if x==0 else print("Congrats you won")
        