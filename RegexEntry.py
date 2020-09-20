import time
import sys
from Console import displayOutputs
class RegexEntry:
    Pattern = '' 
    InputString = ''
    OutputString = ''
    indices = []
    def SetInputs(self,  pattern , inputString) : 
        self.OutputString = ''
        self.Pattern = pattern
        self.InputString = inputString
        self.FindRegex()
    
    def AdvFindDot( self , lineId , input , pattern) : 
        patternLenght = len(pattern) 
        
        if (len(input) < patternLenght):
            return
        
        j = 0 
        for i in range (0 , len(input) ) :
            if  (input[i] == pattern[j] ) or pattern[j] == '.': 
                j+=1
                if(j == patternLenght): 
                    self.indices.append([lineId ,  i - patternLenght + 1 , i])
                    j = 0 
        
    def FindRegex(self):
        # print('Pattern is : ' + self.Pattern + '\n')
        # print('Input String is : ' + self.InputString + '\n')

        if self.Pattern == '':
            raise Exception("Invalid pattern, please try again.")
        if self.InputString == '':
            raise Exception("Invalid InputString, please try again.")

        lineId = 0  
        self.indices = []
        for line in self.InputString.splitlines() :
            print(line)

            # . and * operations are not supported at the same time
            if ( self.Pattern.find('.') != -1) and (self.Pattern.find('*') != -1 ):
                raise Exception(". and * are not supported at the same time, please try again.")

            # # if there was no special character 
            # elif (self.Pattern.find('.') == -1) and (self.Pattern.find('*') == -1):
            #     while line.find(self.Pattern) != -1 : 
            #         self.indices.append( [lineId , line.find(self.Pattern) , line.find(self.Pattern) + patternLength] )
            #         line = line [line.find (self.Pattern) + patternLength + 1 :] 
            elif (self.Pattern.find('*') == -1):
                self.AdvFindDot(lineId , line  , self.Pattern)

            lineId += 1

        displayOutputs(self.indices)
        print( self.indices )


    
