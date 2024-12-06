## Financial Market Data Service

This is a small service designed to process financial market data, calculate technical indicators, and provide a REST API and frontend for querying and visualizing the processed data.

## Features
### Data Processing

Stores 1-minute K-Line data efficiently.
Calculates and provides key technical indicators:
MACD (Moving Average Convergence Divergence)
RSI (Relative Strength Index)
API

Fetch raw K-Line data for time intervals:
1 minute, 5 minutes, and 60 minutes.
Query indicators like MACD and RSI.
Frontend

Visualizes K-Line data on an interactive chart using react-chartjs-2.
Performance Optimization

Optimized database schema for high-frequency data.
Efficient querying mechanisms for better API response times.
Folder Structure
graphql
.
```bash
├── backend/                # Backend service files
│   ├── app/
│   │   ├── database.py     # Database connection and query logic
│   │   ├── indicators.py   # MACD and RSI calculation logic
│   │   ├── main.py         # FastAPI app with API endpoints
│   │   ├── models.py       # SQLAlchemy models for the database
│   │   └── __init__.py     # Package initializer
│   ├── kline_data.db       # SQLite database file
│   ├── requirements.txt    # Python dependencies
│   └── Dockerfile          # Dockerfile for backend service
│
├── frontend/               # Frontend service files
│   ├── src/                # React app source files
│   │   ├── components/     # React components
│   │   ├── KLineChart.js   # Chart component to visualize K-Line data
│   │   └── App.js          # Main app entry point
│   ├── public/             # Static assets
│   ├── package.json        # Node.js dependencies
│   ├── Dockerfile          # Dockerfile for frontend service
│   └── README.md           # Instructions for the frontend
│
├── docker-compose.yml      # Docker Compose file to run both services
└── README.md               # This file
```

### Getting Started
#### Prerequisites
Docker
Docker Compose
Internet connection for dependency installation.

### Setup Instructions
#### Clone the Repository

```bash
git clone <repository-url>
cd <repository-folder>
```

Build and Start Services Use Docker Compose to build and start both backend and frontend services:

```bash
docker-compose up --build
```

### Access the Services

Backend API: http://localhost:8000/docs (Swagger UI)
Frontend: http://localhost:3000


### Backend Service
#### API Endpoints
Endpoint	Method	Description
/kline?interval=1min	GET	Retrieve K-Line data (1min interval)
/kline?interval=5min	GET	Retrieve K-Line data (5min interval)
/kline?interval=60min	GET	Retrieve K-Line data (60min interval)
/indicator/macd?symbol=BTC	GET	Get MACD data for a symbol
/indicator/rsi?symbol=BTC	GET	Get RSI data for a symbol

### Frontend Service
#### Overview
The frontend is built using React and displays K-Line data on a dynamic chart.

#### Key Features
Chart rendering using react-chartjs-2.
Auto-fetching data from the backend API.

### Technical Details
#### Backend
Framework: FastAPI
Database: SQLite
ORM: SQLAlchemy
Dependencies:
fastapi
uvicorn
pandas
sqlalchemy

#### Frontend
Framework: React
Dependencies:
react
react-chartjs-2
chart.js
Performance Optimization
Data Ingestion

The database uses a compact schema for high-frequency K-Line data.

### Querying
Indexing is applied on frequently queried columns.

### API Response Times
Data is paginated for large responses.
Heavy calculations (e.g., MACD, RSI) are cached for repeated requests.

