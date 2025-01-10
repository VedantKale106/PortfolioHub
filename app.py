from flask import Flask, render_template, redirect, url_for, request, session, send_file
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.secret_key = "your_secret_key"

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb+srv://vedant:lulli@portfolio.e8ky0.mongodb.net/portfolio"
mongo = PyMongo(app)

# Routes
@app.route("/")
def index():
    if "user_id" in session:
        return redirect(url_for("home"))
    return render_template("index.html")  # Login page

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])
        
        # Check if email already exists
        if mongo.db.users.find_one({"email": email}):
            return "Email already exists! Try logging in."

        mongo.db.users.insert_one({"name": name, "email": email, "password": password})
        return redirect(url_for("index"))
    
    return render_template("register.html")  # Register page

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]
    user = mongo.db.users.find_one({"email": email})
    
    if user and check_password_hash(user["password"], password):
        session["user_id"] = str(user["_id"])
        return redirect(url_for("home"))
    
    return "Invalid credentials! Please try again."

@app.route("/logout")
def logout():
    session.pop("user_id", None)
    return redirect(url_for("index"))

@app.route("/home")
def home():
    if "user_id" not in session:
        return redirect(url_for("index"))
    
    return render_template("home.html")  # Portfolio templates

@app.route("/profile", methods=["GET", "POST"])
def profile():
    if "user_id" not in session:
        return redirect(url_for("index"))
    
    if request.method == "POST":
        # Collecting the form data
        about = request.form["about"]
        name = request.form["name"]
        
        # Skills - now stored as a list
        skills = request.form.getlist("skills")  # 'getlist' allows you to capture multiple inputs
        
        # Contact information
        online_links = {
            "linkedin": request.form.get("linkedin", ""),
            "github": request.form.get("github", ""),
            "email": request.form.get("email", ""),
            "phone": request.form.get("phone", "")
        }

        # Education details
        education = {
            "course": request.form.get("course", ""),
            "college": request.form.get("college", ""),
            "year": request.form.get("year", "")
        }

        # Collecting project details dynamically
        projects = []
    project_index = 1
    while True:
        # Check if any field for the current project exists
        project_title = request.form.get(f"project_title_{project_index}")
        project_description = request.form.get(f"project_description_{project_index}")
        project_link = request.form.get(f"project_link_{project_index}")

        # Break if no project fields are present
        if not project_title and not project_description and not project_link:
            break

        # Add the project data to the list
        project = {
            "title": project_title,
            "description": project_description,
            "link": project_link
        }
        projects.append(project)
        
        # Move to the next project
        project_index += 1

        
        # Update or insert the profile data in MongoDB
        mongo.db.profiles.update_one(
    {"user_id": session["user_id"]},
    {
        "$set": {
            "name": name,  # Add the user's name here
            "about": about,
            "skills": skills,
            "online_links": online_links,
            "education": education,
            "projects": projects
        }
    },
    upsert=True
)


        return redirect(url_for("preview"))

    # Fetch existing profile data or return an empty dictionary
    profile = mongo.db.profiles.find_one({"user_id": session["user_id"]}) or {}
    return render_template("profile.html", profile=profile)  # Render the profile editor
     


@app.route("/theme", methods=["GET", "POST"])
def theme():
    if "user_id" not in session:
        return redirect(url_for("index"))
    
    if request.method == "POST":
        theme = request.form["theme"]
        mongo.db.profiles.update_one(
            {"user_id": session["user_id"]},
            {"$set": {"theme": theme}},
            upsert=True
        )
        return redirect(url_for("preview"))

    return render_template("theme.html")  # Theme selection page


@app.route("/preview")
def preview():
    if "user_id" not in session:
        return redirect(url_for("index"))
    
    profile = mongo.db.profiles.find_one({"user_id": session["user_id"]})
    if not profile:
        return redirect(url_for("profile"))
    
    # Dynamically load the selected theme
    theme = profile.get("theme", "theme1")  # Default to 'theme1'
    template_name = f"portfolio_template{theme[-1]}.html"  # Map 'theme1', 'theme2', etc.

    return render_template(template_name, profile=profile)  # Load the selected theme

@app.route("/download")
def download():
    if "user_id" not in session:
        return redirect(url_for("index"))
    
    profile = mongo.db.profiles.find_one({"user_id": session["user_id"]})
    if not profile:
        return redirect(url_for("profile"))

    # Dynamically load the selected theme
    theme = profile.get("theme", "theme1")  # Default to 'theme1'
    template_name = f"portfolio_template{theme[-1]}.html"

    # Generate the portfolio as an HTML file
    html_content = render_template(template_name, profile=profile)
    file_path = f"temp/{session['user_id']}_portfolio.html"

    # Save the HTML file
    os.makedirs("temp", exist_ok=True)
    with open(file_path, "w") as f:
        f.write(html_content)
    
    return send_file(file_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
