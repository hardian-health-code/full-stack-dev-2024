# Provide below a brief overview of your approach.
## Objective
To create a single-page Django web application that allows users to search for medical devices by name across two datasets: `fda_data` and `eudamed_data`. The data is stored in an SQLite3 database, and the application handles case sensitivity, data inconsistencies, and provides a JSON API.

---

## Key Steps in the Approach:

### 1. Database Models:
- Defined two models, `FDAData` and `EudamedData`, representing the respective tables (`fda_data` and `eudamed_data`) in the SQLite database.
- **Managed=False** was used in the models to inform Django not to manage or create these tables (since they already exist).
- Created a custom manager (`FDADataManager`) for handling distinct queries and lowercasing the device name to address case sensitivity.

### 2. Data Cleaning:
- The device names are inconsistent in terms of case (uppercase vs lowercase).
- Using Django's `Lower` function to handle case-insensitive matching and deduplication of device names across both tables.

### 3. Search Functionality:
- A search bar allows users to input a device name.
- The query is processed in a case-insensitive manner (`device_name__iexact`), and both tables are searched.
- The results from each table are displayed, and if a device is missing from one table, a message informs the user.

### 4. Handling Missing Data:
- If a device is found in one table but not the other, the application displays an appropriate message to inform the user.
- If no matching device is found in either table, a "Device not found" message is returned.

### 5. API Endpoint:
- An optional API endpoint was created to return JSON responses for a given device name search.
- This API returns results from both the FDA and Eudamed datasets as JSON, and it handles missing devices appropriately.

### 6. Front-End Implementation:
- A single-page application (SPA) with a search bar was implemented.
- Bootstrap was used for responsive design, creating a clean and intuitive interface.
- The search results were displayed clearly, differentiating between results from FDA and Eudamed datasets.

### 7. Error Handling:
- Basic error handling was implemented in the API and web application to return appropriate error messages if invalid or missing input is provided (e.g., empty device name).

### 8. Testing:
- Implemented unit tests to ensure case-insensitive search functionality.
- Tested the application for data integrity and consistency, including scenarios where devices exist in one or both datasets.
- Added test cases to verify the functionality of the API endpoint, ensuring the correct data is returned in JSON format.

---

## Challenges Addressed:
- **Case Sensitivity:** Solved by normalizing device names to lowercase using the `Lower()` function in Django queries.
- **Data Duplicates:** Used `distinct()` to avoid returning duplicate results due to case inconsistencies.
- **Missing Data:** Implemented logic to return clear messages when devices are missing from either dataset.

---

