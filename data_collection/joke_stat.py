# to csv
# [12/18/2018, 2:16:47 PM][1545113807] 109: 2, aaa
import pandas as pd
with open('user_labels', 'r') as f:
	# prepare csv
	columns = ['time', 'joke_id', 'img_id', 'name']
	with open('labels-1218-0717.csv', 'w') as wf:
		wf.write(",".join(columns)+"\n")
	
		for line in f:
			line = line.strip()
			# line = '[12/18/2018, 2:16:47 PM][1545113807] 109: 2, aaa'
			time = line[26:36]
			labels = line[37:].strip()
			print(time)
			print(labels)
			joke_id, other = labels.split(':')
			toks = other.split(',')
			if len(toks) == 2:
				img_id, name = toks[0].strip(), toks[1].strip()
			if len(toks) == 1:
				img_id, name = toks[0].strip(), ''
			print(time, joke_id, img_id, name)
			wf.write("%s,%s,%s,%s\n" % (time, joke_id, img_id, name))
