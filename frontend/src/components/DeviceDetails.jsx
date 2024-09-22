import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';

function DeviceDetails() {
    const { device_name, entry_index } = useParams(); // Get device_name and entry index from the URL
    const [deviceDetails, setDeviceDetails] = useState(null); // To store selected device details

    useEffect(() => {
        fetchDeviceDetails();
    }, []);

    const fetchDeviceDetails = async () => {
        try {
            const response = await axios.get(`http://localhost:8000/api/device-search/?device_name=${device_name}`);
            setDeviceDetails(response.data.results[entry_index]); // Get the specific entry by index
        } catch (error) {
            console.error('Error fetching device details', error);
        }
    };

    return (
        <div>
            <h1>Details for {device_name}</h1>

            {/* Display detailed information for the selected entry */}
            {deviceDetails ? (
                <pre>{JSON.stringify(deviceDetails, null, 2)}</pre>
            ) : (
                <p>Loading details...</p>
            )}
        </div>
    );
}

export default DeviceDetails;
