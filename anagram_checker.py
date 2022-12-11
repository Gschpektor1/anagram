class AnagramChecker:

	def __init__(self, file):
		self.file = file

	def is_valid_word(self, word):
		# should check if the given word (ie. the word of the user) is a valid word.
		self.word = word
		if word.isalpha():
			return word 
		else:
			return False

	def get_anagrams(self, word):
		# should find all anagrams for the given word. (eg. if word of the user is ‘meat’,
		# the function should return a list containing [“mate”, “tame”, “team”].)
		self.word = word
		matching_words = []
		for line in open(self.file):
			line = line.strip()
			line = line.lower()
			if len(line) == len(word):
				sorted_word = sorted(word)
				sorted_line = sorted(line)
				if sorted_line == sorted_word:
					matching_words.append(line)
		return matching_words








