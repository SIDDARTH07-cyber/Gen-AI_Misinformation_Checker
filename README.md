# Gen-AI_Misinformation_Checker

AI-Powered Misinformation Detection Tool
 Project Overview:
We are a team of students who created this project as part of a competition. The problem we wanted to solve is the spread of misinformation. Today, so much fake news and misleading information is shared online, and it is very hard for normal people to know whether something is true or false.
So, we built a simple prototype website that takes a piece of information (like a news sentence or claim) from the user and checks whether it is:
✅ True / Accurate
❌ False / Misleading
❓ Uncertain / Needs more context
Our tool uses AI in the background to analyze the given text and provide a judgment.
Our Goal:
To make a basic working system that shows how AI can be used to detect misinformation.
To give users a very simple way (just copy and paste the news) to check the truthfulness.
To build this as students, without making it too complex, but still good enough to demonstrate in the competition.
Technologies Used:
We used the following tools and languages in our project:
Python (Flask Framework) → For building the backend of the website.
HTML & CSS → For the frontend design (user interface).
Google Generative AI (Gemini API) → For checking whether the text is true, false, or uncertain.
Environment Variables (.env file) → For keeping our API key secret.
 How We Built It (Step by Step):
Set up Python environment
Created a virtual environment.
Installed Flask and Google AI libraries.
Backend (app.py)
Wrote a Flask app that receives user input from the webpage.
Sent this input to the Gemini AI model for analysis.
Got the response back (True / False / Uncertain).
Frontend (HTML file)
Designed a simple webpage with a text box where the user pastes news or claims.
Added a button that sends the text to the backend.
Displayed the AI’s response nicely on the page.
Connecting Everything
Linked frontend and backend using Flask routes.
Tested with sample statements (true, false, uncertain).
Key Features:
Easy to use: just paste text and click Check.
AI-powered: uses real AI models to check truthfulness.
Shows results in a clear way.
Prototype built by students, but works like a demo version of a bigger system.
USP (Unique Selling Point):
Our tool is simple, fast, and focused. While other tools are often complex or full of features, we wanted to make something anyone can use immediately. It doesn’t need technical knowledge, and it shows that even students can build a working AI-powered solution for misinformation.
Team Work (5 Members):
We divided the work among 5 members so each of us contributed:
Research → Understanding misinformation and how AI can help.
Backend Development → Writing Python Flask code.
Frontend Design → Creating HTML & CSS interface.
AI Integration → Connecting with Gemini AI model.
Testing & Deployment → Running on local server, later preparing for hosting.
How to Run the Project:
Clone this repository.
Create a virtual environment and activate it.
Install dependencies:
pip install flask google-generativeai python-dotenv
Add your Gemini API key to a file named .env:
GOOGLE_API_KEY=your_api_key_here
Run the app:
python3 app.py
Open browser at http://127.0.0.1:9000
Conclusion:
This is just a prototype project. It is not 100% perfect, but it shows how we can fight misinformation with AI. With more time and resources, this can be developed into a full website or even a mobile app that helps people quickly verify news and information.


![Image](https://github.com/user-attachments/assets/b473427f-399a-43d9-a865-f7d1953be309)
![Image](https://github.com/user-attachments/assets/6aa5fae2-8668-4f54-8a3c-95506185792a)

![Image](https://github.com/user-attachments/assets/49daee5e-9b64-43ba-bcf2-283d5c8a31a2)

![Image](https://github.com/user-attachments/assets/63741ed8-2b54-4c5b-b698-b0c1bb76f008)
