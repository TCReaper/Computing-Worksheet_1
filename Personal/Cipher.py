
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ALPHABET = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
punctuation = [' ',':',',','.','/','\'',']','[',';','-','_','=','+','~','`',
               '|','!','@','#','$','%','^','&','*','(',')']

import pyperclip
global sentence
global temp
global TEMP


def get_letters():
      input_letter = "A"
      while input_letter != "x":
            ALPHABET.append(input_letter)
            input_letter = input("Letter: ")

def ciphermenu():
      print(("#"*80+"\n\n"))
      sentence = None
      options = [None,atbash,caesar,keyword,unicode,binary,hexadecimal]
      print("Cipher Options:")
      for i in options:
            if i == None:
                  pass
            else:
                  print("\t "+str(options.index(i))+".  "+str(i))
      ciphering = True
      print('\n')
      while ciphering:
            ciph3r = options[int(input("Choose a cipher (INT):  "))]
            print(ciph3r(sentence))

            
#################         FUNCTIONS         ############################

def copycodeindented():

      def samplefunction(sentence = None):
            global alphabet
            global ALPHABET
            global punctuation
            if sentence == None:
                  sentence = input("Sentence to encrypt:    ")
            output = ""
            
            pyperclip.copy(output)
            return output

def hexadecimal(sentence = None):
      global alphabet
      global ALPHABET
      global punctuation
      if sentence == None:
            sentence = input("Sentence to encrypt:    ")
      output = ""
      #help
      pyperclip.copy(output)
      return output

def binary(sentence = None):
      global alphabet
      global ALPHABET
      global punctuation
      if sentence == None:
            sentence = input("Sentence to encrypt:    ")
      output = ""
      for i in sentence:
            output += str(bin( ord( i ) )[2:])
            output += ' '
      pyperclip.copy(output)
      return output

def unicode(sentence = None):
      global alphabet
      global ALPHABET
      global punctuation
      if sentence == None:
            sentence = input("Sentence to encrypt:    ")
      output = ""
      for i in sentence:
            output += str(ord(i))
            output += ' '
      pyperclip.copy(output)
      return output
            
def atbash(sentence = None):
      global alphabet
      global ALPHABET
      global punctuation
      if sentence == None:
            sentence = input("Sentence to encrypt:    ")
      output = ""
      for letter in sentence:
            if letter in punctuation:
                  pass
            elif letter in alphabet:
                  letter_index = alphabet.index(letter)
                  letter = alphabet[25 - letter_index]
            elif letter in ALPHABET:
                  letter_index = ALPHABET.index(letter)
                  letter = ALPHABET[25 - letter_index]
            output += letter
      pyperclip.copy(output)
      return output

def caesar(sentence = None):
      global alphabet
      global ALPHABET
      global punctuation
      if sentence == None:
            sentence = input("Sentence to encrypt:  ")
      shift_value = int(input("\nShift Value:  "))
      output = ""
      for letter in sentence:
            if letter in punctuation:
                  pass
            elif letter in alphabet:
                  index = alphabet.index(letter) + shift_value
                  if index > 25:
                        index -= 26
                  letter = alphabet[index]
            elif letter in ALPHABET:
                  index = ALPHABET.index(letter) + shift_value
                  if index > 25:
                        index -= 26
                  letter = ALPHABET[index]
            output += letter
      pyperclip.copy(output)
      return output

def keyword(sentence = None):
      global alphabet
      global ALPHABET
      global punctuation
      global temp
      global TEMP
      if sentence == None:
            sentence = input("Sentence to encrypt:    ")
      keyword = input("Keyword Encryption:  ")
      used = []
      counter = 0
      counter2 = 0
      temp = alphabet
      TEMP = ALPHABET
      for i in keyword:
            i = i.lower()
            if i in used:
                  pass
            elif i in alphabet:
                  index = temp.index(i)
                  temp = temp[:counter]+[i]+temp[counter:index]+temp[index+1:]
                  counter += 1
                  used.append(i)
                  i = i.upper()
                  index = TEMP.index(i)
                  TEMP = TEMP[:counter2]+[i]+TEMP[counter2:index]+TEMP[index+1:]
                  counter2 += 1
      output = ""
      for letter in sentence:
            if letter in punctuation:
                  pass
            elif letter in temp:
                  index = alphabet.index(letter)
                  letter = temp[index]
            elif letter in TEMP:
                  index = ALPHABET.index(letter)
                  letter = TEMP[index]
            output += letter
      pyperclip.copy(output)
      return output

ciphermenu()

            
