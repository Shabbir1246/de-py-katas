def get_frequencies(arg):
	letter_freq = {}
	for char in arg:
		if char != ' ':
			if char in letter_freq:
				letter_freq[char] += 1  
			else: letter_freq[char] = 1
	return letter_freq