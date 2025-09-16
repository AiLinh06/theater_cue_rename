# 🎭 Theater Cue Organizer

A simple Python + Tkinter app to **rename audio files into numbered theater cues** and **export a cue list (CSV)**.  
Designed for small theater productions where each scene/act needs neatly ordered sound cues.

---

## ✨ Features
- Rename `.mp3` and `.wav` files into a consistent format:
SceneName_Cue01.mp3
SceneName_Cue02.mp3
SceneName_Cue03.mp3

- Export a CSV cue list with:
- Cue Number
- File Name
- Simple GUI for folder selection and scene naming.
- Prevents filename conflicts with a safe two-step renaming process.

---

1. Make sure you have **Python 3.8+** installed.
2. Clone this repository:
 ```bash
 git clone https://github.com/AiLinh06/theater_cue_rename.git
 cd theater-cue-rename

 ```
## **Usage**

1. Place your raw audio files (`.mp3` or `.wav`) into a folder.  
   Example:  
   ```
   ./cue_folder/
       intro_music.mp3
       thunder.wav
       door_knock.mp3
   ```

2. Run the app:
   ```
   python main.py
   ```

3. In the GUI:
- Click **Browse** to select your folder.  
- Enter a **Scene Name** (e.g., `Act1` or `Scene2`).  
- Click **Rename and Export Cue List**.  

4. Result:  
Files are renamed inside the folder:
```
./cue_folder/
  Act1_Cue01.mp3
  Act1_Cue02.mp3
  Act1_Cue03.mp3
```
5. A csv file is created
```
Act1_cue_list.csv
```
