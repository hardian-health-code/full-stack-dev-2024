import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, Link } from 'react-router-dom';
import { Badge } from '@/components/ui/badge';
import { Button } from "@/components/ui/button"
import { Separator } from '@/components/ui/separator'

function DeviceEntries() {
    const { device_name } = useParams(); // Get the device_name from the URL
    const [deviceEntries, setDeviceEntries] = useState([]); // To store all entries for the device

    useEffect(() => {
        fetchDeviceEntries();
    }, []);

    const fetchDeviceEntries = async () => {
        try {
            const response = await axios.get(`http://localhost:8000/api/device-search/?device_name=${device_name}`);
            setDeviceEntries(response.data.results); // Store all related entries
        } catch (error) {
            console.error('Error fetching device entries', error);
        }
    };

    return (
        <div>
            <h1 className='text-4xl font-black text-gray-900 dark:text-white mb-4 mx-auto'>Entries for {device_name}</h1>

            {/* List all available entries for the device */}
            {deviceEntries.length > 0 ? (
                deviceEntries.map((entry, index) => (
                    <div key={index}>
                        <Link to={`/device-details/${device_name}/${index}`}>
                            <Button variant='secondary'>{index + 1} <Badge className='mx-2'>{entry.source}</Badge> {entry.manufacturer_name} </Button>
                        </Link>
                        <Separator className='my-1' />
                    </div>
                ))
            ) : (
                <p>No entries found for this device.</p>
            )}
        </div>
    );
}

export default DeviceEntries;
