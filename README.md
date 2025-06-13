Python Docker App 🐍
A simple Flask web application containerized with Docker, ready for GitHub deployment.
Features

Flask Web Framework: Lightweight and flexible
Docker Support: Fully containerized application
Health Checks: Built-in health monitoring
API Endpoints: REST API with status endpoints
Production Ready: Uses Gunicorn WSGI server

Quick Start
Prerequisites

Docker and Docker Compose installed
Git (for GitHub integration)

Local Development

Clone the repository

bashgit clone <your-repo-url>
cd mini-python-docker-app

Run with Docker Compose

bashdocker-compose up --build

Access the application


Web UI: http://localhost:5000
API Status: http://localhost:5000/api/status
Health Check: http://localhost:5000/api/health

Manual Docker Commands
bash# Build the image
docker build -t mini-python-app .

# Run the container
docker run -p 5000:5000 mini-python-app
API Endpoints
EndpointMethodDescription/GETMain web interface/api/statusGETApplication status with timestamp/api/healthGETHealth check endpoint
Project Structure
.
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Dockerfile         # Docker configuration
├── docker-compose.yml # Docker Compose setup
├── templates/         # HTML templates
│   └── index.html    # Main web page
├── .gitignore        # Git ignore rules
└── README.md         # This file
Docker Configuration

Base Image: Python 3.11 slim
Port: 5000
Health Check: Automatic monitoring
Production Server: Gunicorn WSGI

Development
Adding New Features

Modify app.py for new routes
Update templates/index.html for UI changes
Add dependencies to requirements.txt
Rebuild with docker-compose up --build

Environment Variables

PORT: Application port (default: 5000)

Deployment
This app is ready for deployment on various platforms:

Docker Hub: Push your built image
GitHub Actions: Set up CI/CD workflows
Cloud Platforms: Deploy to AWS, Azure, GCP
Container Orchestration: Kubernetes, Docker Swarm

Contributing

Fork the repository
Create a feature branch
Make your changes
Test with Docker
Submit a pull request

License
This project is open source and available under the MIT License.

Built with ❤️ using Python, Flask, and Docker