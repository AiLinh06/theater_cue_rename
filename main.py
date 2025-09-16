import os
import csv  
import tkinter as tk
from tkinter import filedialog, messagebox

#----GUI Setup----#
root = tk.Tk()
root.title("Theater Cue Organizer")
root.geometry("500x200")

folder_path_var = tk.StringVar()
scene_name_var = tk.StringVar()



#--------------- Core Functionality ---------------#
def list_audio_files(folder_path):
    return [f for f in os.listdir(folder_path) if f.lower().endswith((".wav", ".mp3"))]


def rename_cues(folder_path, scene_name= "Scene1"):
    files = list_audio_files(folder_path)
    files.sort()  # Ensure the files are in order
    renamed ={}

    temp_mapping = {}
    for index, file in enumerate(files, start=1):
        file_ext = os.path.splitext(file)[1]
        new_name = f"{scene_name}_Cue{index:02d}{file_ext}"
        
        temp_mapping[file] = new_name

    for old_name, new_name in temp_mapping.items():
        old_path = os.path.join(folder_path, old_name)
        temp_path = os.path.join(folder_path, f"__temp__{new_name}")
        if os.path.exists(temp_path):
            os.remove(temp_path)  # delete if leftover from previous run
        os.replace(old_path, temp_path)

    for old_name, new_name in temp_mapping.items():
        temp_path = os.path.join(folder_path, f"__temp__{new_name}")
        final_path = os.path.join(folder_path, new_name)
        if os.path.exists(final_path):
            os.remove(final_path)  # delete old file if already there
        os.replace(temp_path, final_path)
        renamed[old_name] = new_name
    
    return renamed
        

rename_cues("cue_folder", "Act1")  # Renames audio files in the cue_folder directory with the prefix "Act1"


def export_cue_list_to_csv(folder_path, scene_name="Scene1"):
    files = list_audio_files(folder_path)
    files.sort()  # Ensure the files are in order
    csv_file_path = os.path.join(folder_path, f"{scene_name}_cue_list.csv")

    with open(csv_file_path, mode='w', newline='') as csv_file:
        fieldnames = ['Cue Number', 'File Name']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for index, file in enumerate(files, start=1):
            writer.writerow({'Cue Number': index, 'File Name': file})

    return csv_file_path


#--------------- GUI Implementation ---------------#

def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_path_var.set(folder_selected)

def process_files():
    folder = folder_path_var.get()
    scene = scene_name_var.get().strip()
    if not folder or not os.path.isdir(folder):
        messagebox.showerror("Error", "Please select a valid folder.")
        return
    if not scene:
        messagebox.showerror("Error", "Please enter a scene name.")
        return

    renamed_count = rename_cues(folder, scene)
    csv_path = export_cue_list_to_csv(folder, scene)

    messagebox.showinfo("Success", f"Renamed {len(renamed_count)} files.\nCSV exported to {csv_path}")


# Folder selection
tk.Label(root, text="Select Folder:").pack(anchor="w", padx=10,pady=5)

frame1 = tk.Frame(root)
frame1.pack(fill="x", padx=10)
tk.Entry(frame1, textvariable=folder_path_var, width=50).pack(side="left", padx=10)
tk.Button(frame1, text="Browse", command=browse_folder).pack(side="left", padx=5)

# Scene name input
frame2 = tk.Frame(root)
frame2.pack(fill="x", padx=10, pady=10)
tk.Label(frame2, text="Scene Name:").pack(side="left")
tk.Entry(frame2, textvariable=scene_name_var, width=20).pack(side="left", padx=5)

# Process button
tk.Button(root, text="Rename and Export Cue List", command=process_files).pack(pady=20)

# Run app
root.mainloop()