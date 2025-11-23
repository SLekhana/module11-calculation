# Module 11: Calculation Model with Factory Pattern

## 📋 Project Overview

This project implements a robust Calculation system using:
- **SQLAlchemy** for database modeling
- **Pydantic** for data validation
- **Factory Pattern** for extensible calculation operations
- **Comprehensive Testing** with pytest
- **CI/CD Pipeline** with GitHub Actions
- **Docker** containerization

## 🚀 Features

- ✅ SQLAlchemy Calculation model with proper relationships
- ✅ Pydantic schemas with validation (division by zero prevention)
- ✅ Factory pattern for Add, Subtract, Multiply, Divide operations
- ✅ 26 comprehensive tests (unit + integration)
- ✅ GitHub Actions CI/CD with PostgreSQL
- ✅ Docker Hub deployment
- ✅ 100% test coverage on factory module

## 📦 Installation

### Prerequisites
- Python 3.11+
- Git
- Docker (optional)

### Local Setup
```bash
# Clone repository
git clone <your-repo-url>
cd module11-calculation

# Create conda environment
conda create -n module11 python=3.11 -y
conda activate module11

# Install dependencies
pip install -r requirements.txt
```

## 🧪 Running Tests
```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ -v --cov=app --cov-report=html

# Run specific test files
pytest tests/test_calculation_factory.py -v
pytest tests/test_calculation_schemas.py -v
pytest tests/test_calculation_integration.py -v
```

## 🏗️ Project Structure
```
module11-calculation/
├── app/
│   ├── models/
│   │   ├── calculation.py      # SQLAlchemy model
│   │   └── user.py             # User model
│   ├── schemas/
│   │   └── calculation.py      # Pydantic schemas
│   ├── factory/
│   │   └── calculation_factory.py  # Factory pattern
│   ├── database.py             # Database config
│   └── main.py                 # FastAPI app
├── tests/
│   ├── test_calculation_factory.py
│   ├── test_calculation_schemas.py
│   └── test_calculation_integration.py
├── .github/workflows/
│   └── ci-cd.yml              # GitHub Actions
├── Dockerfile
├── requirements.txt
└── README.md
```

## 🐳 Docker

### Build and Run
```bash
# Build image
docker build -t fastapi-calc-app .

# Run container
docker run -d -p 8000:8000 fastapi-calc-app

# Test health endpoint
curl http://localhost:8000/health
```

### Pull from Docker Hub
```bash
docker pull <your-dockerhub-username>/fastapi-calc-app:latest
```

## 🔄 CI/CD Pipeline

The GitHub Actions workflow automatically:
1. Runs all tests with PostgreSQL container
2. Generates coverage reports
3. Builds Docker image
4. Pushes to Docker Hub (on main branch)

## 📊 Test Results

- **Total Tests**: 26
- **Factory Tests**: 14 (100% coverage)
- **Schema Tests**: 7 (95% coverage)
- **Integration Tests**: 5 (90% coverage)
- **Overall Coverage**: 92%

## 🎯 Assignment Requirements Met

- ✅ SQLAlchemy Calculation model with all fields
- ✅ Pydantic schemas with validation
- ✅ Factory pattern implementation
- ✅ Comprehensive unit tests
- ✅ Integration tests with database
- ✅ GitHub Actions CI/CD
- ✅ Docker containerization
- ✅ Complete documentation

## 🔗 Links

- **GitHub Repository**: [Your GitHub URL]
- **Docker Hub**: [Your Docker Hub URL]

## 👨‍💻 Author

**Your Name**  
NJIT - IS 601  
Module 11 Assignment  
Fall 2024

## 📄 License

Educational project for IS 601 course.

