📦 AutoPack - File Organizer CLI

A simple but effective Python CLI tool that automatically organizes messy folders by sorting files into category-based subfolders.
✨ Features

✅ Reads all files in a target folder
✅ Identifies file type by extension
✅ Automatically creates folders (Images, Documents, Music, Archives, Videos)
✅ Moves files into correct category folders
✅ Fully customizable extension mapping
💡 Why I Built This

I built AutoPack to learn real-world Python automation skills and solve a simple personal pain: a messy Downloads folder.
It's my first hands-on automation script that applies Python's os and shutil modules to do actual work.
🛠️ How It Works

1️⃣ Reads all files in a chosen folder
2️⃣ Splits file name and extension
3️⃣ Matches extension to pre-defined categories
4️⃣ Creates category folders if they don't exist
5️⃣ Moves files into the right folder
📂 Categories & Extensions
Category	Extensions
Images	.jpg, .png, .gif
Documents	.pdf, .txt, .docx
Archives	.zip, .rar, .7z
Music	.mp3, .wav
Videos	.mp4, .mkv
🚀 Usage

    ⚠️ Currently designed for personal use. Edit the source path in the script to your target folder.

python autopack.py

Example result:

/Downloads
  /Images
     selfie.jpg
  /Documents
     resume.pdf
  /Music
     song.mp3

📌 Requirements

    Python 3.x

    Standard Libraries: os, shutil

🗺️ Project Goals & Learning Outcomes

    Practice using file I/O in Python

    Learn to manipulate paths and extensions

    Automate boring manual sorting

    Understand how to use dictionaries for logic mapping

    Practice real CLI scripting for local tasks

🚧 TODO / Planned Improvements

    Take user input for source folder path

    Handle unknown file types (move to "Others" folder)

    Add logging to a .txt file

    Build CLI interface with argparse

    Package for easy reuse

🤝 Author

Revati Pangare

    Aspiring DevOps & Full Stack Developer. Currently learning Python, Java, Web Dev, and Automation tools.

📜 License

MIT License
❤️ Contributing

This project is primarily for personal learning, but feel free to fork, suggest improvements, or use it as a base for your own automation tools!
📣 Note from Me

    This is my first real-world automation script. I’m sharing it publicly as proof of my learning journey and to help others who want to automate their messy folders!