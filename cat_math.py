def catPicture():
    print()
    print(' /\\   /\\')
    print('(  o  o )')
    print('  > ^ <  ')
    print()
    return

print('How many cats do you have?')
try:
    numCats = int(input())
    if int(numCats) < 0:
        print('Haha. Nice try.')
        numCats = -numCats
        if numCats == 1:
            print('You now have ' + str(numCats) + ' cat.', end=' ')
        else: 
            print('You now have ' + str(numCats) + ' cats.', end=' ')
    while int(numCats) != 4:
        if int(numCats) < 4:
            print('That is not that many cats.', end=' ')
            print('Do you want another cat? (yes or no)')
            answer = ''
            while answer != 'yes':
                answer = input()
                if answer == 'no':
                    print('Change your mind?')
            if answer == 'yes':
                numCats = numCats + 1
                print('You now have ' + str(numCats) + ' cats.')
        elif int(numCats) > 4:
            print('That is a lot of cats...', end=' ')
            print('Does your mother know? Does she want a cat?')
            response = ''
            while response != 'yes':
                response = str(input())
                if response == 'no':
                    print('Change your mind?')
            if response == 'yes':
                numCats = numCats - 1
                print('You now have ' + str(numCats))
    print('Cat-tacular! Just the right number of cats!', end=' ')
    print('Want a cat picture? (yes or no)')
    if str(input()) == 'yes':
        catPicture()
    elif str(input()) == 'no':
        print('Fine.')
    else:
        print('Huh? I guess not! No cat for you!')
except ValueError:
    print('You did not enter a number.')
print('Bye!')
