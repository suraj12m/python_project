#Game -- stone paper scissors
import random
n=input("Enter your name : ")
print(f" Welcome {n} to Game of stone paper scissors")
print(" Game Rule: \n stone 🪨: 's' \n paper 📰: 'p' \n scissors ✂: 'se'" )
print("------------------------------------------  \n")
print("""How to play:-
 stone will win by scissor and loss by paper
 paper will win by stone and loss by scissor
 scissor will win by paper and loss by stone\n""")
print("------------------------------------------  \n")

total_u=0
total_c=0
for i in range(0,5):
    print(f"ROUND {i+1}")
    user=str(input("Your turn : "))

    d=0
    l=-1
    w=1
    s=0
    p=1
    se=2

    if(user=="s"):
        a=s
    elif(user=="p"):
        a=p
    elif(user=="se"):
        a=se
    else:
        raise ValueError("You have enter wrong")
    game=["s","p","se"]
    val= [
        [d,l,w],
        [w,d,l],
        [l,w,d]
    ]
    r=random.randint(0,2)
    comp=game[r]
    print("computer : ",comp)

    if(comp=="s"):
        b=s
    elif(comp=="p"):
        b=p
    elif(comp=="se"):
        b=se

    res=val[a][b]
   

    if(res==-1):
        total_c+=1

    if(res==1):
        total_u+=1

    if(res==0):
        print("DRAW \n")
    elif(res==1):
        print("WIN \n")
    elif(res==-1):
        print("LOSS \n")


print("------------------------------------------  \n")
print(f"Score obtain by {n} : {total_u}")
print(f"Score obtain by computer : {total_c}")
if(total_u>total_c):
    print(f"Congratulation {n} You WIN 🥳 🥳 🥳")
elif(total_u==total_c):
    print("DRAW 🤝 🤝 🤝")
else:
    print(f"Sorry {n} you LOSS 🥲 🥲 🥲\n")