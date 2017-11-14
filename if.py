number=50
guess = int(raw_input('Enter an integer : '))
if guess == number:
   print 'you get it'
elif guess >= number:
   print "it's a little bit higher"
else:
    print "it's a little bit smaller"
print "done"

if True:
    print "you are right"