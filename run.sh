#!/bin/bash

# Fake News Detector Project Runner
# This script starts the Flask backend and opens the frontend in the default browser

echo "🚀 Starting Fake News Detector..."

# Check if Python is installed
if ! command -v python &> /dev/null && ! command -v python3 &> /dev/null; then
    echo "❌ Python is not installed. Please install Python 3."
    exit 1
fi

# Use python3 if available, otherwise python
PYTHON_CMD="python"
if command -v python3 &> /dev/null; then
    PYTHON_CMD="python3"
fi

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    PYTHON_CMD="venv/bin/python3"
fi

# Check if required packages are installed
$PYTHON_CMD -c "import flask, pandas, sklearn, joblib, flask_cors" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ Required Python packages are not installed."
    echo "Please run: $PYTHON_CMD -m pip install flask pandas scikit-learn joblib flask-cors"
    exit 1
fi

# Check if model files exist
if [ ! -f "model.pkl" ] || [ ! -f "vectorizer.pkl" ]; then
    echo "⚠️  Model files not found. The backend will train the model on first run."
fi

# Check if port 5000 is already in use
if lsof -Pi :5000 -sTCP:LISTEN -t >/dev/null 2>&1; then
    echo "ℹ️  Backend is already running on port 5000. Skipping backend start."
    BACKEND_PID=""
else
    # Start the backend in the background
    echo "🔧 Starting Flask backend on http://127.0.0.1:5000..."
    $PYTHON_CMD backend.py &
    BACKEND_PID=$!
fi

# Wait for the server to start
echo "⏳ Waiting for server to start..."
sleep 5

# Get the absolute path to index.html
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
INDEX_PATH="file://$SCRIPT_DIR/index.html"

# Open the frontend in the default browser
echo "🌐 Opening frontend in browser..."
if command -v open &> /dev/null; then
    open "$INDEX_PATH"
elif command -v xdg-open &> /dev/null; then
    xdg-open "$INDEX_PATH"
elif command -v start &> /dev/null; then
    start "$INDEX_PATH"
else
    echo "📋 Please manually open: $INDEX_PATH"
fi

echo "✅ Fake News Detector is running!"
echo "📊 Backend: http://127.0.0.1:5000"
echo "🖥️  Frontend: $INDEX_PATH"
echo "Press Ctrl+C to stop the server"

# Wait for the backend process if it was started
if [ -n "$BACKEND_PID" ]; then
    wait $BACKEND_PID
fi
