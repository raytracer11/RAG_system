# RAG System

A Retrieval-Augmented Generation (RAG) system built with Django that enhances large language model responses with relevant information retrieved from a custom knowledge base.

## Overview

This RAG (Retrieval-Augmented Generation) system improves the quality and accuracy of AI responses by incorporating relevant information from a custom knowledge base. The system retrieves context-specific information and combines it with the language model's capabilities to generate more accurate and contextually relevant responses.

## Directory Structure

```
RAG_system/
├── RAG/                  # Main application directory
├── data/                 # Data files for the knowledge base
├── project/              # Django project settings
├── .gitignore            # Git ignore file
├── db.sqlite3            # SQLite database
├── manage.py             # Django management script
└── requirements.txt      # Project dependencies
```

## Features

- Document ingestion and processing
- Efficient retrieval of relevant context
- Integration with language models for enhanced responses
- Web interface for interacting with the RAG system
- API endpoints for programmatic access

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/raytracer11/RAG_system.git
   cd RAG_system
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - Windows:
     ```bash
     venv\Scripts\activate
     ```
   - Unix/MacOS:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run database migrations:
   ```bash
   python manage.py migrate
   ```

6. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

## Usage

1. Start the development server:
   ```bash
   python manage.py runserver
   ```

2. Access the application at `http://127.0.0.1:8000/`

3. Upload documents to your knowledge base through the web interface or using management commands.

4. Start querying the system with natural language questions related to your knowledge base.

## API Usage

The system provides REST API endpoints for programmatic access:

```python
import requests

# Example: Query the RAG system
response = requests.post(
    "http://localhost:8000/api/query/",
    json={"question": "What is RAG?"}
)
print(response.json())
```

## Configuration

Key configuration options can be found in `project/settings.py`. You may need to set up:

- Language model API keys
- Document processing parameters

## Development

To contribute to the project:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

[Specify your license here]

## Contact

[Your contact information]
