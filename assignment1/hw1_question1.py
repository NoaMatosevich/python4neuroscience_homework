def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    length=len(word)
    
    count=0
    for i in range(1,length):
        if word[i]==word[i-1]:
            count=count+1
            for n in range(i+2,length,2):
                if word[n]==word[n-1]:
                    count=count+1
                elif count<3:
                    count=0
            if count>=3:
                return True            
            
    return False
     
if __name__=='__main__':
    #Question 1
    test_words=['aabbcc','abccddee0123','llkkbmm','aaaazz','bbcCdd','','abbddcc','aabccddeefgghhiii']
    for test in test_words:
        trif=trifeca(test)
        print(f"Question 1 solution {test}: {trif}")
        
