# 🕒 Digital Clock using Tkinter in Python

A simple yet elegant digital clock built with Python’s built-in `tkinter` GUI library. This project displays the current time in real-time with a clean interface.


## 🎯 Features
- Real-time clock display (HH:MM:SS format)
- Dynamic time updates every second
- Clean and minimal GUI using Tkinter
- Automatically refreshes without freezing the window

## 🛠️ Technologies Used
- **Python 3.x**
- **Tkinter** – Python’s standard GUI library
- **time & datetime modules** – For time formatting and retrieval

## 📚 What I Learned
- Basics of GUI programming with Tkinter (`Tk()`, `Label`, `pack()`, `after()`)
- How to safely update GUI elements periodically using `after()` instead of `sleep()`
- Formatting system time using `strftime()`
- Structuring a responsive and non-blocking desktop application

## ⚠️ Challenges Faced
Initially, I used `time.sleep()` to update the clock, which froze the GUI. I learned that in GUI applications, **blocking functions like `sleep()` should be avoided**. Instead, `widget.after()` is the correct method to schedule recurring tasks — a key insight into event-driven programming!

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Digital-Clock-Tkinter-Day11.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Digital-Clock-Tkinter
   ```
3. Run the script:
   ```bash
   python Digital-Clock-Tkinter-Day11.py
   ```
## 🙌 Inspired By
Part of my #50DaysOfPython challenge to build one Python project every day and grow my programming skills.
Learned Tkinter basics from GeeksforGeeks .

### Made with ❤️ and Python
  by [Sunil Rajpurohit](https://www.linkedin.com/in/sunil-rajpurohit)
