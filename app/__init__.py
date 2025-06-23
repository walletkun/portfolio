import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


WORK_EXPERIENCES = [{
        'title': "Full Stack Developer Intern",
        'company': "ERBuddy Inc.",
        'duration': "June 2025 - On going",
        'description' : ["Developed 5+ reusable React Native components reducing code duplication by 60% and improving development \
    velocity.", "Built comprehensive symptom tracking feature supporting 6 core symptoms with drag-to-prioritize functionality enabling users to log health data 50% faster.", 
    "Implemented dynamic medication reminder system serving 100% of user pill schedules with real-time status \
    updates.", "Resolved 10+ UI/UX bugs including text overflow and layout spacing issues within 2-week sprint cycles."],
    },
    {
        'title': "Site Reliability Engineer Fellow",
        'company': "META & MLH Fellowship",
        'duration': "June 2025 - On going",
        'description': ["Still on going"]
    },
    {
        'title': "Software Engineer Fellow",
        "company": "Cuny Tech Prep",
        'duration': "October 2024 - May 2025",
        'description': ["1 of 170 students selected for a Data Science and Software Engineering fellowship designed to jumpstart careers in tech","Engaged in weekly courses to learn and apply industry best practices, including MVC architecture, version control with \
Git/GitHub, Agile & Scrum methodologies using Trello and Slack, test-driven development (TDD), and CI/CD pipelines",
"Implemented a CNN-based facial recognition to analyze user emotions to create an AI-powered song recommendation system"]
    },
]

LEADERSHIP_EXPERIENCES = [
        {
        'title': "Basta Fellow",
        'company': "Basta",
        "duration": "May 2025 - On going",
        'description': ["Selected to participate in a rigorous 10-week career prep fellowship program followed by ongoing weekly coaching designed to support first-generation college students in landing a great entry-level position"],
        },
        {
            'title': "Software Engineer Fellow",
            "company": "Google X Basta",
            'duration': "January 2025 - May 2025",
            "description": ["Selected as one of 1200+ applicants to participate in developing advanced solutions for complex algorithmic problems and \
            mock interviews to enhance career readiness" , "Achieved a high acceptance on medium-difficulty problems and increased confidence in technical interview performance by \
            completing data structures and algorithm challenges on code signal in one month"]
        },
]

ACTIVITIES = [
    {
        "title": "Campus Advocate",
        'company': "Defang",
        "duration" : "March 2025 - On going",
        "description": ["Selected as a Defang Campus Advocate to promote cloud-native development, streamlined cloud deployments, and advocate \
        for modern cloud deployment practices to students and developers"]
    },
    {
        'title': "Volunteer Software Engineer",
        'company': "Ruby for good",
        'duration': "January 2025 - On going",
        'description': ["Volunteering at Ruby for good to gain open source exposure and working consistently with senior developers during the program"]
    }
]

EDUCATION = [
    {
        'degree': "Bachelor of Science with minor in Data Science",
        'instituition': "Brooklyn College",
        'duration': "2022- 2025",
        'courses_taken': ['Data Structures and Algorithm' , 
                          'Artificial Intelligence',
                          'Machine Learning', 
                          'Software Engineering'],
    }
]


TECHNOLOGIES = [
    {"Languages": ['Python', 'Javascript', 'Typescript', 'Java', 'C/C++']},
    {'Design Tools': ['HTML', 'CSS']},
    {'Frameworks / Libraries': ['React', 'Next.js', 'Node.js', 'Flask', 'Django', '.Net', 'Pandas', 'Numpy', 'Tailwind CSS', 'Springboot', 'Bootstrap']},
    {'Developer Tools': ['Git', 'Postman', 'Jira', 'Bash', 'Docker', 'Kubernetes']},
    {'Database Management': ['SQL', 'Supabase', 'Firebase', 'MySQL', 'PostgreSQL', 'MongoDB']},
]



PROJECTS = [
    {
        'title': 'Alexandria Digital Library',
        'role': 'Full Stack Developer',
        'description': '',
        'link': '',
    },
    {
        'title': 'Emotionfy',
        'role': "Full Stack and ML Engineer",
        'description': "",
        'link': ''
    },
]







@app.route('/')
def index():
    return render_template('index.html', 
                           title="Fei Lin - MLH Fellow", 
                           work_experiences=WORK_EXPERIENCES[:2],
                           education=EDUCATION,
                           url=os.getenv("URL"))

# About me section
@app.route('/about_me')
def about():
    return render_template('about.html', title='About Me')

# Experience section
@app.route('/experience')
def experience():
    return render_template('experience.html', 
                           title="Fei Lin - Experience", 
                           work_experiences=WORK_EXPERIENCES,
                           leadership_experiences=LEADERSHIP_EXPERIENCES,
                           activities=ACTIVITIES,
                           url=os.getenv("URL"))