# Create a dictionary to store the frequency of each letter in magazine.

# Check to see if each letter in ransomNote can be constructed from magazine.

def canConstruct(self, ransomNote, magazine):
    
        magazine_letters = {}
        
        for letter in magazine:
            if letter in magazine_letters:
              magazine_letters[letter] += 1
            else:
                magazine_letters[letter] = 1
        
        for letter in ransomNote:
            if letter in magazine_letters and magazine_letters[letter] > 0:
                magazine_letters[letter] -= 1
            else:
                return False
            
        return True