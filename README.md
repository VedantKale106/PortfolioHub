# PortfolioHub - Dynamic Portfolio Template 🚀

**PortfolioHub** is a customizable, dynamic portfolio template designed to showcase your skills, projects, and achievements with a sleek, modern, and responsive interface. This project is built using **Flask** for the backend, **MongoDB** for data storage, and a combination of **HTML**, **CSS**, and **JavaScript** for the front end.

---

### 🌟 Features:
- **Responsive Design** 📱: Optimized for all devices.
- **Dynamic Content** 🔥: Display your profile, skills, projects, and more from MongoDB.
- **Easy Customization** 🎨: Make the design your own by tweaking styles, colors, and layout.
- **Simple Setup** ⚙️: Get started in minutes and personalize easily.

---

### 🔧 Prerequisites:
- **Python 3.x** (for running the Flask application)
- **MongoDB** (either locally or accessible remotely)
- **Pipenv** or **virtualenv** (optional for environment setup)

---

### 🚀 Quick Start:

1. **Clone the Repository**:
   \`\`\`bash
   git clone https://github.com/VedantKale106/PortfolioHub.git
   
   cd portfoliohub
   \`\`\`

3. **Set Up a Virtual Environment** (Optional):
   Using **virtualenv**:
   \`\`\`bash
   virtualenv venv
   
   source venv/bin/activate  # Linux/Mac
   
   venv\Scripts\activate     # Windows
   \`\`\`

5. **Install Dependencies**:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

6. **Configure MongoDB**:
   - Start MongoDB locally or connect to a remote server.
   - Create a database named **portfoliohub** and a collection called **profiles**.
   - Insert a sample user profile in **JSON** format:
   
   \`\`\`json
   {
     "name": "Your Name",
     "about": "A brief introduction about yourself.",
     "skills": ["Python", "HTML", "CSS", "Flask"],
     "projects": [
       {
         "title": "Project Title",
         "description": "Project description goes here.",
         "link": "https://github.com/your-repo"
       }
     ],
     "education": {
       "course": "B.Tech in Computer Science",
       "college": "Your College",
       "year": "2025"
     },
     "contact_info": {
       "phone": "+123456789",
       "linkedin": "https://linkedin.com/in/your-profile",
       "github": "https://github.com/your-username",
       "email": "your.email@example.com"
     }
   }
   \`\`\`

7. **Start the Flask Application**:
   \`\`\`bash
   python app.py
   \`\`\`
   The application will be accessible at: \`http://127.0.0.1:5000/\`.

---
### 📝 For Fellow Developers If you want to give your own template, Please Refer /templates/themes/generic.html file. Instructions are given there

### 💡 How to Customize Your Portfolio:

The dynamic content is rendered from the **MongoDB** database using **Jinja syntax**. You can easily change the following sections:

- **profile.name** - Your name (e.g., \`{{ profile.name }}\`)
- **profile.about** - About you (e.g., \`{{ profile.about }}\`)
- **profile.skills** - List of your skills (e.g., \`{{ profile.skills }}\`)
- **profile.projects** - Show off your projects (e.g., \`{{ profile.projects }}\`)
- **profile.education** - Your educational background (e.g., \`{{ profile.education }}\`)
- **profile.contact_info** - Contact details (e.g., \`{{ profile.contact_info }}\`)

---

### 🎨 Customize Your Template:

- **Write CSS in the Body Tag**: To ensure the page downloads with proper styling, write your CSS inside the body tag.
- **Floating Sidebar**: Add the floating sidebar code at the end of your HTML file for a clean download option.
- **Mobile Responsiveness**: Make sure your design works beautifully on all devices. Check your design's responsiveness.
- **Content**: Feel free to add new sections, content, or features that will enhance your portfolio.
- **Colors & Fonts**: Don't hesitate to tweak the colors, fonts, and layout to make your portfolio truly yours!

---

### 📝 Usage:

- Visit the local server URL (\`http://127.0.0.1:5000/\`) to see your dynamic portfolio.
- Modify your MongoDB database to update the profile information dynamically on the frontend.
- Use the **floating sidebar** to download your customized portfolio HTML page.

---

### 🤝 Contribution:

We welcome contributions! Here's how you can contribute:

1. **Fork** the repository.
2. Create a **feature branch** (\`git checkout -b feature-name\`).
3. **Commit** your changes (\`git commit -m 'Added feature XYZ'\`).
4. **Push** to the branch (\`git push origin feature-name\`).
5. Open a **pull request** to submit your changes.

---

### 🛡️ License:

Sorry No License

---

### 📞 Need Help?

If you run into issues or have questions, feel free to create an issue in the repository or reach out via email.

---

### 🎉 Happy Coding!

We can’t wait to see what you create with **PortfolioHub**. Make it your own, and show the world your amazing work! 😎

---

### 💬 Special Notes:
- **Contact Section**: Do not add backend logic for the contact form. Just include the section as part of the UI.
- **Customization Reminder**: It’s your template, so feel free to get creative and showcase your style! 🎨
