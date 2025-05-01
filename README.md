# FastAPI Application

This is a FastAPI application that provides a backend service for the GenericGrid web app. It serves dynamic grid data and configuration, enabling customizable data grid rendering on the frontend.

## Setup Instructions

Follow these steps to set up and run the application locally:

1. **Create a Virtual Environment**

   First, create a virtual environment to isolate your project dependencies.

   - On **Windows**, run:
     ```bash
     python -m venv venv
     ```
   - On **macOS/Linux**, run:
     ```bash
     python3 -m venv venv
     ```

2. **Activate the Virtual Environment**

   - On **Windows**, run:
     ```bash
     .\venv\Scripts\activate
     ```
   - On **macOS/Linux**, run:
     ```bash
     source venv/bin/activate
     ```

   You should see `(venv)` at the beginning of your command line prompt, indicating the virtual environment is active.

3. **Ensure the Correct Python Interpreter is Selected**

   Make sure the Python interpreter selected in your code editor (e.g., VS Code) is the one from your virtual environment (venv). 
   In VS Code, you can do this by selecting the interpreter from the command palette (Ctrl+Shift+P) and choosing the interpreter inside the venv folder.

4. **Install Requirements**

   Once the virtual environment is activated, install the necessary dependencies listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**

   To start the FastAPI application, use Uvicorn to run the app:

   ```bash
   uvicorn app.main:app --reload
   ```

6. **Access Swagger Documentation**

   Once the application is running, you can access the interactive Swagger UI documentation at: http://127.0.0.1:8000/docs
   This documentation allows you to explore and test the API endpoints directly from your browser.

7. **Check for Lint Issues (Optional)**

   To start the FastAPI application, use Uvicorn to run the app:

   ```bash
   flake8 .
   ```

8. **Run Tests**

   To run the tests for the FastAPI application, use pytest:

   ```bash
   pytest
   ```

## Notes:

Ensure you have Python 3.7+ installed on your machine.
