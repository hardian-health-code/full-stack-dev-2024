# Provide below a brief overview of your approach.

This Django web application allows users to search for device names from two different tables (`fda_data` and `eudamed_data`). The project focuses on retrieving data based on device names while addressing inconsistencies such as case differences and duplicates. The search results display data from both tables, with appropriate messages shown when data is missing in one or both tables. The application features a single-page layout for user-friendly interaction and includes an API endpoint that provides the same functionality.

# Provide below instructions on how to set up and run the project locally.

## Prerequisites

- **Python 3.12** (Make sure it is installed on your system)
- **Virtual Environment** (Recommended for dependency management)

## Steps to Set Up the Project Locally

1. **Clone the Repository:**

    ```bash
    git clone <repository_url>
    cd <project_directory>
    ```

2. **Create a Virtual Environment:**

    ```bash
    python3.12 -m venv venv
    ```

3. **Activate the Virtual Environment:**

    - **On Windows:**

        ```bash
        venv\Scripts\activate
        ```

    - **On macOS/Linux:**

        ```bash
        source venv/bin/activate
        ```

4. **Install Dependencies:**

    Make sure you have a `requirements.txt` file.

    ```bash
    pip install -r requirements.txt
    ```

5. **Run Database Migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Run the Django Development Server:**

    ```bash
    python manage.py runserver
    ```

7. **Access the Application:**

    Open your web browser and navigate to [http://localhost:8000](http://localhost:8000) to access the search functionality.

# Provide below any assumptions or decisions you made while implementing the task.

- **Case Sensitivity:** Device name searches are case-insensitive. Device names are normalized for both `fda_data` and `eudamed_data`.

- **Data Matching:** Matching is done based on `device_name` after cleaning and normalizing inconsistencies (e.g., spaces, special characters).

- **Single Page Design:** The application is designed as a single-page interface with a search bar at the top for a smoother user experience.

- **Data Handling:** If a device exists in one table but not the other, the result is returned from the available table, with a message displayed for the missing table.

- **Testing:** Basic test cases cover key functionalities such as devices found in both tables, in one table, or not found in either table.

# Provide below any suggestions or recommendations for how you would expand on this functionality further. 

- **Data Deduplication:** Implement logic to prevent duplicate entries by adding unique constraints on fields (e.g., `device_name`) or performing checks before inserting new data.

- **Pagination:** Implement pagination for search results to handle large datasets and improve UX and performance.

- **Advanced Search:** Add additional filters (e.g., by device category, manufacturer, or date) to enhance search capabilities.

- **Caching:** Consider caching search results to reduce database hits for frequently searched terms.

- **Data Cleaning Improvements:** Enhance data cleaning processes to handle abbreviations or synonyms, improving search accuracy.

- **Error Handling:** Add robust error handling for edge cases like network failures or database connectivity issues.

- **API Enhancements:** Expand the API to include additional search filters, sorting options, or device details for better flexibility and external integrations.
