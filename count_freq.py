from collections import Counter
from collections import defaultdict
import operator

with open("Algorithms_book.txt","r") as myfile:
	data = myfile.read().replace('\n',' ').split(' ')

d1=defaultdict(int)
for words in data:
	d1[words]+=1

#print d1

sorted_d = sorted(d1.items(), key=operator.itemgetter(1),reverse=True)

for i in range(len(sorted_d)):
	print sorted_d[i]
