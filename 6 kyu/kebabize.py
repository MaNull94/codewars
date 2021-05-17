# https://www.codewars.com/kata/57f8ff867a28db569e000c4a/train/python

# my solution
def kebabize(string):
    #remove digits from string
    tmp = ''.join([char for char in string if not char.isdigit()])

    result = []
    word_start_index = 0
    word_end_index = 0
    for i in range(1, len(tmp)):
        if tmp[i].isupper():
            word_end_index = i
            result.append(tmp[word_start_index:word_end_index])
            word_start_index = i
            print (result)
        if i == len(tmp)-1:
            result.append(tmp[word_start_index:])
    return '-'.join([word.lower() for word in result])

    
# solution from another user
def kebabize(s):
    return ''.join(c if c.islower() else '-' + c.lower() for c in s if c.isalpha()).strip('-')

# another 2
