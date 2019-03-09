def trifeca(word):
    """
    Checks whether word contains three consecutive double-letter pairs.
    word: string
    returns: bool
    """
    length=len(word)
    if length==0:
        return False
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
            
    if count>=3:
        return True
    else:
        return False
     
if __name__==__'main':
    
    word1='aabbcc'
    word2='abccddee0123'
    word3='llkkbmm'
    word4='aaaazz'
    word5='bbcCdd'
    word6=''
    trif=trifeca(word6)
    print(f"Question 1 solution: {trif}")
        