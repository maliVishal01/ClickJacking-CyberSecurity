## 🔒 Clickjacking Awareness
This project demonstrates how **clickjacking attacks** can trick users into clicking hidden elements.  
- A hidden camera frame is placed behind a button.  
- When clicked, user data (IP, location, browser info) is captured and sent to the server.  
- Both `index` and `next` pages are uniquely designed to show how attackers can manipulate user flow.  

⚠️ **Disclaimer:** This project is for **educational and cybersecurity awareness purposes only**. It should not be used for malicious activities.
Got it 👍 — you want a **README.md** file for your GitHub project that explains your Flask + HTML/CSS application which captures user data (like browser info, location, etc.), hides a camera frame behind a button, and stores the data on your server across unique index and next pages.  

# 📊 User Data Capture Web App (Flask + HTML/CSS)

## 📌 Overview
This project is a **Flask-based web application** with a simple **HTML/CSS frontend** that demonstrates how to capture client-side information and send it securely to a server.  
It collects details such as:
- Timestamp  
- IP address  
- Location (city, region, country, latitude, longitude)  
- Browser information (user agent, platform, screen size, language)  
- Battery status (level, charging state)  
- Device details  

Additionally, the app includes a **hidden camera frame behind a button** to simulate how user interactions can trigger additional data capture events.

---

## ⚙️ Features
- **Flask backend** for handling requests and storing data.  
- **HTML/CSS frontend** with interactive buttons and hidden camera frame.  
- **Unique pages** (`index` and `next`) to demonstrate multi-page data flow.  
- **Data logging** to server for analysis and visualization.  
- **Lightweight design** suitable for demos, learning, and awareness projects.  

---

## 🛠️ Tech Stack
- **Backend:** Flask (Python)  
- **Frontend:** HTML, CSS  
- **Data Handling:** JSON, Flask request objects  
- **Environment:** Works on Linux/Windows with Python 3.x  

---

## 🚀 How It Works
1. User opens the app in their browser.  
2. The frontend captures client information (IP, location, browser, device, etc.).  
3. A hidden camera frame is placed behind a button (for demo purposes).  
4. Data is sent to the Flask server and logged.  
5. Both `index` and `next` pages have **unique identifiers** to track user flow.  

---

## 📂 Project Structure
```
project/
│── app.py              # Flask backend
│── templates/
│   ├── index.html       # First page with hidden camera frame
│   ├── next.html        # Second page with unique data capture
│── static/
│   ├── style.css        # Custom CSS
│── data/                # Logs or captured data
│── README.md            # Project documentation
```

---

## 🔒 Disclaimer
This project is built **for educational and awareness purposes only**.  
It demonstrates how client-side data can be captured and logged in a server environment.  
It should **not** be used for malicious tracking or unauthorized surveillance.  

---

## 📈 Future Improvements
- Add **SQL/NoSQL database integration** for structured storage.  
- Build **visual dashboards** (Power BI / Tableau / Matplotlib) for captured data.  
- Implement **user consent and privacy controls**.  
- Extend to **real-time analytics** with WebSockets.  

---

## 👨‍💻 Author
**Mali Vishal**  
Final-year MSc Information Technology student | Aspiring Data Analyst & Python Developer  
```

---
