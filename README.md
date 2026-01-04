# Antibiotic Play

![Project Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Vue.js](https://img.shields.io/badge/Frontend-Vue.js_3-4FC08D?logo=vue.js)
![Flask](https://img.shields.io/badge/Backend-Flask-000000?logo=flask)
![MongoDB](https://img.shields.io/badge/Database-MongoDB-47A248?logo=mongodb)

A gamified web platform designed for pharmacy students to learn and practice topics related to antibiotics, dosing, mechanisms of action, and drug classifications.


## Features

### Gamification & Quiz Engine
- **Interactive Question Types:** Drag & Drop (Categorization/Fill-in-the-blanks), Multiple Select (Card Style), Image Labeling, and True/False.
- **Scoring System:** Earn points, level up, and track progress via dynamic progress bars.
- **Badges:** Unlock achievements and medals for completing specific milestones.
- **Leaderboard:** Compete with peers in Bronze, Silver, Gold, and Diamond leagues.


## Tech Stack

- **Frontend:** Vue.js 3 (Composition API), Vite, Pinia, Vue Router, Tailwind CSS, Axios.
- **Backend:** Python, Flask, Flask-RESTful, PyMongo, Flask-JWT-Extended.
- **Database:** MongoDB (NoSQL).


## Installation & Local Development

Follow these steps to run the project locally on your machine.

### Prerequisites
1. [Node.js](https://nodejs.org/) (v16 or higher).
2. [Python](https://www.python.org/) (v3.8 or higher).
3. [MongoDB](https://www.mongodb.com/try/download/community) installed and running on port `27017`.

### 1. Clone the Repository

```bash
git clone [https://github.com/aref-asadi/antibioticplay.git](https://github.com/aref-asadi/antibioticplay.git)
cd antibioticplay
```

### 2. Setup Backend

Navigate to the backend directory and set up the virtual environment:

```bash
cd backend

# Create Virtual Environment
python -m venv venv

# Activate Virtual Environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

Install dependencies and seed the database:

```bash
# Install Python packages
pip install -r requirements.txt

# (Optional) Seed database with initial quiz data
python seed_db.py

# Run the server
python run.py
```

The backend server will start at `http://localhost:5000`.

> **Note:** Database configuration is located in `backend/config.py`. By default, it connects to `mongodb://localhost:27017/antibiotic-game`.

### 3. Setup Frontend

Open a new terminal (keep the backend running) and navigate to the frontend directory:

```bash
cd frontend

# Install JavaScript dependencies
npm install

# Run the development server
npm run dev
```

The application will be accessible at `http://localhost:5173`.


## Contributing

Contributions are welcome!

1. Fork the project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4. Push to the branch (`git push origin feature/AmazingFeature`).
5. Open a Pull Request.