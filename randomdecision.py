from random import randint
generatedAnswer = ""
randomNumber = randint(0,1)
print randomNumber
if randomNumber:
    generatedAnswer = "Yes"
    print generatedAnswer
else:
    generatedAnswer = "No"
    print generatedAnswer
