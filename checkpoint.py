def analyze_sentences(sentence):
   
    length = 0
    word_count = 1  
    vowel_count = 0
    
    # Definir the vowels
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    
    
    for char in sentence:
        if char == '.':  
            break
        if char != ' ':  
            length += 1
            if char in vowels:  
                vowel_count += 1
        else:
            word_count += 1  
    
    # Output 
    print(f"Length of sentence: {length}")
    print(f"Number of words: {word_count}")
    print(f"Number of vowels: {vowel_count}")


sentence = input("Enter a sentence ending with a period: ")
analyze_sentences(sentence)
