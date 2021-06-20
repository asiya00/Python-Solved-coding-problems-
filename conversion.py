import datetime
date_time_str = '8:15:27'
if data_time_str=='%H:%M:%S':
	date_time_obj = datetime.datetime.strptime(date_time_str,'%H:%M:%S').time()
	b=date_time_obj
	print(b)
	hr=b.hour
	min=b.minute
	sec=b.second
	total=(hr*3600)+(min*60)+(sec)
	print(total)
