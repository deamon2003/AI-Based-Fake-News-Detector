# 🕵️‍♂️ Fake News Detector

A modern web-based AI fake news detector built with HTML, CSS, and JavaScript. This application analyzes news articles to determine if they are likely fake or real news using advanced linguistic analysis and heuristics.

## 🚀 Features

- **Text Analysis**: Input news text directly or upload .txt files
- **Batch Processing**: Upload multiple files and view results in a table format
- **Machine Learning**: Backend ML model for accurate predictions
- **Advanced Detection**: Uses weighted keywords, linguistic patterns, and heuristics
- **Modern UI**: Beautiful gradient design with smooth animations
- **Responsive Design**: Works on desktop and mobile devices
- **Real-time Results**: Instant detection with confidence scores
- **File Upload**: Support for multiple .txt file uploads
- **Color-coded Results**: Visual indicators for fake/real predictions

## 📁 Project Structure

```
fake-news-detector/
├── backend.py          # Flask API server with ML model
├── index.html          # Main HTML file
├── run.sh              # Bash script to run the project
├── assets/
│   ├── styles.css      # Styling and animations
│   └── script.js       # Detection logic and UI interactions
├── tests/
│   ├── test_news.txt   # Sample fake news for testing
│   └── test_real_news.txt  # Sample real news for testing
├── dataset/            # Training data files
├── docs/
│   └── TODO.md         # Development notes and checklist
├── model.pkl           # Trained ML model
├── vectorizer.pkl      # TF-IDF vectorizer
└── README.md           # This file
```

## 🛠️ How to Run

### Option 1: Using the Bash Script (Recommended)

```bash
./run.sh
```

This will automatically start the Flask backend and open the frontend in your browser.

### Option 2: Manual Setup

1. **Install dependencies:**

   ```bash
   pip install flask pandas scikit-learn joblib
   ```

2. **Start the backend:**

   ```bash
   python backend.py
   ```

3. **Open in browser:**
   Navigate to `http://localhost:5000` or open `index.html` directly.

4. **Test the app:**
   - Enter news text or upload multiple .txt files
   - Click "🔍 Detect Fake News"
   - View results with confidence scores and table display for batch processing

## 🔍 Detection Algorithm

The detector uses a sophisticated rule-based approach with:

- **Keyword Analysis**: 40+ fake news indicators and 50+ real news indicators with weighted scoring
- **Linguistic Heuristics**:
  - All caps detection
  - Punctuation overuse
  - Sensational language
  - Source citation checking
  - Article length analysis
  - Emotional language detection

## 📊 Test Results

- **Fake News Sample**: Detected as FAKE (100% confidence)
- **Real News Sample**: Detected as REAL (43% confidence)

## 🧪 Testing

Use the provided test files in the `tests/` folder:

- `test_news.txt`: Should be detected as fake
- `test_real_news.txt`: Should be detected as real

## 📝 Development

- Built with vanilla HTML, CSS, and JavaScript
- No external dependencies required
- Client-side processing for privacy
- Responsive design with modern CSS features

## 🤝 Contributing

Feel free to improve the detection algorithm by:

- Adding more keywords
- Refining heuristics
- Enhancing the UI
- Adding more test cases

## 📄 License

This project is open source and available under the MIT License.
# AI-Based-Fake-News-Detector


<img width="1690" height="918" alt="Screenshot 2025-10-30 at 5 14 50 PM" src="https://github.com/user-attachments/assets/a6d98d01-39f2-438a-bc0b-fa557f060880" />

<img width="1252" height="874" alt="Screenshot 2025-10-30 at 5 15 21 PM" src="https://github.com/user-attachments/assets/d3d4f9e3-7079-4c3c-94e3-9950e4f7952e" />





