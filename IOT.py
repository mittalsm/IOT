import json
from datetime import datetime
# from dateutil.parser import parse
import time
import csv
import requests
import queue
import threading



q1 = queue.Queue()

last_evaluated_time = datetime.now()
buffer_last_evaluated_time = datetime.now()

READ_DATA_EVERY_X_SEC = 5
READ_BUFFER_EVERY_X_SEC = 2

TOTAL_MESSAGES_SENT = 0

url = 'http://127.0.0.1:8081/'
CSV_data = {}
csv_reader_counter = 0

reader = csv.DictReader(open('dataset.csv', 'r'))
dict_list = []
for i,line in enumerate(reader):
	CSV_data[i] = dict(line)



def get_count_of_messages_sent():
	return TOTAL_MESSAGES_SENT

def get_buffer_count():
	return q1.qsize()


def post_data(message):
	x = requests.post(url, data = message)
	return x


def send_buffer_data():
	print("sending buffer data")
	while not q1.empty():
		x = post_data(q1.get())
		print("from buffer call:",x.status_code)
		if x.status_code != 200:
			q1.put(myobj)
		else:
			TOTAL_MESSAGES_SENT+=1


def publish_sensor_data():
	global last_evaluated_time,csv_reader_counter,buffer_last_evaluated_time
	while True:

		if (datetime.now() - buffer_last_evaluated_time).seconds == READ_BUFFER_EVERY_X_SEC:
			'''check buffer, any data present : send to server'''
			if not q1.empty():
				threading.Thread(target=send_buffer_data)
				# thread.start_new_thread(send_buffer_data)

			buffer_last_evaluated_time = datetime.now()




		if (datetime.now() - last_evaluated_time).seconds == READ_DATA_EVERY_X_SEC:
			'''check new messages to be sent to server'''
			myobj = CSV_data[csv_reader_counter]
			print("publish:",CSV_data[csv_reader_counter]['Value'])
			try:
				'''error from SERVER'''
				x = post_data(myobj)
				print(x.status_code)
				if x.status_code !=200:
					q1.put(myobj)
				else:
					TOTAL_MESSAGES_SENT+=1
					
			except Exception as e:
				print("Exception while sending messages to server as:",e)
				q1.put(myobj)

			csv_reader_counter+=1
			last_evaluated_time = datetime.now()


if __name__ == '__main__':
	publish_sensor_data()
