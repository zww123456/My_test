import os
import pandas as pd
from pandas import DataFrame,Series
filepath = r'ad_operation.csv'
old_data = pd.read_csv(filepath,delimiter="\t")

ad_status_value = old_data['ad_status_value']
#print(ad_status_value[:10])

ad_status = {}
pay_money = {}
release_time = {}
people_orientation = {}

for i in range(len(ad_status_value)):
	print(i)
	if ad_status_value[i] is not None:
		if ad_status_value[i].isdigit():
			if int(ad_status_value[i])==0 or int(ad_status_value[i])==1:
				ad_status[i] = ad_status_value[i]
			else:
				pay_money[i] = ad_status_value[i]
		elif ad_status_value[i].isalpha():
			people_orientation[i] = ad_status_value[i]
		elif len(ad_status_value[i].split(","))==7 and ad_status_value[i].split(",")[0].isalnum():
			release_time[i] = ad_status_value[i]
		else:
			people_orientation[i] = ad_status_value[i]

ad_status_ser = Series(ad_status)
pay_money_ser = Series(pay_money)
release_time_ser = Series(release_time)
people_orientation_Ser = Series(people_orientation)
new_data = pd.DataFrame({'ad_status_value':ad_status,'pay_money':pay_money,'release_time':release_time,'people_orientation':people_orientation})
print(new_data[:10])

		
	
	


	

