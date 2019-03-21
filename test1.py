import csv
inf1 = r'/home/ubuntu/Desktop/Test_1/sale_info.csv'
inf2 = r'/home/ubuntu/Desktop/Test_1/employee.csv'
outf = r'/home/ubuntu/Desktop/result.csv'
def get_data(path):
	with open(path,'r') as f:
		data = csv.reader(f)
		data = list(data)
	return data
def sort_rows(data_list,key_name,up_down=False):
	title = data_list.pop(0)
	if key_name not in title:
		print('No index in here!')
	else:
		key_index = title.index(key_name)
		new_data = sorted(data_list,key=lambda x:x[key_index],reverse=up_down)
		new_data.insert(0,title)
	return new_data

def select_values(data_list,key_list):
	new_data=[]
	keys_index=[]
	for i in key_list:
		if i in data_list[0]:
			keys_index.append(data_list[0].index(i))
	for i in range(len(data_list)):
		row_data=[]
		for j in range(len(data_list[0])):
			if j in keys_index:
				row_data.append(data_list[i][j])
		new_data.append(row_data)
	return new_data

def select_remove(data_list,key_list):
	new_data=[]
	keys_index=list(range(len(data_list[0])))
	for i in key_list:
		if i in data_list[0]:
			keys_index.remove(data_list[0].index(i))
	for i in range(len(data_list)):
		row_data=[]
		for j in range(len(data_list[0])):
			if j in keys_index:
				row_data.append(data_list[i][j])
		new_data.append(row_data)
	return new_data

def create_dict(inputlist,key_index):
	d={}
	for i in range(len(inputlist)):
		d[inputlist[i][key_index]]=inputlist[i]
	return d
def check_sameword(keylist):
	enu = list(enumerate(keylist))
	for i in keylist:
		if keylist.count(i)>=2:
			samewords = [index for index,value in enu if value==i]
	for i in range(1,len(samewords)):
		keylist[samewords[i]]=keylist[samewords[i]]+"_{}".format(i)
	return keylist
def inner_join(data_list1,data_list2,key):
	join_data=[]
	title1 = data_list1.pop(0)
	title2 = data_list2.pop(0)
	if key in title1 and key in title2:
		key_index1 = title1.index(key)
		key_index2 = title2.index(key)
		d1 = create_dict(data_list1,key_index1)
		d2 = create_dict(data_list2,key_index2)
	if len(data_list1)<=len(data_list2):
		new_title = check_sameword(title1+title2)
		try:
			for i in d1:
				row_data = d1[i]+d2[i]
				join_data.append(row_data)
		except:
			countinue
	else:
		new_title = check_sameword(title2+title1)
		try:
			for i in d2:
				row_data= d2[i]+d1[i]
				join_data.append(row_data)
		except:
			countinue
	join_data.insert(0,new_title)
	return join_data


data1 = get_data(inf1)
data2 = get_data(inf2)
sort_data2 = sort_rows(data2,'Employee_number')
select_data1 = select_values(data1,['Employee_number','sales','profits'])
sort_select_data1 = sort_rows(select_data1,'Employee_number')
data_join = inner_join(sort_data2,sort_select_data1,'Employee_number')
select_rm_data_join = select_remove(data_join,['department','other','Employee_number_1'])
result = sort_rows(select_rm_data_join,'Employee_number')
with open(outf,'w') as csvfile:
	writer = csv.writer(csvfile)
	try:
		for i in range(len(result)):
			writer.writerow(result[i])
	except:
		print('{} row had error!'.format(i+1))




				
				