#LetterCodeLogic module by....
#"business" object class for LetterCode operations...

class LCL:
    """Encode/Decode Functions"""
    #Integers
    @staticmethod
    def Decode(msg):
        #seperate numbers from msg string (e.g., "1,2,3")
        nums = msg.split(",") #produces list of separate items
        result= ""
        for x in nums:
            try:
                n = int(x.strip()) #remove leading/trailing spaces
                if n == 0:
                     c = " "
                elif n < 0 or n > 26:
                     c = "?"
                else:
                     #ASCII Scheme has A=65, B=66, etc.
                     c = chr(n+64)
            except ValueError:
                c = "?"
                
            result += c

        return result
    #Strings
    @staticmethod
    def Encode(msg):
        result = ""
        m = msg.upper()
        for i in range(0,len(m)):
            x = ord(m[i])
            if x == 32: # 32 ASCII Space
                x = 0
            else:
                x = x - 64
                if x < 1 or x > 26:
                    x = 99
            result = result + str(x) + " "
        return result
        
            

           
                
                
                
                
    

            
        
       
    
