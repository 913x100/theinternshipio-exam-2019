import random


def readFile(category):
    lines = [line.strip('\n').split('|')
             for line in open('./'+category+'.txt')]
    question = random.choice(lines)
    return question


def hangman(question):
    word = question[0]
    hint = question[1]
    score = 0
    attemp = 10
    correct = 0
    guess = ""
    ans = ""

    print('')
    print('Hint: {}'.format(hint))

    for letter in word:
        if(letter.isalpha()):
            ans += '_ '
        else:
            ans += letter
    print(ans + "   score " +
                str(score)+", "+"remaining wrong guess " +
                str(attemp))
    while True:
        display = ""
        if (attemp <= 0):
            print("GAME OVER")
            break
        else:
            letter = input().strip().lower()
            attemp = attemp - 1
            if (letter in word and letter not in ans):
                correct = correct + 1
                if (correct == len(word)):
                    print(word)
                    print("Congrulation")
                    break
                score += 5
                for i in range(len(word)):
                    if (letter == word[i]):
                        ans = ans[:2*i] + letter + ans[2*i+1:]

            else:
                guess = guess+letter+" "

            display = ans + "   score " + \
                str(score)+", "+"remaining wrong guess " + \
                str(attemp)+", "+"wrong guessed: "+guess

            print(display)


print("Select Category:")

categories = ["animals", "careers"]
for index, category in enumerate(categories):
    print('{} - {}'.format(index+1, category))

inp = int(input())
question = readFile(categories[inp-1])
hangman(question)
