
import random 
rte_train = open('/data1/data/hansongbo/parikh_snli-master/RTE7_train.txt','r')

new_rte_train = open('/data1/data/hansongbo/parikh_snli-master/RTE7_train_add.txt','w')


lines = rte_train.readlines()
length = len(lines)
i = 0

data = []

while i < length:
	tag = lines[i+2].strip()
	if tag == 'Y':
		for j in range(16):
			pairs = []
			pairs.append(lines[i])
			pairs.append(lines[i+1])
			pairs.append(lines[i+2])
			data.append(pairs)
	else:
		pairs = []
		pairs.append(lines[i])
		pairs.append(lines[i+1])
		pairs.append(lines[i+2])
		data.append(pairs)

	i += 3

random.shuffle(data)

i = 0
for pairs in data:
	new_rte_train.write(pairs[0])
	new_rte_train.write(pairs[1])
	new_rte_train.write(pairs[2])

rte_train.close()
new_rte_train.close()	
