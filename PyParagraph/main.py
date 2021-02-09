import re
import os
import os.path

sSent = []
sLetter = []
countWord = 0
flag = 0

#ask for name of document and checks if it exists
while flag == 0:
    document = input("What is the documents filename in Resources folder? ")
    if (os.path.exists('Resources/'+document+'.txt')):
        flag = 1
    else: 
        print("File does not exist in Resources folder!")
        

#Find document in Resourcs
paragraph = os.path.join('Resources',document+'.txt')
with open(paragraph, 'r') as para:
    #split by sentences
    sPara = re.split("(?<=[.!?]) +",para.read())
    
#count of sentences
countSen = len(sPara)

#split sentences by word
for sen in sPara:
    sSent.append(re.split("[ (),><=+/%$^#@&*{}]",sen))
for a in sSent:
    #removing all blank caused by (,),>,<, , etc. 
    while '' in a:
        a.remove('')
    #count of word
    countWord += len(a)
    
#average sentence calc
avgSen = countWord/countSen

#letter split
for a in sSent:
    for b in a:
        for c in b:
            sLetter.append(c.split())
#letter count
countLet = len(sLetter)
avgLet = countLet/countWord

#checks if analysis folder exists, else creates one
if (os.path.exists('Analysis')) == False:
    os.mkdir('Analysis')
    
    
#writing analysis
outputFile = os.path.join('Analysis',document+'_results.txt')
spacer = "-----------------\n"
with open(outputFile, 'w', newline = '') as paraFile:
    paraFile.write("Paragraph Analysis\n")
    paraFile.write(spacer)
    paraFile.write(f'Approximate Word Count: {countWord}\n')
    paraFile.write(f'Approximate Sentence Count: {countSen}\n')
    paraFile.write(f'Average Letter Count: {avgLet:.1f}\n')
    paraFile.write(f'Average Sentence Length: {avgSen:.1f}\n')
    
#reads the txt file
with open(outputFile, 'r') as readFile:
    print(readFile.read())

print("Results file successfully generated! Check the Analysis Folder for text file")