This approach ensured that the project met the requirements, handled real-world data inconsistencies, and provided a clean, user-friendly interface with a robust backend.
"""

# Provide below instructions on how to set up and run the project locally.

## Prerequisites
1. **Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).
2. **Virtualenv**: It's recommended to use a virtual environment to manage dependencies. You can install it using:
   ```bash
   pip install virtualenv
   ```
   **Clone the Repository**:

   ```bash
    git clone https://github.com/frazmirza/full-stack-dev-2024.git
    cd full-stack-dev-2024
    ```
   **Create a Virtual Environment**
   ```bash
    virtualenv venv
   ```
   **Activate the virtual environment**:
   **On macOS/Linux**:
    ```bash
      source venv/bin/activate
     ```
   **On Windows**:
   ```bash
    venv\Scripts\activate
     ```
  **Install Dependencies**:
  ```bash
    pip install -r requirements.txt
   ```
  **Run the Development Server**:
  ```bash
    python manage.py runserver
   ```
**Running Tests**:
  ```bash
    python manage.py test
   ```
**API Usage**:
  Search API: You can search for devices using the /api/search_device/ endpoint. The API accepts a GET request with a device_name parameter.
  Example
  ```bash
    http://127.0.0.1:8000/v1/device/?device_name=BoneMRI
   ```
**Frontend Access**:
  ```bash
    http://127.0.0.1:8000/
  ```
# GitHub Actions for Code Formatting
**I have included GitHub Actions to automatically check the code formatting and style using flake8 and isort.**


 


# Provide below any assumptions or decisions you made while implementing the task.
## 1. Database Structure & Integrity
- **Assumption**: 
  - The data in the `fda_data` and `eudamed_data` tables might not be clean and can contain case inconsistencies, duplicates, and missing values.
- **Decision**: 
  - Since there are no foreign keys linking the tables and `device_name` serves as the common identifier, case-insensitive matching and cleaning were applied to ensure accurate matching of devices across both datasets.

## 2. Data Cleaning
- **Assumption**: 
  - Device names may vary in case (e.g., "Device A" vs. "device a"), but represent the same entity.
- **Decision**: 
  - During the search, `Lower()` was used to normalize device names by converting them to lowercase to avoid case-sensitive matching issues. This approach ensures that devices with the same name but different cases are considered identical.

## 3. Django ORM Optimizations
- **Assumption**: 
  - The dataset could potentially grow larger in a real-world scenario.
- **Decision**: 
  - Leveraged Django's `annotate` and `distinct()` methods to optimize query performance and ensure uniqueness in results without manually filtering duplicate entries after retrieval.

## 4. API Response Format
- **Assumption**: 
  - The API will need to return both FDA and Eudamed data, even if the device is found in only one of the tables.
- **Decision**: 
  - The API was designed to return distinct device data from both tables. If a device was found in one table but not the other, the API would still include the results and indicate which table had missing data.

## 5. User Experience (UI/UX)
- **Assumption**: 
  - Users should be able to interact easily with the search interface, and it should handle cases where a device is not found in both tables.
- **Decision**: 
  - A single-page application design with a search bar in the header was implemented. Clear messaging was included for cases where a device exists in one dataset but not the other, or where no results are found in either table.

## 6. Test Cases
- **Assumption**: 
  - Tests are crucial to validate the case-insensitive search and ensure distinct results across the datasets.
- **Decision**: 
  - A test case was created to check the case-sensitivity issue, ensuring that device names with different cases (e.g., "Device A" and "device a") return only one result, simulating a real-world scenario where data inconsistencies exist.

## 7. Handling Missing Data
- **Assumption**: 
  - Certain fields such as `manufacturer_name` could be empty or null.
- **Decision**: 
  - The `manufacturer_name` field was set to accept null and blank values to ensure the model could handle such cases gracefully without causing validation errors.

These assumptions and decisions guided the development and helped address both functional and potential performance considerations for future scalability.

# Provide below any suggestions or recommendations for how you would expand on this functionality further. 
## 1. Full-Text Search
- **Suggestion**: Add full-text search for `device_name` and `manufacturer_name` to allow partial matches and improve search accuracy.
- **Technology**: Use Django’s `SearchVector` or integrate Elasticsearch/PostgreSQL `tsvector`.

## 2. Pagination for Large Results
- **Suggestion**: Implement pagination to handle large result sets and improve performance.
- **Technology**: Use Django’s `Paginator` or DRF’s built-in pagination.

## 3. Enhanced Validation
- **Suggestion**: Add better input validation to handle invalid or incomplete queries and return more informative error messages.

## 4. Caching for Frequent Searches
- **Suggestion**: Cache frequent search results to improve response times and reduce database load.
- **Technology**: Use Django’s caching framework or Redis.

## 5. Expandable Search Fields
- **Suggestion**: Allow search by fields like `manufacturer_name`, `classification`, and `approval_date` for more flexibility.

## 6. Search Autocompletion
- **Suggestion**: Add autocompletion to the search bar for improved user experience and faster searches.

## 7. Role-Based Access
- **Suggestion**: Implement authentication and role-based access control to restrict access to sensitive device data.

## 8. Data Sync Automation
- **Suggestion**: Automate FDA and Eudamed data imports to keep the database up to date.
- **Technology**: Use Celery for task scheduling or external APIs for data sync.

## 9. Advanced Filtering and Sorting
- **Suggestion**: Add filtering and sorting options by attributes like `approval date`, `manufacturer`, etc.

## 10. Detailed Logging and Analytics
- **Suggestion**: Add logging and analytics to monitor user behavior and optimize search performance.