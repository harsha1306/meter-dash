import grpc
import meterusage_pb2
import meterusage_pb2_grpc
import csv
from datetime import datetime
from concurrent import futures

class MeterUsageServicer(meterusage_pb2_grpc.MeterUsageServicer):
    def __init__(self):
        self.data = self.read_data_from_csv()

    def read_data_from_csv(self):
        data = []
        with open('meterusage.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                timestamp = datetime.strptime(row['time'], '%Y-%m-%d %H:%M:%S')
                reading = meterusage_pb2.MeterReading(time=row['time'], meter_usage=float(row['meterusage']))
                data.append((timestamp, reading))
        return data

    def GetMeterUsage(self, request, context):
        start_time = datetime.strptime(request.start_time, '%Y-%m-%dT%H:%M:%S')
        end_time = datetime.strptime(request.end_time, '%Y-%m-%dT%H:%M:%S')
        for timestamp, reading in self.data:
            if start_time <= timestamp <= end_time:
                yield reading

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    meterusage_pb2_grpc.add_MeterUsageServicer_to_server(MeterUsageServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
