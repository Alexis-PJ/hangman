

word ="llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch"
secret_word = list(word)
new_word = ['*' for i in range(len(secret_word))]
penalty = 0
letters_used = []
while '*' in new_word and penalty < 7:
    guess = input('enter a letter\n')
    if guess not in secret_word or guess in letters_used:
        penalty += 1
    else:
        for i in range(len(secret_word)):
            if guess == secret_word[i]:
                new_word[i] = secret_word[i]
    letters_used.append(guess)
    print(letters_used)
    print('penalty',penalty)
    print(new_word)