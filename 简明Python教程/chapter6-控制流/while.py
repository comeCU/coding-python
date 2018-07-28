# filename : while.py
# 猜数字游戏

number = 23
running = True

while running:
    guess = int(input('Enter a number:'))

    if guess == number:
        print('Congratulations, you guessed it.')
        running = False #猜中，结束while循环
    elif guess < number:
        print('No, it is a little highter than that')
    else:
        print('No, it is a little lower tan that')

else:
    print('The while loop is over.')

print('Done')
