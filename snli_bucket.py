
'''
To help speed things up, 
I had semi-sorted the training data so that examples were both sentences of length < 20 were first, then < 50, and then < 80  
(i had intended this just for efficiency reasons, but it may boost performance a bit)
'''

# set 3 bucket

bucketA = [] 
bucketB = []
bucketC = []
buckedD = []

f1 = open('/data1/data/hansongbo/parikh_snli-master/snli_1.0/snli_1.0_train.txt','r')
f2 = open('/data1/data/hansongbo/parikh_snli-master/snli_1.0/snli_1.0_dev.txt','r')
f3 = open('/data1/data/hansongbo/parikh_snli-master/snli_1.0/snli_1.0_test.txt','r')

f1_sorted = open('/data1/data/hansongbo/parikh_snli-master/snli_1.0/snli_1.0_train_sorted.txt','w')
f2_sorted = open('/data1/data/hansongbo/parikh_snli-master/snli_1.0/snli_1.0_dev_sorted.txt','w')
f3_sorted = open('/data1/data/hansongbo/parikh_snli-master/snli_1.0/snli_1.0_test_sorted.txt','w')

fs = [(f1,f1_sorted),(f2,f2_sorted),(f3,f3_sorted)]

#sorted
for f,fsorted in fs:
    
    print 'process %s file...'% f.name
    
    filehead = f.readline() #strip head line
    fsorted.write(filehead)
    for line in f.readlines():
        line_s = line.split('\t')
        s1 = filter(lambda x:x!='(' and x!=')',line_s[1].split(' '))
        s2 = filter(lambda x:x!='(' and x!=')',line_s[2].split(' '))
        
        if len(s1)<20 and len(s2)<20:
            bucketA.append(line)
        elif len(s1)<50 and len(s2)<50:
            bucketB.append(line)
        elif len(s1)<80 and len(s2)<80:
            bucketC.append(line)
        else:
            buckedD.append(line)
    
    for bucket in [bucketA,bucketB,bucketC,buckedD]:
        for line in bucket:
            #print line
            fsorted.write(line)
    
    f.close()
    fsorted.close()
    
print "finished"

