# Remove Alphabet

def Remove():
    fr = open('Sample.txt', 'r')
    data = fr.read()
    fr.close()

    print("Original Text:", data)

    remove_words = [' a ', ' an ', ' the ', ' A ', ' An ', ' The ', 
        'a ', 'an ', 'the ', 'A ', 'An ', 'The ',       
        ' a', ' an', ' the', ' A', ' An', ' The']
    
    for word in remove_words:
        data = data.replace(word, ' ')  

    
    fw = open('Sample1.txt', 'w')
    fw.write(data)
    fw.close()

    print("Modified Text Written to Sample1.xt")

Remove()
