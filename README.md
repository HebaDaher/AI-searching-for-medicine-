# AI-searching-for-medicine-
Project Structure First (Double Check This):
Before running the app, make sure your files are organized like this:

paradigm project/
├── ai_medicine_bot.py
├── med_knowledge.pl
└── templates/
    ├── index.html
    ├── results.html
    └── not_found.html
✅ Step-by-Step Guide to Run It:
📁 1. Open Your Project in VS Code:

Open VS Code
Click File → Open and choose your paradigm project folder.
🖥️ 2. Open Terminal in VS Code:

Press Ctrl + ` (the backtick key)
Or go to Terminal → New Terminal
⏩ 3. Make sure you’re in the right folder:

cd ~/Desktop/paradigm\ project
(Or wherever your folder is)

🧪 4. Run your Flask app:

python3 ai_medicine_bot.py
If everything is correct, you should see:

 * Running on http://127.0.0.1:5050/
🌐 5. Open the app in your browser:

Go to: http://127.0.0.1:5050
You’ll see your form!
Enter a symptom (like headache or cough) and press submit.
If you set it up as explained, it will return a list of recommended medicines with “Buy Now” links.
