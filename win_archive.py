import os
import zipfile
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox

class WinArchiveApp:
    def __init__(self, root):
        self.root = root
        self.root.title("WinArchive - File Compressor and Decompressor")
        self.root.geometry("400x200")
        
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Select Action:").pack(pady=5)
        
        self.action_var = tk.StringVar()
        self.action_combobox = Combobox(self.root, textvariable=self.action_var)
        self.action_combobox['values'] = ("Compress", "Decompress")
        self.action_combobox.current(0)
        self.action_combobox.pack(pady=5)
        
        tk.Button(self.root, text="Select File", command=self.select_file).pack(pady=5)

        self.file_label = tk.Label(self.root, text="No file selected")
        self.file_label.pack(pady=5)

        tk.Button(self.root, text="Execute", command=self.execute_action).pack(pady=5)

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.file_label.config(text=os.path.basename(self.file_path))

    def execute_action(self):
        action = self.action_var.get()
        if not hasattr(self, 'file_path') or not self.file_path:
            messagebox.showwarning("Warning", "No file selected")
            return

        if action == "Compress":
            self.compress_file(self.file_path)
        elif action == "Decompress":
            self.decompress_file(self.file_path)

    def compress_file(self, file_path):
        try:
            zip_file_path = file_path + ".zip"
            with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                zipf.write(file_path, os.path.basename(file_path))
            messagebox.showinfo("Success", f"File compressed to {zip_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def decompress_file(self, file_path):
        try:
            with zipfile.ZipFile(file_path, 'r') as zipf:
                extract_path = os.path.splitext(file_path)[0]
                zipf.extractall(extract_path)
            messagebox.showinfo("Success", f"File decompressed to {extract_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WinArchiveApp(root)
    root.mainloop()