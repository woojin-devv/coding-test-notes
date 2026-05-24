word1 = input()
word2 = input()

# Please write your code here.
def func(word1, word2):
    word1 = list(word1)
    word1.sort()
    word2 = list(word2)
    word2.sort()
    result = ""
    
    if word1 == word2 :
        result = "Yes"
        return result
    else:
        result = "No"
        return result

print(func(word1, word2))