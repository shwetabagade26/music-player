# 🎵 Django Music Player

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.1-092E20?style=for-the-badge&logo=django&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-Green?style=for-the-badge&logo=gunicorn&logoColor=white)

A full-featured, web-based music player application built with **Django**. This project allows users to upload their favorite audio tracks, create and manage custom playlists, and experience real-time synced lyrics.

---

## ✨ Features

- **🎧 Audio Management:** Seamlessly upload, store, and stream audio files utilizing Django's robust media handling capabilities.
- **📂 Playlist Creation:** Organize your music library by building and managing custom playlists.
- **🖼️ Album Art Support:** Integrated with `Pillow` for optimized image processing and cover art uploads.
- **🚀 Production Ready:** Configured with WSGI settings and `Gunicorn` for smooth deployment and static file handling.

---

## 🛠️ Tech Stack

- **Backend:** Python, Django 6.1
- **Image Processing:** Pillow
- **Web Server:** Gunicorn
- **Environment:** Python `venv`, Custom Requirements
- **Frontend Utilities:** Custom LRC-to-JSON parser, HTML5 Audio API

---

## 🚀 Getting Started

Follow these steps to set up the project locally. 

### Prerequisites
Make sure you have **Python 3.x** installed on your machine.

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/shwetabagade26/music-player.git](https://github.com/shwetabagade26/music-player.git)
   cd music-player
2. **Set up a virtual environment:**
    ```bash
    python -m venv venv

    # On Windows
    venv\Scripts\activate

    # On macOS/Linux
    source venv/bin/activate
3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
4. **Apply database migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
5. **Create a superuser (to access the admin panel for uploading songs):**
    ```bash
    python manage.py createsuperuser
6. **Run the development server:**
    ```bash
    python manage.py runserver
7. **Access the application:**
    ```bash
    Open your browser and navigate to http://127.0.0.1:8000. Access the admin panel at http://127.0.0.1:8000/admin to start uploading your audio and LRC files.

