print("Welcome to my English quiz")
playing = input("Do you want to play? ")
if playing.lower() != "yes": 
    quit()
print("Okay!, Let's play :)")    
score = 0


answer = input("What is the past tense of go? ")
if answer.lower() == "went":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("Fill in the blank: I ______ eaten since 9:00 am. ")
if answer.lower() == "haven't":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    
answer = input("What day comes after Wednesday? ")
if answer.lower() == "Thursday":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer = input("Fill in the blanks: yesterday I _____(see) my friend? ")
if answer.lower() == "saw":
    print("correct!")
    score += 1
else:
    print("incorrect!")
    
print("you got " +str(score)+  "questions correct")

print("You got " + str(score/4)* 100+ "%")




    
    

    
