#! /bin/bash
FLASK_APP=Client.py
FLASK_ENV=development
cd server
echo "Starting GRPC Client"
flask run
