import random

def game():
	# generate a random number between 1 and 10
	secret_num = random.randint(1, 10)
	guesses = []


	while len(guesses) < 5:
		# get a number guess from the player
		try:
			guess = int(raw_input("Guess a number between 1 and 10: "))
		except ValueError:
			print("{} isn't a number.".format(guess))
		else:
			# compare guess to secret number
			if guess == secret_num:
				print("You got it! My number was {}".format(secret_num))
				break
			elif guess < secret_num:
				print("My number is higher than {}".format(guess))
			elif guess > secret_num:
				print("My number is smaller than {}".format(guess))
			else:
				# print hit/miss
				print "That's not it"
			guesses.append(guess)
	else:
		print("You didn't get it! My number was {}".format(secret_num))
	play_again = raw_input("Do you want to play again? Y/n ")
	if play_again != 'n':
		game()
	else: print("Bye")

game()


