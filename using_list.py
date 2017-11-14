qqlist = ['haojin','tiantian','ace']
print "There are", len(qqlist), 'people in my family'
#print 'These people are',
#for item in qqlist:
   # print item,
#print
print 'These people are',qqlist[0],qqlist[1],'and',qqlist[2]
print '\nWe also want to have another baby'
qqlist.append('unknown')
print 'These people are',qqlist
qqlist.sort()
print 'Sorted family list is', qqlist
print 'the first priority of our family is', qqlist[0]
del qqlist[3]
print 'Currently, these people are', qqlist
