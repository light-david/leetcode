#Creates a class called Solution and takes one argument
class Solution(object):
    #Defines searchMartix and takes three arguments
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #Creates an empty list
        digit = []
        #Loops through the matrix
        for digit in matrix:
            #Loops through digit
            for i in digit:
                #Checks if target is in digit
                if i == target:
                    return True
            #Return False if target is not in digit
            return False
