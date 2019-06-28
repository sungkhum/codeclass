def mult(n, m):
	"""mult(n, m) should return the product of the two 
	integers n and m. Since this would be a bit too easy if 
	the multiplication operator * were used, for this function, 
	you are limited to using the addition, subtraction, and 
	negation operators, along with recursion. (Use the power 
	function we did in class as a guide.)"""
    
    #check if any negative numbers

	if n < 0 and m < 0:
		sign = 'bothnegative'
	elif n < 0 and m > -1:
		sign = 'firstnegative' 
	elif n > -1 and m < 0:
		sign = 'secondnegative'
	elif n > -1 and m > -1:
		sign = 'bothpositive' 

	if m == 0:
		return 0
		
	else:
		if sign == 'bothnegative':
			return (n * -1) + mult(n, m+1)
		elif sign == 'firstnegative':
			return n + mult(n, m-1)
		elif sign == 'secondnegative':
			return (n * -1) + mult(n, m+1)
		elif sign == 'bothpositive':
			return n + mult(n, m-1)


#
# Tests
#
assert mult(6, 7)   ==  42
assert mult(6, -7)  == -42
assert mult(-6, 7)  == -42
assert mult(-6, -7) ==  42
assert mult(6, 0)   ==   0
assert mult(0, 7)   ==   0
assert mult(0, 0)   ==   0

#print(mult(-6, 7))

def dot(L, K):
	"""dot(L, K) should return the dot product of the lists L and K."""

	if L == [] or K == []:
		return float(0)
	elif len(L) != len(K):
		return float(0)

	else:
		return L[0] * K[0] + dot(L[1:], K[1:])

#
# Tests
#
assert dot([5, 3], [6, 4])                       == 42.0
assert dot([1, 2, 3, 4], [10, 100, 1000, 10000]) == 43210.0
assert dot([5, 3], [6])                          == 0.0
assert dot([], [6])                              == 0.0
assert dot([], [])                               == 0.0

#print(dot([7, 8], [6, 9]))


def ind(e, L):
	"""Write ind(e, L), which takes in a sequence L and 
	an element e. L might be a string, or it might be a list. """

	if L == [] or L == '':
		return len(L)

	elif e == L[0]:
		return 0
	elif e != L[0]:
		return 1 + ind(e, L[1:])

#
# Tests
#
assert ind(42, [55, 77, 42, 12, 42, 100]) == 2
assert ind(42, list(range(0, 100)))       == 42
assert ind('hi', ['hello', 42, True])     == 3
assert ind('hi', ['well', 'hi', 'there']) == 1
assert ind('i', 'team')                   == 4
assert ind(' ', 'outer exploration')      == 5

#print(ind('rss', ['well', 'hi', 'there']))

def letterScore(let):
	"""return the value of character as a Scrabble tile point value"""
	if let == '':
		return 0

	elif let in 'aeilnorstu':
		return 1
	elif let in 'dg':
		return 2
	elif let in 'bcmp':
		return 3
	elif let in 'fhvwy':
		return 4
	elif let in 'k':
		return 5
	elif let in 'jx':
		return 8
	elif let in 'qz':
		return 10

#
# Tests
#
assert letterScore('a') == 1
assert letterScore('z') == 10
assert letterScore('b') == 3
assert letterScore('w') == 4

#print(letterScore('a'))

def scrabbleScore(S):


	if S == '':
		return 0
	elif S[0] in 'aeilnorstu':
		return 1 + scrabbleScore(S[1:])
	elif S[0] in 'dg':
		return 2 + scrabbleScore(S[1:])
	elif S[0] in 'bcmp':
		return 3 + scrabbleScore(S[1:])
	elif S[0] in 'fhvwy':
		return 4 + scrabbleScore(S[1:])
	elif S[0] in 'k':
		return 5 + scrabbleScore(S[1:])
	elif S[0] in 'jx':
		return 8 + scrabbleScore(S[1:])
	elif S[0] in 'qz':
		return 10 + scrabbleScore(S[1:])
	else:
		return 0 + scrabbleScore(S[1:])

#
# Tests
#
assert scrabbleScore('quetzal')                    == 25
assert scrabbleScore('jonquil')                    == 23
assert scrabbleScore('syzygy')                     == 25
assert scrabbleScore('abcdefghijklmnopqrstuvwxyz') == 87
assert scrabbleScore('?!@#$%^&*()')                == 0
assert scrabbleScore('')                           == 0

#print(scrabbleScore('quetzal'))


def one_dna_to_rna(c):
        """Converts a single-character c from DNA
           nucleotide to complementary RNA nucleotide """
        if c == 'A':
            return 'U'
        if c == 'C':
            return 'G'
        if c == 'G':
            return 'C'
        if c == 'T':
            return 'A'
        else:
        	return ''
        # you'll need more here...


def transcribe(S):
	"""Convert DNA nucleotide to RNA nucleotide"""

	if S == '':
		return ''
	else:
		return one_dna_to_rna(S[0]) + transcribe(S[1:])

#
# Tests
#
assert transcribe('ACGTTGCA') == 'UGCAACGU'
assert transcribe('ACG TGCA') == 'UGCACGU' # Note that the space disappears
assert transcribe('GATTACA')  == 'CUAAUGU'
assert transcribe('cs5')      == ''        # Note that the other characters disappear
assert transcribe('')         == ''

#print(transcribe('ACGT TGCA'))

def removeAll(e, L):
	"""takes in a list L and an element e 
	(really any data whatsoever). Then, removeAll 
	should return another list that is identical to L 
	except that all elements identical to e have been removed."""

	if L == []:
		return L
	else:
		if e == L[0]:

			M = [L[1]] + removeAll(e, L[2:])
		else:

			M = [L[0]] + removeAll(e, L[1:])
		return M


#print(removeAll(42, [ 35, 77, 42, 11, 42, 88 ]))


def zipper(L, K):
	"""takes in two lists L and K and should output 
	a single list of two-element sublists."""

	if L == [] or K == []:
		return []
	else:
		if L[0] != '' and K[0] != '':
			M = [L[0], K[0]], [zipper(L[1:], K[1:])]
			return M

print(zipper([1,2], ['a','b','c']))

#should return [ [1,'a'], [2,'b'] ]

def listOfWords(words):
	"""takes as input a string S and should return a list of the "words" in S."""
	#remove any space before a word
	while len(words) != 0 and (words[0] == ' '):
		#chomp through a character since it is a space
		words = words[1:]
	#the base case
	if len(words) == 0:
		return []
	temp_word = ''
	#as long as we are not at the end of words and we are not at a space
	while len(words) != 0 and (words[0] != ' '):
		#populate our temp word with characters until there is a space
		temp_word = temp_word + words[0]
		#chomp to the next character
		words = words[1:]
	#now we have a word, so place it in the output variable
	output = [temp_word]
	#run the recursion
	output.extend(listOfWords(words))
	return output


#print(listOfWords('bond. james bond'))








#Should return [ 'Bond.', 'James', 'Bond' ]
#but doesn't

#Word = 'Bond'

#List = [Word[0] + Word[1]]
#print(List)


