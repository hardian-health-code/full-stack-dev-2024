# Hardian Health - Full Stack Developer Task Documentation

## Overview
This project is a Django-based single-page application (SPA) that allows users to search for medical devices across two datasets: FDA and EUDAMED. The app provides functionality to search for devices by name, view results from either or both datasets, handle data inconsistencies, and display detailed information for selected devices.

## Approach
### Backend (Django):
 - Database: The application uses an SQLite3 database with two tables: fda_data and eudamed_data. Each table contains relevant device data, with no foreign keys linking the tables.
 - Data Handling:
Device names are matched across both tables using case-insensitive comparisons.
Inconsistencies in device names (e.g., case differences, duplicates) are cleaned and handled gracefully.
Devices found in one or both tables are presented to the user accordingly, with a message indicating if the device exists in only one table or both.

### Frontend (React):
 - Search Functionality: Users can search for devices by entering a query in the search bar. The search query dynamically fetches results from the backend.
 - Data Display: Devices found in both tables are presented with detailed information for each entry. If no device is found, a “not found” message is displayed.
 - Responsiveness: The frontend is styled using TailwindCSS and ShadcnUI, ensuring the app is functional and responsive on different devices.

## Instructions
### Backend Setup:
Install Dependencies:
```
pip install -r requirements.txt
```
Run Migrations: Initialize the database with the following command:
```
python manage.py migrate
```
Run the Development Server: Start the Django development server with:
```
python manage.py runserver
```
### Frontend Setup:
Navigate to the Frontend Directory
Install Dependencies:
```
npm install
```
Run the Development Server: Start the React development server with:
```
npm run dev
```

## Key Decisions and Assumptions
Data Cleaning: Case differences and slight variations in device names (e.g., "ScreenPoint Medical" vs. "screenpoint medical") are cleaned using a case-insensitive comparison. However, if significant inconsistencies (e.g., misspellings) occur, they will be treated as separate entries.

Search Behavior: The search results are fetched dynamically as the user types. Partial matches are supported, so typing a few letters will return all matching devices from both datasets.

API Endpoint: A GET API endpoint (/api/device-search/?device_name=...) is available to fetch device data in JSON format, which can be used for integration with other systems.

## Further Improvements
Pagination: If the dataset grows, pagination could be implemented to handle large search results more efficiently.

Search Autocomplete: Adding an autocomplete feature to enhance the user experience when searching for devices.

Data Validation: Further cleaning and validation of the data, especially for fields like manufacturer_name where variations may exist.

Filtering Options: Adding filters (e.g., risk class, manufacturer, etc.) to allow users to refine their searches.


