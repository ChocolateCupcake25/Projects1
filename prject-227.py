import json
import csv

data_from_csv=[]
with open('data_set.txt', 'r') as f:
	data_from_txt = json.loads(f.read())

	field_names = ['brake','hand_brake',"throttle",'steer']
	csv_file_store = open('Project_227.csv','w',newline="")
	writer=csv.DictWriter(csv_file_store, fieldnames=field_names)
	writer.writeheader()
	writer.writerows(data_from_txt)

with open('Project_227.csv','r') as file:
	reader = csv.reader(file)
	for row in reader:
		data_from_csv.append(row)

print(data_from_csv)
