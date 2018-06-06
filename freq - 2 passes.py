import re

ciphertext = raw_input('Enter cipher text: ').upper()

####### BASIC FREQUENCY ANALYSIS #########

letters = [] # Used to store unique letters in ciphertext
frequency = {} #  Used to store frequency of letters
engFreq = "EARIOTNSLCUDPMHGBFYWKVXZJQ" # Frequency of English letter usage, in order

# FIlter out any non-letter characters, add to letters list, count frequency
for letter in ciphertext:
	if re.match('[A-Z]', letter):
 		if letter not in letters:
			letters.append(letter)
			frequency[letter] = ciphertext.count(letter)

# Create sorted lists by frequency from dictionary
letterKeys = sorted( frequency, key=frequency.__getitem__, reverse=True)
letterValues = sorted( frequency.values(), reverse=True )

print ''
print 'FREQUENCY ANALYSIS'
print ''	

# Replace ciphertext with plaintext by matching frequency
plaintext = ciphertext
i = 0
replacedLetters = []
for letter in letterKeys:
	print letter, letterValues[i], '(%s)' % engFreq[i]
	if letter not in replacedLetters:
		plaintext = plaintext.replace( letter, engFreq[letterKeys.index(letter)].lower() )
		replacedLetters.append(letter)
	i += 1
print ''
print ciphertext
print plaintext
print ''

####### DOUBLE LETTERS #######
if re.match(r'([A-Z])\1', ciphertext):
	lstDbletters = re.findall(r'([A-Z])\1', ciphertext)

	print 'DOUBLE LETTERS FOUND:'
	for letter in lstDbletters:
		print letter,
	print 'MOST COMMON USED:'
	print 's e t f l m o'
	print ''
	
###### THREE LETTER WORDS ######
print 'THREE LETTER WORD POSSIBILITIES'
print ''

possibilities = []
plaintext = ciphertext

