number = 50
running = True

while running:
    guess = int(raw_input('Enter an integer : '))
    if guess == number:
        print "you get it"
        running = False
    elif guess > number:
        print "it's a little bit higher"
    else:
        print "it's a little bit lower"
else:
    print 'game over'
print "done"