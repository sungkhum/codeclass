#
# Number to Words Converter
# 
# By Nathan Wells
#

def underTwenty(number):
	underTwentyDictionary = {
		19: 'Nineteen',
		18: 'Eighteen',
		17: 'Seventeen',
		16: 'Sixteen',
		15: 'Fifteen',
		14: 'Fourteen',
		13: 'Thirteen',
		12: 'Twelve',
		11: 'Eleven',
		10: 'Ten',
		9: 'Nine',
		8: 'Eight',
		7: 'Seven',
		6: 'Six',
		5: 'Five',
		4: 'Four',
		3: 'Three',
		2: 'Two',
		1: 'One'
	}
	for x in underTwentyDictionary:
		if number == x:
			underTwentyInWords = underTwentyDictionary[x]
	return underTwentyInWords

def theTensPlace(number):
	tensDictionary = {
		9: 'Ninety',
		8: 'Eighty',
		7: 'Seventy',
		6: 'Sixty',
		5: 'Fifty',
		4: 'Forty',
		3: 'Thirty',
		2: 'Twenty',
		1: 'Ten'
	}
	for x in tensDictionary:
		if number == x:
			tensInWords = tensDictionary[x]
	return tensInWords


def numToWord(number):
	numberInWords = ''
	tempNumberInWords = ''
	skip = False
	places = len(str(number))

	#check if number is too large
	if int(places) > 21:
		tooLarge = 'The number you entered is too large.'
		return tooLarge

	placeDictionary = {
		19: '-Quintillion ',
		16: '-Quadrillion ',
		13: '-Trillion ',
		10: '-Billion ',
		7: '-Million ',
		4: '-Thousand ',
		3: '-Hundred and ',
		2: '-',
		1: ''
	}

	#Check where we are if 0 then we are in the hundreds place, 
	# 1 we are in the ones, 2 we are in the tens
	whatPlace = len(str(number)) % 3
	i = 1
	i2 = 1

	if (number) < 20:
		return underTwenty(number)

	#reverse the numbers and make it a string
	number = str(number)[::-1]


	for x in range(len(str(number))):
		
		#if we processed two digits in the last iteration, then skip this digit
		if skip == True:
			skip = False
			i2 += 1
			i +=1
			continue
		
		#check if we are in the ones place that we don't have a number under 
		#twenty and greater than nine
		tensCheck = number[x:x+2]
		tensCheck = tensCheck[::-1]
		tensCheck = int(tensCheck)
		if i2 == 1 and tensCheck < 20 and tensCheck > 9:
			tempNumberInWords = underTwenty(tensCheck)
			#skip the next iteration
			skip = True

			


		#check to make sure we aren't at a zero - if we are skip to the next
		elif int(number[x]) != 0:
			#if we are in the ones place and not at the thousands place
			if i2 == 1:
				tempNumberInWords = underTwenty(int(number[x]))
			#if we are in the tens place
			if i2 == 2:
				tempNumberInWords = theTensPlace(int(number[x]))
			if i2 == 3:
				tempNumberInWords = underTwenty(int(number[x]))

		#if we need to add a place word then add it
		if i in [4, 7, 10, 13, 16, 19]:
			numberInWords = tempNumberInWords + placeDictionary[i] + numberInWords
		#if we are in the hudreds or tens add place word
		elif i2 in [2, 3]:
			numberInWords = tempNumberInWords + placeDictionary[i2] + numberInWords
		else:
			numberInWords = tempNumberInWords + numberInWords




		i += 1
		if i2 == 3:
			i2 = 1
		else:
			i2 += 1
	

	return numberInWords



print(numToWord(1233322232456514))

