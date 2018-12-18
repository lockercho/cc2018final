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
			time = line[25:35]
			labels = line[36:].strip()
			print(time)
			print(labels)
			joke_id, other = labels.split(':')
			img_id, name = other.split(', ')
			print(time, joke_id, img_id, name)
			all_labels.append((time, joke_id, img_id, name))
			wf.write("%s,%s,%s,%s\n" % (time, joke_id, img_id, name))
