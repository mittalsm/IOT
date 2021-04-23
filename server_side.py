
import random
import csv
from csv import writer
from os import path




fields = ["Sensor","Value","Timestamp"]

if not path.exists("OUTPUT.csv"):
    with open("OUTPUT.csv", 'a') as csvfile: 
        csv_writer = writer(csvfile)
        csv_writer.writerow(fields)
        csvfile.close()


from flask import Flask, request, Response

resps= [200,404]
app = Flask(__name__)


@app.route('/', methods=['POST'])
def result():
    status_code = random.choice(resps)
    if status_code == 200:
        print("Random status code is 200")
        try: 
            with open("OUTPUT.csv", 'a', newline='') as csvfile:
                csv_writer = writer(csvfile)
                # Add contents of list as last row in the csv file
                csv_writer.writerow(dict(request.form).values())
                csvfile.close()
        except Exception as e:
            print("Exception while saving sensor data point as:",e)
            return Response(status=404, mimetype='application/json')

    else:
        print("Random status code is not 200")
    return Response(status=status_code, mimetype='application/json')

if __name__ == '__main__':
   app.run(host="",port=8081,debug = True)
