# Auto Job Application Script

This Python script helps you **automatically search and apply** for jobs based on your preferred keywords and location. It scrapes job listings from a job board (you’ll need to plug in a real one), filters the results, and sends out applications with your CV via email.

## 🔧 What It Does

- Scrapes job listings using BeautifulSoup
- Filters listings by keywords like "business analyst" or "data analyst"
- Sends application emails with your CV attached
- Can be extended to use Selenium for job portals that need form-filling

## ⚙️ Requirements

- Python 3.8+
- Install dependencies:

```bash
pip install beautifulsoup4 requests
```

## ✍️ How to Use

1. Open the script.
2. Add your email credentials (preferably via environment variables).
3. Set your preferred `KEYWORDS`, `LOCATION`, and path to your `cv.pdf`.
4. Replace the dummy job board URL with a real one (like `profession.hu`, `indeed.com`, etc.).
5. Run it:

```bash
python auto_apply.py
```

## 📁 File Structure

```
auto_apply.py       # Main script
cv.pdf              # Your résumé (needs to be in the same folder or update the path)
```

## ⚠️ Notes

- The job board used in the code is a placeholder. You'll need to find a real one that can be scraped or has an API.
- Don’t hardcode your email password. Use environment variables or a `.env` file with `python-dotenv`.
- Sending a ton of applications in one go might get you flagged, so... be gentle 😉

## 🚀 To-Do Ideas

- Add a GUI (maybe with Streamlit or Tkinter)
- Track applied jobs in a local database (SQLite)
- Add Telegram notifications
- Support for uploading directly to job portals (using Selenium)

## 🤝 Contributing

If you’ve got improvements or want to expand this into a proper app — feel free to fork and open a pull request!

---

Built with ☕, Python, and a bit of job-hunting frustration.
