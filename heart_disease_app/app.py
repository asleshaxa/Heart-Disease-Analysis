from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Heart Disease Data
dashboard_data = {
    "gender": {
        "labels": ["Female", "Male"],
        "no_disease": [2377, 1640],
        "with_disease": [277, 226],
        "title": "Gender vs Heart Disease"
    },
    "race": {
        "labels": ["White", "Black", "Asian", "Hispanic", "Other", "American Indian"],
        "values": [70.47, 24.16, 2.92, 1.52, 0.79, 0.14],
        "colors": ["#f9c74f", "#3B5BDB", "#f97316", "#4cc9f0", "#7c3aed", "#10b981"],
        "title": "Race wise Heart Disease"
    },
    "smoking_alcohol": {
        "labels": ["No Smoke / No Alcohol", "Smoke Only", "Alcohol Only", "Smoke + Alcohol"],
        "values": [1200, 1850, 980, 2450],
        "title": "Impact of Smoking and Alcohol on Heart Disease"
    },
    "diabetic_stroke": {
        "categories": ["No Diabetes / No Stroke", "Diabetes / No Stroke", "No Diabetes / Stroke", "Diabetes + Stroke"],
        "no_disease": [2800, 620, 180, 95],
        "with_disease": [380, 280, 75, 65],
        "title": "Diabetic vs Stroke"
    },
    "age_diabetes": {
        "age_groups": ["35-44", "45-54", "55-64", "65-74", "75-79", "80+"],
        "diabetic": [120, 380, 720, 950, 480, 210],
        "non_diabetic": [890, 1200, 1450, 1100, 560, 280],
        "title": "People Suffering from Diabetes within Age Category"
    },
    "physical_activity": {
        "labels": ["Active", "Inactive"],
        "no_disease": [3100, 1200],
        "with_disease": [280, 620],
        "title": "Effect of Physical Activity on Heart Disease"
    }
}

story_steps = [
    {
        "id": 1,
        "title": "Gender suffering from Heart Disease",
        "description": "Female vs male breakdown of heart disease diagnoses. Females show higher absolute numbers (2,377 no disease / 277 with disease) compared to males (1,640 / 226).",
        "chart": "gender",
        "insight": "Females represent a slightly higher proportion of heart disease cases in this dataset."
    },
    {
        "id": 2,
        "title": "Effect of Physical Activity on Heart Disease",
        "description": "How exercise habits and physical activity levels correlate with cardiovascular risk. Inactive individuals show significantly higher rates of heart disease.",
        "chart": "physical_activity",
        "insight": "Inactive patients are 2.2x more likely to have heart disease than active patients."
    },
    {
        "id": 3,
        "title": "Diabetes Affecting Heart Disease",
        "description": "The relationship between diabetic status and heart disease. Diabetic patients show disproportionately higher rates of cardiovascular complications.",
        "chart": "diabetic_stroke",
        "insight": "Diabetic patients account for 45% of heart disease cases despite being a smaller proportion of the study population."
    },
    {
        "id": 4,
        "title": "Impact of Smoking and Alcohol on Stroke",
        "description": "Combined smoking and alcohol use dramatically increases cardiovascular risk, with the highest disease rates seen in patients who both smoke and drink.",
        "chart": "smoking_alcohol",
        "insight": "Combined smokers and drinkers show the highest heart disease counts at 2,450 cases."
    },
    {
        "id": 5,
        "title": "Diversity-wise Heart Disease Count",
        "description": "Racial and ethnic distribution of heart disease, revealing disparities. White patients represent 70.47% of cases, with Black patients at 24.16%.",
        "chart": "race",
        "insight": "Racial disparities highlight the need for targeted cardiovascular interventions in underrepresented communities."
    },
    {
        "id": 6,
        "title": "People Suffering from Diabetes within Age Category",
        "description": "Age-stratified view of diabetes prevalence. The 65-74 age group has the highest diabetic count, while younger groups (35-44) show the lowest.",
        "chart": "age_diabetes",
        "insight": "Diabetes risk peaks in the 65-74 age group, correlating with the highest heart disease risk in that demographic."
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', data=dashboard_data)

@app.route('/story')
def story():
    return render_template('story.html', steps=story_steps, data=dashboard_data)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/api/data')
def api_data():
    return jsonify(dashboard_data)

@app.route('/api/story')
def api_story():
    return jsonify(story_steps)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
