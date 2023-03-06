# Meter Dash
The project shows a simple application that will serve timeseries meter data.
The project consistes of 3 parts:
* A GRPC Server in `MeterUsageServer.py`:
This is a simple python script that will read the meterdata present in the meterusage.csv file and serve that content over GRPC when provided with a start and end date
* A GRPC Client/HTTP Webserver in `Client.py`:
This is a simple Flask application that serves the meter data locally on port 5000 at the /meter endpoint.
When a call is made to this endpoint the Client will make a GRPC request to the GRPC Server to get the meter data.
* A React Frontent application:
This is a simple barebones react frontend that will make calls to the HTTP webserver mentioned above and display the resulting json response

## Requirements and Setup
This project will need python3 and NodeJS.
Install the python requirements using the following command
```
pip3 install -r server/requirements.txt
```

## Usage
You will have to run each of the 3 components using a seperate terminal using their respective start scripts.
Please run them in separate console windows

