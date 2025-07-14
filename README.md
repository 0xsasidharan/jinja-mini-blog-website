

## 📝 Jinja Mini Blog Website

A minimal **microblogging web application** built using **Flask**, **MongoDB**, and **Jinja2 templates with macros**. Users can post short text entries that are stored in MongoDB and displayed using a clean, reusable macro-based interface.

---

### 🚀 Features

* 🧠 Simple, clean **Jinja2 macro-powered** UI
* 🗃️ **MongoDB** backend for storing posts
* 📝 Form for adding new blog entries
* 📅 Date-based formatting of posts
* 🔁 Use of **Jinja2 macros** for rendering posts consistently
* 🌐 Easily deployable on any Flask-compatible server

---

### ⚙️ Tech Stack

* 🐍 Python 3.x
* 🔥 Flask
* 🌿 MongoDB
* 🎨 Jinja2 Templates with **Macros**
* 📦 python-dotenv (for managing secrets)

---

### 🛠️ Installation

1. **Clone the Repository**

```bash
git clone 
cd jinja-mini-blog
```

2. **Create & Activate Virtual Environment**

```bash
# On Linux/macOS:
python -m venv venv
source venv/bin/activate

# On Windows:
python -m venv venv
venv\Scripts\activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Configure MongoDB Connection**

Create a `.env` file in the project root:

```
MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/your-db
```

---

### ▶️ Running the Application

```bash
flask run
```

or

```bash
python app.py
```

Then visit:

```
http://localhost:5000
```

---

