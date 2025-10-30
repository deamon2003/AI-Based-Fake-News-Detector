# TODO: Update Batch Results to Table Format

## Steps to Complete

- [x] Update index.html to replace <ul id="resultsList"> with <table id="resultsTable"> including headers for File Name, Prediction, Confidence, Fake Score, Real Score
- [x] Update assets/script.js to modify displayBatchResults function to create table rows (<tr>) and cells (<td>) instead of list items
- [x] Update assets/styles.css to add table-specific styles matching the existing design, including hover effects and color coding for fake/real
- [x] Test the batch upload functionality with multiple .txt files to ensure the table displays correctly
- [x] Backend now predicts on any text using ML model with probabilities/confidence
- [x] Frontend displays batch results in table format with individual predictions per line in uploaded txt files
- [x] Run script checks if port 5000 is in use and skips starting backend if occupied
- [x] Critical-path testing completed: backend predicts on new texts, frontend displays batch results correctly, script handles existing port usage
