import React, { useState, useEffect } from 'react';
import axios from 'axios';

function MeterReading(props) {
    const [meterData, setMeterData] = useState([]);
    const [startTime, setStartTime] = useState(new Date("2019-01-01T00:00:00Z").toISOString().slice(0, 16));
    const [endTime, setEndTime] = useState(new Date("2019-01-01T12:00:00Z").toISOString().slice(0, 16));

    useEffect(() => {
        fetchData();
    }, [startTime, endTime]);

    const handleStartTimeChange = (event) => {
        const localDate = new Date(event.target.value);
        const utcDate = new Date(
            localDate.getTime() - localDate.getTimezoneOffset() * 60000
        );
        setStartTime(utcDate.toISOString().slice(0, 16));
    };

    const handleEndTimeChange = (event) => {
        const localDate = new Date(event.target.value);
        const utcDate = new Date(
            localDate.getTime() - localDate.getTimezoneOffset() * 60000
        );
        setEndTime(utcDate.toISOString().slice(0, 16));
    };


    const handleFetchData = () => {
        fetchData();
    };

    const fetchData = () => {
        axios.get("/meter", {
            params: {
                start_time: startTime,
                end_time: endTime
            }
        })
            .then(response => setMeterData(response.data))
            .catch(error => console.error(error));
    };

    return (
        <div>
            <h1>Meter Reading</h1>
            <div>
                <label htmlFor="start-time">Start Time:</label>
                <input type="datetime-local" id="start-time" name="start-time" value={startTime} onChange={handleStartTimeChange} />
            </div>
            <div>
                <label htmlFor="end-time">End Time:</label>
                <input type="datetime-local" id="end-time" name="end-time" value={endTime} onChange={handleEndTimeChange} />
            </div>
            <button onClick={handleFetchData}>Fetch Data</button>
            <pre>{JSON.stringify(meterData, null, 2)}</pre>
        </div>
    );
}

export default MeterReading;
