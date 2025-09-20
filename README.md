# TO-DO-LIST

📝 To-Do List App

A simple, visually intuitive To-Do List desktop application built with Python's tkinter library. It allows users to add, complete, and delete tasks, with task persistence via a local tasks.json file.

📸 Preview

<!-- You can add your app's screenshot and rename accordingly -->

🚀 Features

✅ Add new tasks

❌ Delete tasks

🔁 Mark tasks as complete/incomplete using status icons

💾 Automatically saves tasks to a tasks.json file for persistence

🖼️ Uses images (1.png for incomplete, 2.jpg for completed tasks) for toggling task status

🛠️ Requirements

Python 3.x

tkinter (usually pre-installed with Python)

Pillow library for image handling

Install Pillow (if not installed):

pip install pillow

📂 Project Structure
├── 1.png               # Icon for incomplete task
├── 2.jpg               # Icon for completed task
├── tasks.json          # Auto-generated JSON file to store tasks
├── main.py             # Main application file
├── README.md           # This file

▶️ How to Run

Clone the repository:

git clone https://github.com/your-username/todo-app.git
cd todo-app


Ensure the required images exist:

Place two images named 1.png and 2.jpg in the same directory:

1.png → icon for incomplete task

2.jpg → icon for completed task

Run the application:

python main.py


📌 Notes

All tasks are saved locally in tasks.json

Icons are resized to 20x20 px for uniformity

Background color theme: darkseagreen with wheat-colored buttons

.

🙌 Acknowledgements

Built using Python’s tkinter

Image handling via the Pillow library
