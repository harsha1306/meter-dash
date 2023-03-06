import grpc
import meterusage_pb2
import meterusage_pb2_grpc
import urllib.parse
from datetime import datetime,timedelta
from flask import Flask, jsonify, request

app = Flask(__name__)

def get_meter_usage(start_time: datetime, end_time: datetime):
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = meterusage_pb2_grpc.MeterUsageStub(channel)
        request = meterusage_pb2.TimestampRange(start_time=start_time.strftime("%Y-%m-%dT%H:%M:%S"), end_time=end_time.strftime("%Y-%m-%dT%H:%M:%S"))
        response_iterator = stub.GetMeterUsage(request)
        meter_readings = [reading for reading in response_iterator]
        return meter_readings

@app.route('/meter', methods=['GET'])
def meter():
    start_time_str = request.args.get('start_time')
    end_time_str = request.args.get('end_time')
    start_time = datetime.now() - timedelta(days=1)
    end_time = datetime.now()

    if start_time_str :
        start_time = datetime.fromisoformat(urllib.parse.unquote(start_time_str))

    if end_time_str :
        end_time = datetime.fromisoformat(urllib.parse.unquote(end_time_str))

    meter_readings = get_meter_usage(start_time, end_time)

    response = {
        'meter_readings': [{'time': str(reading.time), 'meterusage': reading.meter_usage} for reading in meter_readings]
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()
