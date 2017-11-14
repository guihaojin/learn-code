ab={'father':'guihaojin','mother':'liqian','daughter':'Ace'}
print "father's name is %s"%ab['father']
ab['son']='Ambda'
print ab
del ab['son']
print ab
print 'there are %d people in my family'%len(ab)
for a, b in ab.items():
    print "%s's name is %s"%(a,b)
if 'son' in ab:
    print "son's name is %s"%ab['son']
