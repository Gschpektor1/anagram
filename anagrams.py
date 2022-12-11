from anagram_checker import AnagramChecker

def menu():
	choices = ['P', 'Q']
	choice = input('Please select one of: \n(P)lay, (Q)uit \n')
	while choice not in ['P', 'Q']:
		print('Incorrect input, please select one of the choices')
		choice = input('Please select one of: \n (P)lay, (Q)uit \n')
	return choice

def main():
	playing = True
	while playing == True:
		choice = menu()
		if choice == 'Q':
			playing = False
		else:
			word = input('input one word \n')
			while ' ' in word:
				print(word)
				word = input('I said one word, input one word')
			while not word.isalpha():
				word = input('Only alphanumeric')
			word = word.strip()
			checker = AnagramChecker('word.txt')
			matching_words = checker.get_anagrams(word)
			words = ', '.join(matching_words)
			print(f'Your word is {word}\nganagrams are: {words}')




main()