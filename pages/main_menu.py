import tkinter as tk
from ui_components import NavBar, create_manual_lamp

class MainMenu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#80cbc4")
        tk.Label(self, text=" JOB CONTROL ", font=("Arial", 18, "bold"), bg="#80cbc4").pack(pady=10)
        
        tk.Button(self, text="START SYSTEM", bg="green", fg="white", font=("Arial", 10, "bold"),
                  command=lambda: controller.pulse_plc(0)).place(x=50, y=80)
        tk.Button(self, text="STOP SYSTEM", bg="red", fg="white", font=("Arial", 10, "bold"),
                  command=lambda: controller.pulse_plc(1)).place(x=180, y=80)

        self.config = [
            (2, 100, 200, "RUN", "Sistem Sedang Running"),
            (3, 200, 200, "READY", "Sistem Siap Operasi"),
            (4, 300, 200, "FAULT", "Sistem Error/Alarm!")
        ]
        self.lamps = {bit: create_manual_lamp(self, x, y, lbl, tip) for bit, x, y, lbl, tip in self.config}
        NavBar(self, controller).pack(side="bottom", fill="x")

    def update_ui(self, bits):
        colors = {2: "green", 3: "yellow", 4: "red"}
        for bit, (cvs, lamp) in self.lamps.items():
            if bit < len(bits):
                cvs.itemconfig(lamp, fill=colors[bit] if bits[bit] else "gray")
