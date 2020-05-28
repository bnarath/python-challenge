import os
import re

#change the working directory to the location of this file
os.chdir(os.path.dirname(os.path.abspath(__file__)))
#print(os.getcwd())


'''
with open('Resources/PyParagraph_raw_data_paragraph_1.txt') as file1, open('Resources/PyParagraph_raw_data_paragraph_2.txt') as file2:
    for line in file1:
        print(line)

    print("\n")

    for line in file2:
        print(line)
'''


with open('Resources/sample.txt') as file:
    #print(file.read())
    
    reader = file.read()
    #print(reader)

    
    #Sentences :- 
    # Logic
    # We need to select the space(or spaces) wisely with certain conditions and split the paragraph with these spaces
    # Rememeber all spaces do not split a sentence
    # What qualifies such a space
    # 1. Should precede with [.,!]  (?<=[.?!])
    # 2. consider "i.e. " -> exclude such a condition (?<!\w\.\w\.)
    # \w implies [A-Za-z0-9_] 
    # 3. consider Dr. Bernard -> exclude such a condition (?<![A-Z][a-z]\.)
    # A (a chunk of) spaces satifying conditions 1 and 2 and 3, can be represented as (?<!\w\.\w\.)(?<![A-Z][a-z]\.)(?<=[.?!])\s+
    # \s -> space ; + implies one or more
    sentences = re.split("(?<!\w\.\w\.)(?<![A-Z][a-z]\.)(?<=[.?!])\s+", reader)
    #print(sentences)
    #This would contain sentences with . at the end
    sentence_count = len(sentences)
    #print(sentence_count)

    #Sentence Length:- Total no of words
    sentence_length = [len(sentence.split()) for sentence in sentences]
    #print(sentence_length)
    avg_sentence_length = sum(sentence_length)/len(sentence_length)
    #print(avg_sentence_length)

    #Word Count
    #Logic
    #Words are separated by one or more \s
    words = re.split("\s+", reader)
    word_count = len(words)
    #print(word_count)

    #Letter count:- Letter count in words
    letter_count = [len(word) for word in words]
    avg_letter_count = sum(letter_count)/len(letter_count)
    #print(round(avg_letter_count,1))

    '''
    #For future reference
    #This is good enough for word count.
    #However, having .,!, or ? at the end will have some problem on the letter count.
    #Hence, substitude ,.!? at the end of each words by ''
    words = [re.sub('[.!?,]+$','',word) for word in words]
    #This cleans up the words chopping the unnecessary characters at the end
    letter_count = [len(word) for word in words]
    avg_letter_count = sum(letter_count)/len(letter_count)
    print(avg_letter_count)
    '''

    #Make a format string and write it to the file, also display it to the terminal
    content = "Paragraph Analysis\n\
-----------------\n\
Approximate Word Count: {}\n\
Approximate Sentence Count: {}\n\
Average Letter Count: {:.1f}\n\
Average Sentence Length: {:.1f}\n\
".format(word_count, sentence_count, avg_letter_count, avg_sentence_length)
    #Output to the terminal
    print(content)

#Output to the file
with open('analysis/PyParagraph_Analysis.txt', 'w') as output_file:
    output_file.write(content)


    
    


