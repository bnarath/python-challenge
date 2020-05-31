import os
import re

#change the working directory to the location of this file
os.chdir(os.path.dirname(os.path.abspath(__file__)))


with open('Resources/sample.txt') as file:

    reader = file.read()
    
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
    #This would contain sentences with . at the end
    sentence_count = len(sentences)
    

    #Sentence Length:- Total no of words
    sentence_length = [len(sentence.split()) for sentence in sentences]
    
    avg_sentence_length = sum(sentence_length)/len(sentence_length)
    

    #Word Count
    #Logic
    #Words are separated by one or more \s
    #Please not that, frock-coat is a word not two words
    words = re.split("\s+", reader)
    word_count = len(words)
    

    #Letter count:- Letter count in words
    letter_count = [len(word) for word in words]
    avg_letter_count = sum(letter_count)/len(letter_count)
    

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


    
    


