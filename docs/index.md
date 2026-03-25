# 🚀 Techdocs: MkDocs Project

This repository contains technical documentation built using **Python 3**, **MkDocs**, and the **Material theme**. It follows a professional development workflow to ensure the project is isolated, clean, and easy to collaborate on.

## 🧠 Why we chose this Setup

We deliberately avoided the "quick" web-based setup to ensure a robust local development environment:

* **Virtual Environment (`venv`):** We created a local "sandbox." This keeps the project's dependencies (like MkDocs) separate from your computer's global Python settings, preventing version conflicts.
* **The Root `.gitignore`:** We explicitly told Git to ignore the `venv/` folder. We don't share the "engine" (the thousands of files that run Python); we only share the **content** (`docs/`) and the **blueprints** (`mkdocs.yml`).
* **Manual GitHub Initialization:** We unchecked the default "Add README/Gitignore" options on GitHub Web. This allowed us to push our local "Source of Truth" to the cloud without "Merge Conflicts" (where the cloud and your computer disagree on history).

---

## 🛠 Installation & Local Setup

If you are a new user or moving to a new machine, follow these steps to get the environment running:

### 1. Clone the Repository
```bash
git clone https://github.com/NutantShailesh/Techdocs.git
cd Techdocs
```

### 2. Create and Activate the Virtual Environment
```bash
# Create the sandbox
python3 -m venv venv

# Activate (Mac/Linux)
source venv/bin/activate

# Activate (Windows)
.\venv\Scripts\activate
```

### 3. Install Dependencies
Instead of installing tools one by one, use the provided requirements file:
```bash
pip install -r requirements.txt
```

---

## ✍️ How to Contribute

To make changes or add new documentation:

1.  **Start the Preview Server:**
    ```bash
    mkdocs serve
    ```
    View your live changes at `http://127.0.0.1:8000`.

2.  **Edit Content:**
    * Add or edit Markdown files in the `docs/` folder.
    * Update the `nav` section in `mkdocs.yml` if you add new pages.

3.  **Sync Changes to GitHub:**
    
    ```bash
    git add .
    git commit -m "Brief description of your changes"
    git push origin main
    ```

---

## 📂 Project Structure
* `docs/`: The Markdown source files for the documentation.
* `mkdocs.yml`: The main configuration file (Theme, Nav, Plugins).
* `requirements.txt`: The list of Python packages required for this project.
* `.gitignore`: Prevents temporary and environment files from being uploaded.

---