import os

with open("paragraph_2.txt", "r") as P1:

    #Read text file into one string
    Para_Str = P1.readline()
    P1.close

#Read string into array split by space character
Para_List = Para_Str.split(" ")

#Initialize Variables
Tot_Sent = 0
Tot_Chars = 0

#Calculate total number of words by list length
Tot_Words = len((Para_List))

#loop through word list to find number of periods
#this number should be equal to number of sentences
#THIS CODE ASSUMES THERE ARE NO PERIODS IN ANY PLACE 
#OTHER THAN THE END OF A SENTENCE
for word in Para_List:
    if "." in word:
        Tot_Sent = Tot_Sent + 1

    #totals characters of each word in array    
    Tot_Chars = Tot_Chars + len(word)
    
#Calculate total letter charaters in paragraph by 
#subtracting number of periods (sentences) from total characters
Tot_Chars = Tot_Chars - Tot_Sent

#Calculate average letter count and sentence length
Avg_Letter = round(Tot_Chars/Tot_Words,1)
Avg_Sent = round(Tot_Words/Tot_Sent,1)

#print information
print(f"Paragraph Analysis")
print(f"---------------------------------------")    
print(f"Approximate Word Count: {Tot_Words}")
print(f"Approximate Sentence Count: {Tot_Sent}")
print(f"Average Letter Count: {Avg_Letter}")
print(f"Average Sentence Length: {Avg_Sent}")