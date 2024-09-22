import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import DeviceSearch from './components/DeviceSearch';
import DeviceDetails from './components/DeviceDetails';
import DeviceEntries from "./components/DeviceEntries"

function App() {
    return (
        <Router className="mx-auto my-5 w-1/2">
            <Routes>
                <Route path="/" element={<DeviceSearch />} />
                <Route path="/device-entries/:device_name" element={<DeviceEntries />} />
                <Route path="/device-details/:device_name/:entry_index" element={<DeviceDetails />} />
          </Routes>
        </Router>
    );
}

export default App;
