#PyParagraph Homework
import os
import re

filepath = os.path.join("Resources","paragraph_2.txt")


letter_count = 0



with open(filepath, 'r') as text:
    fileinput = text.read() 

    words = fileinput.split()

    word_count = (len(words))

    # sentences = re.split("(?<=[.!?]) +", fileinput)
    # print(sentences)

    # sentence_count = len(sentences)
    
    sentence_count = fileinput.count('.') 

    for letter in fileinput:
        if letter.isalnum():
            letter_count += 1


    average_letter_count = round(letter_count/word_count, 1)

    average_sentence_length = round(word_count/sentence_count, 1)
    
    #Print results to the screen
    print("Paragraph Analysis")
    print("------------------")
    print(f"Approximate Word Count: {word_count}")
    print(f"Approximate Sentence Count: {sentence_count}")
    print(f"Average Letter Count: {average_letter_count}")
    print(f"Average Sentence Length: {average_sentence_length}")

    #Print results to a text file
output_file = os.path.join("Analysis","Paragraph2_data.txt")

with open(output_file, 'w') as textfile:
    
    textfile.writelines(f'Paragraph Analysis \n------------------- \nApproximate Word Count: {word_count} \nApproximate Sentence Count: {sentence_count} \nAverage Letter Count: {average_letter_count} \nAverage Sentence Length: {average_sentence_length}') 
    
    
        
    

    