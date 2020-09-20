import time
import sys
from Console import displayOutputs
class RegexEntry:
    Pattern = '' 
    InputString = ''
    OutputString = ''
    indices = []
    resultNum = 1
    def SetInputs(self,  pattern , inputString) : 
        self.OutputString = ''
        self.Pattern = pattern
        self.InputString = inputString
        self.FindRegex()
    
    # This function finds the regular expression for each single line and saves the indices into a list
    def AdvFindDot( self , lineId , input , pattern) : 
        patternLenght = len(pattern) 
        
        if (len(input) < patternLenght):
            return
        
        # Scan through the line to find the first character of pattern and if successful checks the next character 
        # with the second pattern charactor. special pattern characters have been taken into consideration as well.
        j = 0 
        for i in range (0 , len(input) ) :
            if (input[i] == pattern[j]  or pattern[j] == '.') or (pattern[j] == '*'): 
                if(pattern[j] == '*') : 
                    if input[i] == pattern[j-1]:
                        j+=1
                else :
                    j+=1
                if (j == patternLenght) : 
                    self.indices.append([lineId ,  i - patternLenght + 1 , i])
                    j = 0 

                elif(pattern[j] == '*' and j == patternLenght-1) :
                    if i < len(input) -1 :
                        if(input[i+1] == pattern[j-1]) : 
                            self.indices.append([lineId ,  i - patternLenght + 2 , i+1])
                            j = 0
                        else : 
                            self.indices.append([lineId ,  i - patternLenght + 2 , i])
                            j = 0 
                    else:
                            self.indices.append([lineId ,  i - patternLenght + 2 , i])
                            j = 0 
        
    def FindRegex(self):

        # Check for the edge cases
        if self.Pattern == '':
            raise Exception("Invalid pattern, please try again.")
        if self.InputString == '':
            raise Exception("Invalid InputString, please try again.")

        lineId = 0  
        self.indices = []
        for line in self.InputString.splitlines() :
            # Star character is not valid at the beginning of the pattern 
            if(self.Pattern.find('*') == 0 ):
                raise Exception("Invalid Regular Expression input (* cannot be at the beginning).")
            self.AdvFindDot(lineId , line  , self.Pattern)
            lineId += 1

        displayOutputs(self.indices , self.resultNum)
        print( self.indices )
        self.resultNum+=1