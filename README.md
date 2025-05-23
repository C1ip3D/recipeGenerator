# flask-app

This is a Flask web application project.

## Project Structure

```
flask-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── templates
│       └── base.html
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd flask-app
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python run.py
   ```

## Usage

After running the application, you can access it at `http://127.0.0.1:5000/`. 

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.