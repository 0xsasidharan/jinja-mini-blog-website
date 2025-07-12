
## 📝 Jinja Mini Blog Website

A minimal microblogging web application built using **Flask**, **MongoDB**, and **Jinja2 templates**. Users can post short text entries which are stored in a MongoDB database and displayed with a clean interface.

---

### 🚀 Features

* 🧠 Simple, clean Jinja-powered UI
* 🗃️ MongoDB backend for storing posts
* 📝 Form to add new entries
* 📅 Date-based formatting of posts
* 🌐 Deployable on any Flask-compatible server

---



### ⚙️ Tech Stack

* 🐍 Python 3.x
* 🔥 Flask
* 🌿 MongoDB
* 🎨 Jinja2 Templates
* 📦 dotenv (for managing secrets)

---

### 🛠️ Installation

1. **Clone the repository**


2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate     # on Linux/macOS
   venv\Scripts\activate        # on Windows
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**

   Create a `.env` file in the root directory:

   ```
   MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/test
   ```

---

### ▶️ Running the App

```bash
flask run
```

Or, if using `app.py` directly:

```bash
python app.py
```

Then visit `http://localhost:5000` in your browser.


