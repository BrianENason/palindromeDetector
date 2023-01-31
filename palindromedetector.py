################################################################################
# Initialization(s)
#  1) testRun = 
#    When set to True, it will iterate through the testList below
#    When set to False, it will call for the user to enter a string
################################################################################

testRun = True

################################################################################
# Special List(s)
#  1) specialCharacter - This list is populated with common punctuation for the program to ignore
#  2) testList - A list of special words/sentences as test cases
################################################################################

specialCharacter = [' ', ',', '.', '-', '!', '\'', '\"', '@', '#', '$', '%', ';', ':']
testList = ["what!", "Racecar!", "raceCar", " rise to vote, sir", "goog", "", 
            "         ", "tattarrattat", "Madam, in Eden, I'm Adam", "12321", 
            "1A2b3C3B2a1", "too hot to hoot!", "tO oHoTt o,HoOt!", " 1 2,3.4-5!6@5#4$3%2;1:"]

################################################################################
# Output Format Function(s)
#  1) printDivider - When called, it prints a standard divider between entries
#  2) outputToUser - provides a standard way to output each of the 3 possible cases:
#    a. Word IS a palindrome
#    b. Word is NOT a palindrome
#    c. Word is not valid for analysis
################################################################################

def printDivider():  
  print('/', ('-' * 100), '/')

def outputToUser(word, isAPal):
  printDivider()
  print("\nYour word \n\t\"{}\"\n{} a palindrome\n".format(word, isAPal))

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
  while (k >= i):
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
################################################################################

def runTest():
  for word in testList:
    # palindromeCheck(word)
    fullPalindromeCheck(word)

################################################################################
# Program Main
################################################################################

def main():
  if (testRun == True):
    runTest()
  else:
    userWord = input("Please enter a word to check")
    # palindromeCheck(userWord)
    fullPalindromeCheck(userWord)

if __name__ == "__main__":
  main()
