def summarize(lst):
    string = ''
    for i in range(len(lst)):
        if i == 0:
            string = string + lst[i]
        elif i == len(lst) - 1 :
            string = string + ' and ' + lst[i]
        elif i != len(lst):
            string = string + ', ' + lst[i]
    print(string)
    print(type(string))


#lst = ['apples', 'bananas', 'tofu', 'cats']
summarize(['apples', 'bananas', 'tofu', 'cats'])
