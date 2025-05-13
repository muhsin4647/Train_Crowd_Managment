import tkinter as tk
from tkinter import messagebox, ttk
from collections import defaultdict

class CrowdFinderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Train Crowd Finder System")
        self.root.geometry("400x300")
        
        # Store crowd data as numerical values (1=Low, 2=Medium, 3=High)
        self.data = defaultdict(list)
        
        self.create_main_menu()

    def create_main_menu(self):
        self.clear_window()
        lbl = ttk.Label(self.root, text="Select Train", font=('Helvetica', 14))
        lbl.pack(pady=20)
        
        trains = [
            ("AKS Train", "aks"),
            ("BKS Train", "bks"),
            ("CAS Train", "cas")
        ]
        
        for train_name, train_code in trains:
            btn = ttk.Button(self.root, text=train_name,
                            command=lambda tc=train_code: self.train_selected(tc))
            btn.pack(pady=5)

    def train_selected(self, train_code):
        self.clear_window()
        lbl = ttk.Label(self.root, text=f"{train_code.upper()} Train Options", font=('Helvetica', 12))
        lbl.pack(pady=15)
        
        btn1 = ttk.Button(self.root, text="Check Crowd Level",
                         command=lambda: self.check_crowd(train_code))
        btn1.pack(pady=5)
        
        btn2 = ttk.Button(self.root, text="Add Crowd Data",
                         command=lambda: self.add_crowd_data(train_code))
        btn2.pack(pady=5)
        
        back_btn = ttk.Button(self.root, text="Back to Main Menu",
                             command=self.create_main_menu)
        back_btn.pack(pady=10)

    def add_crowd_data(self, train_code):
        popup = tk.Toplevel()
        popup.title("Add Crowd Level")
        popup.geometry("300x200")
        
        lbl = ttk.Label(popup, text="Select Crowd Level:", font=('Helvetica', 12))
        lbl.pack(pady=15)
        
        levels = [("Low", 1), ("Medium", 2), ("High", 3)]
        
        for level_name, value in levels:
            btn = ttk.Button(popup, text=level_name,
                            command=lambda v=value: self.save_crowd_data(train_code, v, popup))
            btn.pack(pady=5)

    def save_crowd_data(self, train_code, value, window):
        self.data[train_code].append(value)
        messagebox.showinfo("Success", "Crowd data added successfully!")
        window.destroy()

    def check_crowd(self, train_code):
        if not self.data[train_code]:
            messagebox.showwarning("No Data", "No crowd data available for this train")
            return
        
        data = self.data[train_code]
        average = sum(data) / len(data)
        
        if average < 1.5:
            level = "Low"
        elif 1.5 <= average < 2.5:
            level = "Medium"
        else:
            level = "High"
        
        report = (
            f"Crowd Analysis Report\n\n"
            f"Train: {train_code.upper()}\n"
            f"Total Entries: {len(data)}\n"
            f"Average Score: {average:.2f}\n"
            f"Crowd Level: {level}"
        )
        
        popup = tk.Toplevel()
        popup.title("Crowd Level Report")
        
        lbl = ttk.Label(popup, text=report, font=('Helvetica', 12), justify=tk.LEFT)
        lbl.pack(padx=20, pady=20)
        
        close_btn = ttk.Button(popup, text="Close", command=popup.destroy)
        close_btn.pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = CrowdFinderApp(root)
    root.mainloop()