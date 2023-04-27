word_1 = input("enter the word 1:")
word_2 = input("enter the word 2:")
word_3 = input("enter the word 3:")
word_4 = input("enter the word 4:")

list_of_words = [word_1,word_2,word_3,word_4]
print("length of word_1:",len(word_1))
print("length of word_2:",len(word_2))
print("length of word_3:",len(word_3))
print("length of word_4:",len(word_4))
maxlengthword =max(list_of_words,key=len)
print("LONGEST WORD IS: ",maxlengthword)