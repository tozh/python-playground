



def run_length_encode(string):
    if len(string)<=1:
        return str
    letter_dict = {}
    i = 0
    j = 0
    n = len(string)
    while i<n and j<n:
        if string[j] != string[i]:
            letter_dict[string[i]] = j-i
            i = j
        else:
            j+=1
    new_str = []
    for key, value in letter_dict.items():
        new_str.append(key)
        new_str.append(str(value))
    return ''.join(new_str)

a = 'aaaaabbbcdvfffddd'

print(run_length_encode(a))
