import smtplib
import requests
from bs4 import BeautifulSoup
from email.message import EmailMessage

# Configuration
KEYWORDS = ["business analyst", "data analyst", "project coordinator"]
LOCATION = "Budapest"
YOUR_EMAIL = "youremail@example.com"
YOUR_PASSWORD = "yourpassword"  # ⚠️ Use environment variables in real apps!
CV_FILE_PATH = "cv.pdf"

# Function to search jobs from a placeholder job board (modify this!)
def search_jobs():
    print("🔍 Searching for jobs...")
    job_listings = []
    url = f"https://example-jobboard.com/jobs?location={LOCATION.replace(' ', '+')}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    for job in soup.select(".job-posting"):
        title = job.select_one(".title").text.lower()
        link = job.select_one("a")["href"]
        if any(keyword in title for keyword in KEYWORDS):
            job_listings.append({"title": title, "link": link})
    
    return job_listings

# Function to send your application via email
def send_application(job):
    print(f"📨 Sending application for: {job['title']}")
    
    msg = EmailMessage()
    msg["Subject"] = f"Application for {job['title'].title()}"
    msg["From"] = YOUR_EMAIL
    msg["To"] = "hr@examplecompany.com"  # Replace with job contact or extract dynamically

    msg.set_content(f"""
Dear Hiring Manager,

I am writing to express my interest in the position of {job['title'].title()}.

Please find my CV attached. I would be grateful for the opportunity to further discuss how I can contribute to your team.

Best regards,
Richard
    """)
    
    with open(CV_FILE_PATH, "rb") as f:
        msg.add_attachment(f.read(), maintype="application", subtype="pdf", filename="cv.pdf")
    
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(YOUR_EMAIL, YOUR_PASSWORD)
        smtp.send_message(msg)

# Main flow
if __name__ == "__main__":
    jobs = search_jobs()
    
    if not jobs:
        print("😔 No matching jobs found today.")
    else:
        for job in jobs:
            send_application(job)
            print(f"✅ Applied to: {job['title']} - {job['link']}")

    print("✨ Job application automation finished!")
