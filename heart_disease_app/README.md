# Heart Disease Analysis — Flask Web Application

A full Flask web application for visualizing heart disease risk factors through interactive Chart.js dashboards and a guided story walkthrough.

## Project Structure

```
heart_disease_app/
├── app.py                  # Flask application & routes
├── requirements.txt        # Python dependencies
└── templates/
    ├── base.html           # Shared navbar, footer, layout
    ├── index.html          # Home page with hero & features
    ├── about.html          # About page with methodology
    ├── dashboard.html      # Full analytics dashboard (6 charts)
    ├── story.html          # 6-step guided story
    └── contact.html        # Contact page with form
```

## Pages

| Route        | Description                                      |
|--------------|--------------------------------------------------|
| `/`          | Home — hero, feature overview, mini chart        |
| `/about`     | About — project info, risk factors, methodology  |
| `/dashboard` | Dashboard — 6 interactive Chart.js visualizations |
| `/story`     | Story — 6-step guided narrative with charts      |
| `/contact`   | Contact — links, GitHub, message form            |
| `/api/data`  | JSON API — dashboard data                        |
| `/api/story` | JSON API — story steps                           |

## How to Run

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run the app:
   ```bash
   python app.py
   ```

3. Open your browser at: **http://127.0.0.1:5000**

## Charts Included

- **Gender vs Heart Disease** — Grouped bar chart
- **Diabetic vs Stroke** — Grouped bar chart  
- **Race wise Heart Disease** — Pie chart
- **Smoking & Alcohol Impact** — Horizontal bar chart
- **Physical Activity Effect** — Doughnut chart + progress bars
- **Age & Diabetes** — Stacked bar chart

## GitHub

https://github.com/asleshaxa/Heart-Disease-Analysis
