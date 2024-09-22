import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import { Input } from '@/components/ui/input';
import { Separator } from '@/components/ui/separator'
import { Button } from '@/components/ui/button'

function DeviceSearch() {
    const [query, setQuery] = useState('');
    const [allDevices, setAllDevices] = useState([]); // To store all devices initially
    const [filteredDevices, setFilteredDevices] = useState([]); // To store filtered devices
    const [searching, setSearching] = useState(false); // To track if searching

    // Fetch all devices initially and sort alphabetically
    useEffect(() => {
        fetchAllDevices();
    }, []);

    const fetchAllDevices = async () => {
        try {
            const response = await axios.get('http://localhost:8000/api/device-search/?device_name=');
            const sortedDevices = response.data.results.sort((a, b) =>
                a.device_name.localeCompare(b.device_name)
            );
            setAllDevices(sortedDevices);
            setFilteredDevices(removeDuplicates(sortedDevices)); // Remove duplicates when displaying
        } catch (error) {
            console.error('Error fetching all devices', error);
        }
    };

    // Remove duplicates based only on device_name
    const removeDuplicates = (devices) => {
        return devices.reduce((acc, current) => {
            const normalizedDeviceName = current.device_name.toLowerCase();

            const existingDevice = acc.find(
                device => device.device_name.toLowerCase() === normalizedDeviceName
            );

            if (!existingDevice) {
                acc.push(current);
            }
            return acc;
        }, []);
    };

    // Handle search input and dynamically fetch/filter devices
    const handleSearch = async (e) => {
        const inputValue = e.target.value;
        setQuery(inputValue);
        setSearching(true);

        if (inputValue === '') {
            setFilteredDevices(removeDuplicates(allDevices));
            setSearching(false);
            return;
        }

        try {
            const response = await axios.get(`http://localhost:8000/api/device-search/?device_name=${inputValue}`);
            setFilteredDevices(removeDuplicates(response.data.results)); // Remove duplicates in search results
        } catch (error) {
            console.error('Error fetching search results', error);
        }
    };

    return (
        <div>
            <h1 className='text-4xl font-black text-gray-900 dark:text-white mb-4 mx-auto'>Device Search</h1>

            {/* Search bar */}
            <Input
                type="text"
                value={query}
                onChange={handleSearch}
                placeholder="Search for a device"
            />

            {/* Display the list of filtered devices without duplicates */}
            <ul>
                {filteredDevices.length > 0 ? (
                    filteredDevices.map((device, index) => (
            <div>            
            <li key={index}>
                            <Link to={`/device-entries/${device.device_name}`} style={{ textDecoration: 'none' }}>
                                <Button variant="secondary">{device.device_name}</Button>
                            </Link>
                        </li>
                        <Separator className='my-1'/>
                 </div>
                 ))
                ) : (
                    <li>No devices found</li>
                )}
            </ul>
        </div>
    );
}

export default DeviceSearch;
