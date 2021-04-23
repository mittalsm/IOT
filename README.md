# IOT
reading sensor data and publishing it to server

There are two source code file :

IOT.py for reading sensor data and publishing it to cloud server 

server_side for receving POST request from IOT.py and saving sensor data to CSV file.

Sample data:
dataset.csv = A small collection of sensor data, used here to read by IOT.py and send it to cloud

Commands to run IOT.py

After Pull request of the brach
1. source IOT_env/bin/activate
2. pip3 install requirements.txt
3. python3 IOT.py
client side code is ready and should be running

Commands to run server_side.py

1. python3 server_side.py
Server_side is ready and should be running


IOT.py:
is resposible for reading a record from dataset.csv every 5 seconds and send the data point to cloud. If server does not respond or gives any error code, the data point is stored in a buffer and is tried sending again every 2 seconds

server_side.py:
is resposible for receving POST request on the server side hosted with help of flask. after reading data point from post request, server try to save it OUTPUT.csv file. If any issue comes in appending data point, server respond with error code to client.



