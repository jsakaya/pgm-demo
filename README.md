# Model Dashboard

This is a Dash application that provides a dashboard for various statistical models.

## Installation

1. Clone this repository
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On Windows: `venv\Scripts\activate`
   - On macOS and Linux: `source venv/bin/activate`
4. Install the required packages: `pip install -r requirements.txt`

## Running the Application

To run the application, execute the following command from the project root:

```
python -m app.main
```

The application will be available at `http://127.0.0.1:8050/` in your web browser.

## Project Structure

- `app/`: Contains the main application files
  - `main.py`: Entry point of the application
  - `models.py`: Definitions of statistical models
  - `layout.py`: Layout of the Dash application
  - `callbacks.py`: Callback functions for interactivity
- `static/`: Static files (CSS)
- `templates/`: HTML templates
- `utils/`: Utility functions
- `requirements.txt`: List of Python dependencies
- `README.md`: This file

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.