# Provide below a brief overview of your approach.
I built the project around the provided tests.py to ensure the core search functionality met the requirements. I utilized Django’s ORM to query both FDA and Eudamed datasets, cleaned data by ensuring case-insensitive searches, and handled cases where devices were missing from one or both tables. TailwindCSS was integrated for responsive front-end design, and I implemented an API endpoint to serve JSON responses for search queries.

# Provide below instructions on how to set up and run the project locally.
1. Install dependencies: Run `pip install -r requirements.txt` to install all required packages.
2. Database Setup: Ensure the `db.sqlite3.db` file is in the project root and migrate if necessary using `python manage.py migrate`.
3. Run the server: Start the server with `python manage.py runserver` and navigate to `localhost:8000` to test the application.
4. Run Tests: Use `python manage.py test devices` to run the provided test suite and ensure everything works.

# Provide below any assumptions or decisions you made while implementing the task.
- I assumed that device_name was the primary field for searching in both datasets.
- All search queries were case-insensitive to handle inconsistencies in naming conventions.
- The task allowed flexibility with front-end frameworks, so I chose TailwindCSS for rapid styling and responsiveness.

# Provide below any suggestions or recommendations for how you would expand on this functionality further. 
- Implement pagination for search results, especially if the dataset grows.
- Introduce additional filtering options (e.g., by manufacturer) for more refined search results.
- Add authentication and role-based access for different types of users (e.g., admins managing the datasets).
- Integrate real-time search using JavaScript and AJAX for better user experience on the front-end.