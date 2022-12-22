'''
This class contains functions that compute values, the binomial coefficients,
that are found in pascal's triangle from 3 different functions.  
'''
class binomial_coefficients: 
    '''
    The get_n function takes an input, n, that will return all the binomial coefficients of row n.  There is already a 
    function that calculates a specific value in a row(get_nk()), so it's best to iterate through all of the values in 
    row n up until the length of the whole row.  Each value in that row gets turned into a string and is added to an empty 
    string, nk_values, which is returned at the end of the for loop.  The values are originally integers and must be turned 
    to string type to be added to an empty string.  
    '''
    def get_n(self,n):
        nk_values = ''
        for k in range(n+1): #iterate into the row until the end of the row
            nk = str(self.get_nk(n,k))
            nk_values += nk + ' ' #space added after each number to shape the triangle
        return nk_values
    
    def get_nk(self,n,k):
        '''
        This function returns the value of the nth row and kth value within that row. n and k start at 0 due to python 
        syntax.  When it comes to recursion, the golden rules are to return 1 or 0 if the n and k inputs apply to what 
        is inside the if statement.  If not, the return statement at the bottom of the function is run.  When the inputs
        do not apply to either if statement, they are taken through the recursive return statement where the n and k 
        input values change(the return statements calls it's own function twice for (n-1,k-1) and (n-1,k)), and run until 
        those values are applicable to the if statements.  The sum of the two calls are then returned to get the 
        binomial coefficient at column k in row n.    
        '''
        #conditional golden rules
        if (n == 0) & (k == 0):
            return 1

        if (n < k) | (k < 0):
            return 0

        return self.get_nk(n-1,k-1) + self.get_nk(n-1,k) #recursive formula

    def print_pt(self,n):
        '''
        This function is focused on formatting of the triangle.  The other funtions already calculate the values, and each
        row of values are appended to a list separated by rows. Iteration happens through that list and returns each list 
        value in a new line until it reaches row n, the value taken as input.  To make the output look more like an 
        equilateral triangle, the length of spaces/characters from the last row is taken, and all the previous rows are 
        centered in the middle of the last row.
        '''
        triangle = [self.get_n(i) for i in range(n+1)] 
        center_len = len(triangle[-1]) #length of characters/spaces for the last row
        out_triangle = ''
        for i in triangle:
            out_triangle += i.center(center_len) + '\n' #centering each row
        return out_triangle