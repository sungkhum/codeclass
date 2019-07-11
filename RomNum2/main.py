import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.text import LabelBase


LabelBase.register(name = "NatoSans",
    fn_regular = "Arimo-BoldItalic.ttf"
    )
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

#
# Decimal to Roman Numeral Converter
# 
# by Nathan Wells
#

def decToRoman(number):

    romanNumeral = ''

    ConvertDictionary = {
        3000000000000000000: 'S̅̅S̅̅S̅̅',
        2000000000000000000: 'S̅̅S̅̅',
        1000000000000000000: 'S̅̅',
        900000000000000000: 'G̅̅S̅̅',
        800000000000000000: 'F̅̅G̅̅G̅̅G̅̅',
        700000000000000000: 'F̅̅G̅̅G̅̅',
        600000000000000000: 'F̅̅G̅̅',
        500000000000000000: 'F̅̅',
        400000000000000000: 'G̅̅F̅̅',
        300000000000000000: 'G̅̅G̅̅G̅̅',
        200000000000000000: 'G̅̅G̅̅',
        100000000000000000: 'G̅̅',
        90000000000000000: 'H̅̅G̅̅',
        80000000000000000: 'P̅̅H̅̅H̅̅H̅̅',
        70000000000000000: 'P̅̅H̅̅H̅̅',
        60000000000000000: 'P̅̅H̅̅',
        50000000000000000: 'P̅̅',
        40000000000000000: 'H̅̅P̅̅',
        30000000000000000: 'H̅̅H̅̅H̅̅',
        20000000000000000: 'H̅̅H̅̅',
        10000000000000000: 'H̅̅',
        9000000000000000: 'M̅̅H̅̅',
        8000000000000000: 'N̅̅M̅̅M̅̅M̅̅',
        7000000000000000: 'N̅̅M̅̅M̅̅',
        6000000000000000: 'N̅̅M̅̅',
        5000000000000000: 'N̅̅',
        4000000000000000: 'M̅̅N̅̅',
        3000000000000000: 'M̅̅M̅̅M̅̅',
        2000000000000000: 'M̅̅M̅̅',
        1000000000000000: 'M̅̅',
        900000000000000: 'C̅̅M̅̅',
        800000000000000: 'D̅̅C̅̅C̅̅C̅̅',
        700000000000000: 'D̅̅C̅̅C̅̅',
        600000000000000: 'D̅̅C̅̅',
        500000000000000: 'D̅̅',
        400000000000000: 'C̅̅D̅̅',
        300000000000000: 'C̅̅C̅̅C̅̅',
        200000000000000: 'C̅̅C̅̅',
        100000000000000: 'C̅̅',
        90000000000000: 'X̅̅C̅̅',
        80000000000000: 'L̅̅X̅̅X̅̅X̅̅',
        70000000000000: 'L̅̅X̅̅X̅̅',
        60000000000000: 'L̅̅X̅̅',
        50000000000000: 'L̅̅',
        40000000000000: 'X̅̅L̅̅',
        30000000000000: 'X̅̅X̅̅X̅̅',
        20000000000000: 'X̅̅X̅̅',
        10000000000000: 'X̅̅',
        9000000000000: 'I̅̅X̅̅',
        8000000000000: 'V̅̅I̅̅I̅̅I̅̅',
        7000000000000: 'V̅̅I̅̅I̅̅',
        6000000000000: 'V̅̅I̅̅',
        5000000000000: 'V̅̅',
        4000000000000: 'I̅̅V̅̅',
        3000000000000: 'S̅S̅S̅',
        2000000000000: 'S̅S̅',
        1000000000000: 'S̅',
        900000000000: 'G̅S̅',
        800000000000: 'F̅G̅G̅G̅',
        700000000000: 'F̅G̅G̅',
        600000000000: 'F̅G̅',
        500000000000: 'F̅',
        400000000000: 'G̅F̅',
        300000000000: 'G̅G̅G̅',
        200000000000: 'G̅G̅',
        100000000000: 'G̅',
        90000000000: 'H̅G̅',
        50000000000: 'P̅',
        40000000000: 'H̅P̅',
        10000000000: 'H̅',
        9000000000: 'M̅H̅',
        5000000000: 'N̅',
        4000000000: 'M̅N̅',
        1000000000: 'M̅',
        900000000: 'C̅M̅',
        800000000: 'D̅C̅C̅C̅',
        700000000: 'D̅C̅C̅',
        600000000: 'D̅C̅',
        500000000: 'D̅',
        400000000: 'C̅D̅',
        100000000: 'C̅',
        90000000: 'X̅C̅',
        50000000: 'L̅',
        40000000: 'X̅L̅',
        10000000: 'X̅',
        9000000: 'I̅X̅',
        5000000: 'V̅',
        4000000: 'I̅V̅',
        1000000: 'S',
        900000: 'GS',
        500000: 'F',
        400000: 'GF',
        100000: 'G',
        90000: 'HG',
        50000: 'P',
        40000: 'HP',
        10000: 'H',
        9000: 'MH',
        5000: 'N',
        4000: 'MN',
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }


    while number > 0:
        for x in ConvertDictionary:
            if number >= x:
                while number >= x:
                    romanNumeral = romanNumeral + ConvertDictionary[x]
                    number = number - x
    return romanNumeral



class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text="Enter Number: ",  font_name="NatoSans"))
        self.name = TextInput(multiline=False,  font_name="NatoSans", font_size="30")
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Roman Numeral: ", font_name="NatoSans"))
        self.lastName = TextInput(multiline=True,  font_name="NatoSans", font_size="30")
        self.inside.add_widget(self.lastName)

        self.inside.add_widget(Label(text="Number in Words: ", font_name="NatoSans"))
        self.email = TextInput(multiline=True,  font_name="NatoSans", font_size="30")
        self.inside.add_widget(self.email)

        self.add_widget(self.inside)

        self.submit = Button(text="Submit", font_name="NatoSans", font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self, instance):
        name = self.name.text
        last = self.lastName.text
        email = self.email.text
        if name.isdigit():
            self.lastName.text = decToRoman(int(name))
            
            #self.name.text = ""
            #self.lastName.text = ""
            self.email.text = numToWord(int(name))
        else:
            self.name.text = "Please enter a number."

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()