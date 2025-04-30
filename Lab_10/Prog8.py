def q8():
    f_r = open('sample.txt', 'r')
    data = f_r.read()
    f_r.close()

    print("Original Text:", data)

    remove_words = [
        ' a ', ' an ', ' the ', ' A ', ' An ', ' The ', 
        'a ', 'an ', 'the ', 'A ', 'An ', 'The ',       
        ' a', ' an', ' the', ' A', ' An', ' The'        
    ]
    for word in remove_words:
        data = data.replace(word, ' ')  

    
    fw = open('8_out.txt', 'w')
    fw.write(data)
    fw.close()

    print("Modified Text Written to 8b.txt")

q8()
