class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Creates a dictionary to map symbols to values
        symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        #Initialize the total value to 0
        total = 0
        #Iterates through the string
        for i in range(len(s)):
            #Checks if the current symbol is smaller than the next one
            if i < len(s) - 1 and symbol[s[i]] < symbol[s[i+1]]:
                #Subtractes it value
                total -= symbol[s[i]]
            #Checks if the current symbol is greater or equals to the next one
            else:
                #Adds it values
                total += symbol[s[i]]
        return total
