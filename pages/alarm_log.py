import tkinter as tk
from tkinter import ttk
from ui_components import NavBar

class AlarmLog(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#f8f9fa")
        self.controller = controller
        tk.Label(self, text="SYSTEM ALARM LOG", font=("Arial", 18, "bold"), bg="#f8f9fa", fg="#dc3545").pack(pady=10)
        
        columns = ("date", "screen", "indicator", "status")
        self.tree = ttk.Treeview(self, columns=columns, show="headings")
        self.tree.heading("date", text="Tanggal & Jam")
        self.tree.heading("screen", text="Screen")
        self.tree.heading("indicator", text="Indikator")
        self.tree.heading("status", text="Status")
        self.tree.pack(fill="both", expand=True, padx=20, pady=10)
        
        tk.Button(self, text="Hapus Semua Log", command=self.clear_logs, bg="#6c757d", fg="white").pack(pady=5)
        NavBar(self, controller).pack(side="bottom", fill="x")

    def refresh_log(self):
        for item in self.tree.get_children(): self.tree.delete(item)
        for entry in self.controller.alarm_history: self.tree.insert("", "end", values=entry)

    def clear_logs(self):
        self.controller.alarm_history = []
        self.refresh_log()
