print('''
Welcome
If you want to beat the Computer, guess the right number between 0 and 9
Remember you have only 3 guesses
    ''')
name=input("What's your name?  ")
import random
number=random.randint(0,9)
guess_count=0
guess_limit=3
while guess_count<guess_limit:
	guess=int(input("@@@@>>> GUESS : "))
	guess_count+=1
	if guess == number :
		print(' Congratulations ' + name + ' you guessed the right number :)' )
		break
	elif guess < number :
		print("Number too low!") 
	elif guess > number :
		print("Number too high!")
else :
	  print(' Sorry ' + name + ' you failed ): ')
	  num=str(number)
	  print(' The number I was thinking was ' + num )  
			


