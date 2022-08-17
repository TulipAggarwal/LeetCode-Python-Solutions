class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        
        #giving access to a dictionary to link alphabet set and morse_codes set
        dct = {i:j for i,j in zip(alphabet, morse_codes)}
    
        words_morse = []
        for word in words:
            #Map will access and link them to their morse code
            #''.join will convert it in a string
            words_morse.append(''.join(map(dct.get, list(word))))
        
        #set will convert the code to a set thus eliminating the duplicate elements
        return len(set(words_morse))
