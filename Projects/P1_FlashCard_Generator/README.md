# AI Flash Card Generator

A beginner-friendly web application that uses AI to automatically generate high-quality flashcards from a topic of interest or user-provided learning material (limited to 100 pages). Users can choose the type of flashcards they want—such as summary notes, concept maps, or quick MCQs—and the app instantly creates them for easy study and revision.  
Review the generated flashcards, make changes, and download them as PDFs.

---

## Features

- **Simple Upload/Input:** Choose a topic of interest or paste/upload your learning material (plain text, PDF, or DOC files – limited to 100 pages max). Select the flashcard types.
- **Customizable Flashcard Types:**
  - **Summary Notes:** Concise summaries of key topics.
  - **Concept Maps:** Visual/text outlines of relationships between concepts.
  - **Quick MCQs:** Multiple-choice questions for rapid review.
- **AI-Powered Flashcard Generation:** Instantly generate flashcards using natural language processing.
- **Review and Regenerate:** Review each card and accept input for any modifications. Regenerate as needed.
- **Download/Export:** Save your flashcards in PDF format.
- **Beginner-Friendly:** Clean, minimal interface with no extra features—just great flashcards.

---

## Tech Stack

- **Frontend:** React (or your preferred beginner-friendly framework)
- **Backend:** Python (Flask)
- **AI/NLP:** HuggingFace Transformers for text analysis and generation
- **File Handling:** Python libraries (e.g., pdfplumber, python-docx)
- **Deployment:** Streamlit Cloud, Vercel, or Heroku (optional)

---

## Getting Started

### Project Structure
```sh
<<<<<<< HEAD
project-root/
=======
ai-flashcard-generator/
>>>>>>> a35dcdf0b2c5c77c5953a14ad6ed27f9c7af9d52
│
├── backend/
│   ├── src/
│   │   ├── file_ingestion.py
│   │   ├── card_generation.py
│   │   ├── output_handler.py
│   │   ├── pipeline.py
│   │   ├── split_pdf_by_chapter.py
│   │   ├── logger.py
│   │   ├── custom_exceptions.py
│   │   └── utils.py
│   ├── tests/
│   │   ├── test_file_ingestion.py
│   │   ├── test_card_generation.py
│   │   ├── test_output_handler.py
│   │   ├── test_pipeline.py
│   │   └── test_utils.py
│   ├── venv/                       # Python virtual environment (excluded in .gitignore)
│   ├── requirements.txt
│   └── README.md
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   ├── package-lock.json
│   └── README.md
│
<<<<<<< HEAD
├── artifacts/
│   ├── experimentation/
│   │   ├── chapter_1.pdf
│   │   ├── chapter_2.pdf
│   │   └── ... (rest of chapters)
│   ├── data/
│   │   └── preprocessed/
│   ├── outputs/
│   │   └── flashcards/
│   └── test_data/
│
├── .gitignore
├── README.md
└── (other config files as needed)
=======
├── README.md                 # Project documentation
└── .gitignore                # Files/folders to ignore in git
>>>>>>> a35dcdf0b2c5c77c5953a14ad6ed27f9c7af9d52
```

### Prerequisites

- Python 3.8+
- Node.js (if using React)
- API key for OpenAI or HuggingFace (for text generation)

### Setup

1. **Clone the repository**
   ```sh
   git clone https://github.com/yourusername/ai-flashcard-generator.git
   cd ai-flashcard-generator
   ```

2. **Install backend dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Install frontend dependencies** (if using React)
   ```sh
   cd frontend
   npm install
   ```

4. **Set up API keys**

   Create a `.env` file and add your API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

### Run the app

- **Backend:**
  ```sh
  python app.py
  ```

- **Frontend (if using React):**
  ```sh
  npm start
  ```

---

## Usage

1. Open the web app in your browser.
2. Upload your notes or paste text.
3. Choose the type of flashcard you want.
4. Click **Generate** to create flashcards instantly.
5. Review, edit, and download the generated flashcards as PDFs for your study routine.

---

## Future Enhancements

- Multi-language support
- Practice/quiz mode
- Integration with Anki/Quizlet
- User accounts and flashcard deck management

---

## License

MIT License

---

## Acknowledgements

- [OpenAI](https://openai.com/)
- [HuggingFace](https://huggingface.co/)
- [Streamlit](https://streamlit.io/) (if used)
