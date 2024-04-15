#function to form the string to a list
def list_maker(any_world):
    word_list=[]
    for letter in any_word:
            word_list.append(letter)
    return word_list
#asking for a word.
any_word=input("Please add a string")
word_list=list_maker(any_word)
#making the list to the desired form(1uppercase 1 lowercase)
for i in range(len(word_list)):
    if i%2==0:
        word_list[i]=word_list[i].upper()
#Transforming the list back to a string.
transformed_word="".join(word_list)
#first part is end here
#Spliting the string into a list
sec_list=any_word.split()
for i in range(len(sec_list)):
    if i%2==0:
        sec_list[i]=sec_list[i].upper()
#make a string from the list.
second_transformedword=" ".join(sec_list)
#part1:
print(transformed_word)
#part2:
print(second_transformedword)