words = ciphertext.split(' ')
threeLtrWords = ('the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'any', 'her', 'can', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'may', 'end')


replacedLetters = []
for wordCip in words:
	y = 0
	if len(wordCip) == 3:
		for word in threeLtrWords:
			for letter in wordCip:
				if letter not in replacedLetters:
					plaintext = plaintext.replace( letter, word[y] )
					replacedLetters.append(letter)
					y += 1
			possibilities.append(plaintext)			
			plaintext = ciphertext
			replacedLetters = []
			y = 0
			
#print 'DEBUG - possibilities 1', len(possibilities)
	
#threeWorking = threeLtrWords
new3LtrPoss = []
#######
looping = True
ogPoss = len(possibilities)
while looping:
	startPoss = len(possibilities)
	for phrase in possibilities:
		
		threeWorking = list(threeLtrWords)

		#print '\n[-]PHRASE:', phrase
		splitPhrase = phrase.split(' ')
		found = ''
		loop = True
		while loop:
			new3LtrPoss = [] 
			for word in splitPhrase:
				#print '\n[-]Current ciphertext:', word
				if not re.match(r'[a-z]', word):
					continue
				if len(word) == 3:
					#print '[-]Word is 3 letters'
					if word in threeLtrWords:
						if found:
							loop = False
							#if len(new3LtrPoss) == 0:
							#	try:
							#		possibilities.remove(phrase)
							#		print 'DEBUG - removing', phrase
							#		print 'DEBUG - PHRASE REMOVED'
							#		break
							#	except:
							#		break
							#raw_input()
						found = word
						try:
							threeWorking.remove(word)
							#print '[-]Removed "' + word + '" from threeWorking'
						except:
							continue
					else:
						for w3 in threeWorking:
							#print '\n[-]Current PT word:', w3
							for i in range(len(word)):
								if re.match(r'[a-z]', word[i]):
									#print '[-]' + word, 'starts with  a lowercase letter'
									#print '[-]Checking if', word[i], 'matches', w3[i]
									if word[i] == w3[i]:
										#print '[-]Match! Appending new 3 ltr poss'
										new3LtrPoss.append(w3)
									else:
										#print '[-]Does not match, continuing'
										continue
								else:
									continue
								####
								for poss in new3LtrPoss:
									for x in range(len(word)):
										#print '[-]Vetting new possibility', poss, 'against', word
										#print '[-]Checking if', poss[x], '!=',  word[x]
										if re.match(r'[a-z]', word[x]):
											#print '[-]Lowercase OK.'
											if poss[x] != word[x]:
												#print '[-]Mismatch found, removing possibility'
												new3LtrPoss.remove(poss)
												break 
										else:
											#print '[-]Letters match or enciphered, next letter...'
											continue										
								'''
								if len(new3LtrPoss) == 0:
									#print 'DEBUG - possibilities', possibilities
									#print 'DEBUG - PHRASE:', phrase
									try:
										possibilities.remove(phrase)
										print 'DEBUG - PHRASE REMOVED' 
									except:
										continue
								
								else:
									
									try:
										possibilities.remove(phrase)
										print 'DEBUG - removing', phrase
										print 'DEBUG - PHRASE REMOVED' 
										break
									except:
										continue
								'''
						if len(new3LtrPoss) == 0:
							try:
								possibilities.remove(phrase)
								#print 'DEBUG - removing', phrase
								#print 'DEBUG - PHRASE REMOVED'
								break
							except:
								continue
			#print 'DEBUG - new3LtrPoss:', new3LtrPoss
			
			#print 'DEBUG'
			#print len(possibilities)

			#raw_input('end of phrase\n')
	endPoss = len(possibilities)
	if startPoss == endPoss:
		break
#for phrase in possibilities:
#	print phrase


#######	
print ''	
print 'OG Possibilities:', ogPoss
print 'Current Possibil:', endPoss
print ciphertext
print '_' * 20

#workingWords = list(threeLtrWords)
#print '[-]workingWords:', workingWords
 	
for phrase in possibilities:
	workingWords = list(threeLtrWords)
	possiWords = []
	pairs = []
	newPoss = []
	print '\n[!]Phrase:', phrase
	for word in phrase.split(' '):
		
		matchedLetters = ['','','']
		print '\n[-]Ciphertext:', word
		if len(word) != 3:
			continue
		else:
			if word in workingWords:
				workingWords.remove(word)
				print '[-]Removed ciphertext from working words'
			else:
				for letter in word:
					if letter.islower():				
						matchedLetters[word.index(letter)] = letter
				print '[-]Appended letters', matchedLetters
				#newPattern = ''.join(matchedLetters)
				#print '[-]Pattern: "' + newPattern + '" created'
				
				lowers = 0
				for i in range(3):
					if word[i].islower():
						lowers += 1
				print '[-]', lowers, 'lowers found'
				
				print '[-]Looking for pattern matches in working words'
				for work in workingWords:
					if lowers == 0:
						continue
					print '[-]Working with:', work
					matched = 0
					while matched != lowers:
						for i in range(3):
							#print '[-]Current index:', i
							if matchedLetters[i] == '':
								print '[-]Blank, skipping'
								continue
							print '[-]Checking', work[i], '->', matchedLetters[i]
							if work[i] != matchedLetters[i]:
								break
							elif work[i] == matchedLetters[i]:
								print '[-]Positional match found at index', i, work[i], 'to', matchedLetters[i ] 
								matched += 1
							else:
								continue
						if matched != lowers:
							break
								
							#else:
							#	break
					if matched == lowers:
						newPoss.append(work)
						print '[!]Appended newPoss:', work
					'''
					try: 
						if work[i+1].islower() and work[i+1] == matchedLetters[i+1]:
							newPoss.append(work)
							print '[-]Pattern found in', work, '.. Appending to newPoss'
									
					except:
						continue
					'''
		if word in newPoss:
			newPoss.remove(word)
	
		#if word == 'and':
		#	raw_input()
	
	if len(newPoss) == 0:
		possibilities.remove(phrase)
	print '[-]New Possibilities:', newPoss		

for phrase in possibilities:
	print phrase