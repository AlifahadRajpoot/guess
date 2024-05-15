import random
l=["rock","paper","scissor"]
while True:
    ucount=0
    ccount=0
    uc=int(input("""Welcome To Rock,Paper,Scissor Game:
                 1.Play
                 2.No"""))
    if uc ==1:
        for i in range(1,6):
            userinput=int(input("""please enter your choice :
                                1.rock
                                2.paper
                                3.scissor"""))
            if userinput==1:
                uchoice="Rock"
            elif userinput==2:
                uchoice="Paper"
            elif userinput==3:
                uchoice="Scissor"
            Cchoice=random.choice(l)
            if Cchoice==uchoice:
                print("Computer value",Cchoice)
                print("User value",uchoice)
                print("Game Draw")
                ucount+=1
                ccount+=1
            elif (uchoice=="rock" and Cchoice=="paper") or (uchoice=="rock" and Cchoice=="scissor") or (uchoice=="paper" and Cchoice=="scissor"):
                print("Computer value",Cchoice)
                print("User value",uchoice)
                print("You Win")
                ucount+=1
            else:
                print("Computer value",Cchoice)
                print("User value",uchoice)
                print("Computer Win")
                ccount+=1
            if ucount==ccount:
                print("Game Draw")
                print("User score",ucount)
                print("Computer score",ccount)
            elif ucount>ccount:
                print("Congrulation You Win")
                print("User score",ucount)
                print("Computer score",ccount)
            else:
                print("Computer Win")
                print("User score",ucount)
                print("Computer score",ccount)
    else:
        print("invalid")
        break;        
                
                
                
                
                
                
                
                
                
                
                
                
            