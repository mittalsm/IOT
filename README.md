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

