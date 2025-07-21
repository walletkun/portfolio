import os
from flask import Flask, render_template, request, redirect, flash
from dotenv import load_dotenv
from peewee import *
from datetime import datetime
from playhouse.shortcuts import model_to_dict
import re


load_dotenv()
app = Flask(__name__)
# Allowing flash to work
app.config['SECRET_KEY'] = 'your-generated-key-here'


#flip between sqlite and mysql
if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
    )
print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.now())

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])




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


HOBBIES = [
    {
        "name": "Snowboarding",
        "icon": "fas fa-snowboarding",
        "description": "Love hitting the slopes and carving through fresh powder during winter seasons!",
    },
    {
        "name": "Creating Projects",
        "icon": "fas fa-code",
        "description": "Building innovative solutions and experimenting with new technologies in my spare time.",
    },
    {
        "name": "Photography",
        "icon": "fas fa-camera",
        "description": "Capturing moments and beautiful landscapes through the lens of my camera.",
    },
    {
        "name": "Hiking",
        "icon": "fas fa-mountain",
        "description": "Exploring nature trails and discovering scenic views while staying active outdoors.",
    },
]


# Validation for name and email inputs
def name_validation(name):
    """Validating the name of user trying to comment on Guest book"""
    if not name or len(name.strip()) < 2 or len(name.strip()) > 50:
        return False

    return re.match(r'^[a-zA-Z\s]+$', name.strip())

def email_validation(email):
    """Validating the email of user commenting on guest book"""
    if not email or '@' not in email: #adding a check for missing @
        return False

    return re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email.strip())



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
                            title="Experience", 
                            work_experiences=WORK_EXPERIENCES,
                            leadership_experiences=LEADERSHIP_EXPERIENCES,
                            activities=ACTIVITIES,
                            url=os.getenv("URL"))


# Hobbies section
@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html', 
                            title="Hobbies",
                            hobbies=HOBBIES)

# Time line blog section
@app.route("/timeline")
def timeline():
    # Getting all the guest book comments in descending order
    timeline_posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())
    return render_template("timeline.html", title="Guestbook", timeline_posts=timeline_posts)


# add endpoint of the post timeline
@app.route('/api/timeline_post', methods=["POST"])
def post_timeline_post():
    try:
        name = request.form.get('name', "").strip()
        email = request.form.get('email', "").strip()
        content = request.form.get('content', "").strip()


        print(f"Name: '{name}', Email: '{email}', Content: '{content}'")
        print(f"Content length: {len(content)}")


        # validation
        errors = []

        if not name_validation(name):
            #errors.append("Name should only contain letters and spaces (2-50 characters)")
            return "Invalid name", 400
        if not email_validation(email):
            #errors.append("Please enter a valid email address")
            return "Invalid email", 400
        if not content or len(content) < 5:
            #errors.append("Message must be at least 5 characters long")
            return "Invalid content", 400
        print(f"Validation errors: {errors}")

        # if any error was caught we will flash it
        if errors:
            for error in errors:
                flash(error, 'error')

            # Don't refresh the page when error was encountered we'll render with content preserved
            timeline_posts = TimelinePost.select().order_by(TimelinePost.created_at.desc())

            return render_template('timeline.html', 
                                 title="Guestbook", 
                                 timeline_posts=timeline_posts,
                                 form_data={'name': name, 'email': email, 'content': content})
            
        # Then if the validation passes we'll create the post
        timeline_post = TimelinePost.create(name=name, email=email, content=content)
        flash("Your comment has been posted successfully", 'success')
        #return redirect("/timeline") #redirects use status code 302, which is not what we want here
        return {"message": "Post created successfully", "post_id": timeline_post.id}, 200 
        #just returning a success message with post id. ensures 200 status
    except Exception as e:
        print("Error", str(e))
        print("Exception type:", type(e).__name__)
        flash('An error occurred. Please try again.', 'error')
        #return redirect('/timeline')
        return {"message": "An error occurred while creating the post"}, 500

# get end point of the time line
@app.route('/api/timeline_post', methods=['GET'])
def get_timeline_post():
    return {
        'timeline_post': [
            model_to_dict(post) for post in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }


