bank = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o", "p", "q", "r", "s","t", "u", "v", "w", "x", "y", "z"]
# taking the user input and setting it equal to the variable word

word = input("Type a word for someone to guess: ")
spaces = []
for i in range(len(word)):
	spaces.append("_")
print(spaces)
maxfails = 6
while True:
	# Converts the word to lowercase
	word = word.lower()
	# Checks if only letters are present
	if(word.isalpha() == False):
		print("That's not a word!")
	wordl = word
	wordl = list(word)
	# Some useful variables
	# this is a list that will store the users letter guesses
	guess = input("Guess a letter: ")
	for i in range(0, len(word)):
		if word[i] == guess:
			spaces[i] = guess
	print(spaces)
# this will take the user's guess and set it equal to guess
	length = len(word)
	if guess in bank:
		if guess in word:
			print("That is in the word!")
			if spaces == wordl:
				print("You did it! Yay! You won!")
				break
		else:
			maxfails -= 1
			print("WRONG! You have this many fails left: ")
			print(maxfails)
			if maxfails == 0:
				print("No more tries ;( ")
				print("GAME OVER")
				break
