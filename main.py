import random
from random import randint

def whole(approval):

    lst=['clothes-what you wear','parents-Who gives you birth','pirate-Who owns the ocean','ship-Travels in water','places-Where you travel','apple-Fruit mainly found in Kashmir',"computer-Today's weapon"]
    word=random.choice(lst)
    complete=word.split('-')
    obj=complete[0]
    desc=complete[1]

    def shuffle(obj):
        n = len(obj)
        li = list(obj)
        for i in range(0,n-1):
            pos = randint(i+1,n-1)
            li[pos],li[i] = li[i],li[pos]
        res = ""
        for i in range(n):
            res = res + li[i]
        return res+' - '+ desc
    print(shuffle(obj))
    user=input('Guess the word- \n')
    while user==obj:
        print('Hurray! You got it right.\n')
        break
    else:
        print('You lost!\nCorrect word is {}'.format(obj)+'\n')

    a='Do you want to play again?\nY for Yes\nN for No\n'
    print(a)
    approval = input()
    if approval == 'Y' or approval == 'y':
        whole(approval)
    if approval == 'N' or approval == 'n':
        print('Thanks for playing!')
        exit()

lst = ['pirate-Who owns the ocean', 'ship-Travels in water', 'places-Where you travel',
       'apple-Fruit mainly found in Kashmir', "computer-Today's weapon"]
word = random.choice(lst)
complete = word.split('-')
obj = complete[0]
desc = complete[1]


def shuffle(obj):
    n = len(obj)
    li = list(obj)
    for i in range(0, n - 1):
        pos = randint(i + 1, n - 1)
        li[pos], li[i] = li[i], li[pos]
    res = ""
    for i in range(n):
        res = res + li[i]  # sequentially add the charters of the list
        # to the string
    return res + ' - ' + desc


print(shuffle(obj))
user = input('Guess the word- \n')
while user == obj:
    print('Hurray! You got it right.\n')
    break
else:
    print('You lost!\nCorrect word is {}'.format(obj)+'\n')

a = 'Do you want to play again?\nY for Yes\nN for No\n'
print(a)
approval = input()
if approval == 'Y' or approval == 'y':
    whole(approval)
if approval == 'N' or approval == 'n':
    print('Thanks for playing!')
    exit()



