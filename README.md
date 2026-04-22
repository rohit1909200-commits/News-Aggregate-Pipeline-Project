# 📚 News Aggregator Pipeline

## 🧠 Overview

This project is a **Python-based data pipeline** that generates daily vocabulary quizzes, tracks user learning progress, and adapts content using **spaced repetition techniques**.

The system follows a **Bronze → Silver → Gold architecture**, ensuring clean data processing and intelligent quiz generation.

---

## 🎯 Objective

* Generate daily vocabulary quizzes
* Track user performance
* Improve learning using spaced repetition
* Provide review mode for weak areas

---

## 📂 Dataset / Data Source

### Input File

* `Vocabulary.csv`

  * Word
  * Optional Difficulty (easy, medium, hard)

### External API

* Dictionary API:

  * Definitions
  * Example Sentences

---

## ⚙️ Pipeline Architecture

```
CSV → Bronze Layer → Silver Layer → Gold Layer
```

### 🥉 Bronze Layer (Raw Data)

* Reads vocabulary from CSV
* Fetches definitions from API
* Stores raw data in SQLite

### 🥈 Silver Layer (Clean Data)

* Removes invalid or missing API responses
* Keeps only usable data

### 🥇 Gold Layer (Final Output)

* Generates quizzes
* Tracks performance
* Applies spaced repetition
* Provides review mode

---

## 🚀 Features

### 1. Data Ingestion

* Reads vocabulary from CSV
* Fetches data from API
* Logs failures using try-except

### 2. Quiz Generation

* Generates 10 random words daily
* Avoids frequent repetition
* Includes:

  * Word
  * Definition
  * Example

### 3. Spaced Repetition

* Repeats difficult words more often
* Reduces frequency of mastered words

### 4. Data Storage (SQLite)

Tables:

* `bronze_words` → Raw data
* `silver_words` → Clean data
* `quizzes` → Daily quiz
* `performance` → User progress

### 5. Score Tracking

* Tracks correct and incorrect answers
* Calculates accuracy per word

### 6. Review Mode

* Focuses on:

  * Incorrect words
  * Difficult words

### 7. Output Generation

* Daily quiz retrieval
* Past quiz history

### 8. Data Validation

* Handles:

  * Missing words
  * API failures
  * Incomplete responses

---

## 🛠️ Technologies Used

* Python
* Pandas
* Requests (API calls)
* SQLite (Database)
* Random (quiz selection)
* Datetime

---

## 📦 Installation & Setup

### Step 1: Install dependencies

```bash
pip install pandas requests
```

### Step 2: Add your dataset

Place `Vocabulary.csv` in the project folder.

### Step 3: Run the script

```bash
python main.py
```

---

## 🧪 Example Workflow

1. Load words from CSV
2. Fetch meanings from API
3. Store raw data (Bronze)
4. Clean data (Silver)
5. Generate quiz (Gold)
6. Track user answers
7. Improve future quizzes

---

## 📊 Database Schema

### bronze_words

* word
* difficulty
* definition
* example

### silver_words

* Cleaned version of bronze data

### quizzes

* quiz_date
* word
* definition
* example

### performance

* word
* correct_count
* wrong_count
* last_seen

---

## 🔁 Spaced Repetition Logic

* If **wrong > correct** → word repeated more
* If **correct > wrong** → word shown less
* Ensures efficient learning

---

## 📌 Future Improvements

* Add GUI (Tkinter / Web App)
* User authentication system
* Difficulty-based adaptive quizzes
* Analytics dashboard
* Mobile app integration

---

## 👨‍💻 Author

* Rohit Murari

---

## 📄 License

This project is for educational purposes.
