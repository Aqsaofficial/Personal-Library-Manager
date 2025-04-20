

---

## 📚 Personal Library Manager – Beginner Level Project

### 🌐 Overview

This web-based app lets you manage your personal book collection:  
- 📖 Add new books  
- 🗑️ Remove books  
- 🔍 Search for books  
- 📊 View statistics on your library

We’ll build this using **Python** and **Streamlit**, which makes UI creation simple and interactive — no HTML/CSS needed!

---

## 🛠️ Prerequisites

Make sure the following are installed:

- ✅ Python 3.x: [Download Python](https://www.python.org/downloads/)
- ✅ Visual Studio Code (VS Code): [Download VS Code](https://code.visualstudio.com/)
- ✅ Streamlit (install via pip):

```bash
pip install streamlit
```

---

## 🧱 Project Setup

### Step 1: Create the Project Folder

Open your terminal or command prompt and run:

```bash
mkdir personal_library_manager
cd personal_library_manager
```

### Step 2: Create the Main App File

In the `personal_library_manager` folder, create a file called `app.py`. Paste this code inside:

```python
import streamlit as st
import json
import os

# -----------------------
# Helper Functions
# -----------------------

DATA_FILE = "library.json"

def load_library():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return []

def save_library(library):
    with open(DATA_FILE, "w") as file:
        json.dump(library, file, indent=4)

def add_book(title, author, year, genre, status):
    library = load_library()
    library.append({
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "status": status
    })
    save_library(library)

def remove_book(title):
    library = load_library()
    updated_library = [book for book in library if book["title"].lower() != title.lower()]
    save_library(updated_library)

def search_books(query):
    library = load_library()
    return [book for book in library if query.lower() in book["title"].lower() or query.lower() in book["author"].lower()]

def get_stats():
    library = load_library()
    total = len(library)
    read = sum(1 for book in library if book["status"] == "Read")
    unread = total - read
    return total, read, unread

# -----------------------
# Streamlit App
# -----------------------

st.set_page_config(page_title="📚 Personal Library Manager")
st.title("📚 Personal Library Manager")

menu = ["Add Book", "Remove Book", "Search Book", "View All Books", "Statistics"]
choice = st.sidebar.selectbox("Choose Action", menu)

# 1. Add Book
if choice == "Add Book":
    st.subheader("➕ Add a New Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Year Published", min_value=1000, max_value=9999, value=2023)
    genre = st.text_input("Genre")
    status = st.selectbox("Status", ["Read", "Unread"])
    if st.button("Add Book"):
        if title and author:
            add_book(title, author, year, genre, status)
            st.success(f"Book '{title}' added successfully!")
        else:
            st.warning("Please enter both title and author.")

# 2. Remove Book
elif choice == "Remove Book":
    st.subheader("🗑️ Remove a Book")
    title = st.text_input("Enter the exact title of the book to remove")
    if st.button("Remove Book"):
        remove_book(title)
        st.success(f"Book '{title}' removed successfully!")

# 3. Search Book
elif choice == "Search Book":
    st.subheader("🔍 Search for a Book")
    query = st.text_input("Enter title or author")
    if query:
        results = search_books(query)
        if results:
            st.write("### Results:")
            for book in results:
                st.write(f"- **{book['title']}** by {book['author']} ({book['year']}) — *{book['genre']}* [{book['status']}]")
        else:
            st.info("No matching books found.")

# 4. View All Books
elif choice == "View All Books":
    st.subheader("📖 Your Library")
    library = load_library()
    if library:
        for book in library:
            st.write(f"- **{book['title']}** by {book['author']} ({book['year']}) — *{book['genre']}* [{book['status']}]")
    else:
        st.info("Your library is empty.")

# 5. Statistics
elif choice == "Statistics":
    st.subheader("📊 Library Statistics")
    total, read, unread = get_stats()
    st.write(f"**Total Books:** {total}")
    st.write(f"**Read Books:** {read}")
    st.write(f"**Unread Books:** {unread}")
```

---

## 🚀 Run the Application

In your terminal, run:

```bash
streamlit run app.py
```

Streamlit will launch your app in your browser. 🎉

---

## 📂 Folder Structure

```
personal_library_manager/
│
├── app.py
├── library.json  ← created automatically when you add books
```

---

## 📦 Optional: Deploy It Online

You can deploy your app using [Streamlit Cloud](https://streamlit.io/cloud) — just upload your project and you're live!

---

## ✅ Summary

You now have a full-featured **Personal Library Manager**:
- Add and delete books
- Search by title or author
- View your full collection
- Get reading statistics

