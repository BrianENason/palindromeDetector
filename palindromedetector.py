################################################################################
# Initialization(s)
#  1) runTests = 
#    When set to True, it will iterate through the testList below
#    When set to False, it will call for the user to enter a string
################################################################################

runTests = False

################################################################################
# Special List(s)
#  1) specialCharacter - This list is populated with common punctuation for the program to ignore
#  2) testList - A list of special words/sentences as test cases
#  3) testDict - A Dictionary of words/phrases to test with their expected outcome as the value
################################################################################

specialCharacter = [' ', ',', '.', '-', '!', '\'', '\"', '@', '#', '$', '%', ';', ':']

testList = ["what!", "Racecar!", "raceCar", " rise to vote, sir", "goog", "", 
            "         ", "tattarrattat", "Madam, in Eden, I'm Adam", "12321", 
            "1A2b3C3B2a1", "too hot to hoot!", "tO oHoTt o,HoOt!", " 1 2,3.4-5!6@5#4$3%2;1:"]

testDict = {"what!":False, "Racecar!":True, "raceCar":True, " rise to vote, sir":True, 
            "goog":True, "":False, "         ":False, "tattarrattat":True, 
            "Madam, in Eden, I'm Adam":True, "12321":True, "1A2b3C3B2a1":True, 
            "too hot to hoot!":True, "tO oHoTt o,HoOt!":True, " 1 2,3.4-5!6@5#4$3%2;1:":True}

################################################################################
# Output Format Function(s)
#  1) printDivider - When called, it prints a standard divider between entries
#  2) printSeparator - When called, it prints a standard separator between entries
#  3) outputToUser - provides a standard way to output each of the 3 possible cases:
#    a. Word IS a palindrome
#    b. Word is NOT a palindrome
#    c. Word is not valid for analysis
################################################################################

def printDivider():  
  print('\n/', ('-' * 80), '/')

def printSeparator():  
  print('\n', ('~' * 40))

def outputToUser(word, isAPal):  
  printDivider()  
  print("\nYour word: \"{}\" {} a palindrome".format(word, isAPal))  

################################################################################
# Main Logic Function(s)
#  1) clearSpecialChar - This will clear any whitespace and/or special characters from the string before analysis
#  2) checkForPal - This is the main logic to see if the now cleaned word can be considered a palindrome
################################################################################

def clearSpecialChar(word):
  newWord = word.strip(' ')  # Remove any leading or trailing whitespace  
  newWord = newWord.lower()
  for sc in newWord:
    if (sc in(specialCharacter)):
      newWord = newWord.replace(sc, "")        
  return newWord

def checkForPal (cleanString):
  i = 0  
  k = (len(cleanString) - 1)
  while (k > i):
    if(cleanString[k] == cleanString[i]):
      k -= 1
      i += 1
    else:
      return False
  return True

################################################################################
# Progressive Function(s) - 
# NOTE: These functions show the sequence of events for verifying if a word is or is not a palindrome.
#  1) fullPalindromeCheck - This will run through the subsequent sequences to check and verify that the word/phrase is or is not a palindrome by cycling through the other 2 functions
#  2) newPalindromeCheck - This will first ensure that the user entered an actual word/phrase before performing the logic checks
#  3) nextPalindromeCheck - If the word/phrase passes through the first check, this will send it to main palindrome checking function in the main logic
################################################################################

def fullPalindromeCheck(word):
  blankWord = firstPalindromeCheck(word)
  if not blankWord:
    outputToUser(word, "is not a valid word, and therefore is NOT")
  else:    
    palindromeWord = nextPalindromeCheck(blankWord)
    if not palindromeWord:
      outputToUser(word, "is NOT")
    else:
      outputToUser(word, "is")

def firstPalindromeCheck(word):
  isBlank = clearSpecialChar(word)
  return isBlank

def nextPalindromeCheck(word):
  possiblePalindrome = checkForPal(word)
  return possiblePalindrome

################################################################################
# Test Function(s)
#  1) runTest() - This will iterate through the test list of words and pass them through the full palindrome check
#  2) runDictTest() - This will use the testDict to pass the keys (word/phrase to test) and make sure the expected answer (value) is returned
################################################################################

def runListTest():
  for word in testList:    
    fullPalindromeCheck(word)

def runDictTest():
  for word in testDict:
    fullPalindromeCheck(word)
    printSeparator()
    print("\nThe correct answer is {}".format(testDict[word]))

################################################################################
# Program Main
################################################################################

def main():
  if (runTests == True):
    # runListTest()  # Old form of test using a list of values
    runDictTest()
  else:
    userWord = input("Please enter a word to check: ")
    # palindromeCheck(userWord)
    fullPalindromeCheck(userWord)

if __name__ == "__main__":
  main()
