# OGA Prototype - Independent Research Project

## About the Project

This project is a Django-based web application for gene and antibody research. It provides a platform for browsing gene information, searching for specific genes, and viewing associated antibody data.

## Features

- User authentication (sign in and register)
- Gene browsing and searching functionality
- Detailed gene information pages
- Antibody data associated with genes
- Responsive design for various screen sizes

## Technologies Used

- Django (Python web framework)
- HTML/CSS for frontend
- JavaScript (assumed for interactivity)
- SQLite (assumed as the default Django database)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/barbaratpferreira/OGA_Prototype--Independent-Research-Project.git
     ```
2. Navigate to the project directory:
     ```bash
     cd OGA_Prototype--Independent-Research-Project
     ```
3. Install required packages (it's recommended to use a virtual environment):
      ```bash
      pip install -r requirements.txt
      
4. Run migrations:
      ```bash
      python manage.py migrate
 
5. python manage.py runserver:
      ```bash
      python manage.py runserver
    

## Usage
After starting the server, navigate to http://localhost:8000 in your web browser to access the application.
Project Structure

   - browse/: App for gene browsing functionality
   - static/: Contains CSS and JavaScript files
   - templates/: HTML templates for the project

## Disclaimer
This project is part of an academic assessment and is designed for educational purposes only.
