import tkinter as tk
from ui_components import NavBar, create_manual_lamp, set_background

class Feeding(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        set_background(self, "feeding.jpg")
        tk.Label(self, text="FEEDING SECTION", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
        self.config = [
            (70, 550, 100, "M1280", "Conveyor In Vibratory Conveyor"),
            (71, 750, 120, "M1281", "Vibratory Screen Separator 7"),
            (72, 800, 150, "M1282", "Conveyor In Vibratory Conveyor"),
            (73, 750, 250, "M1283", "Conveyor Pick Up Feeder"),
            (74, 800, 280, "M1284", "Conveyor Feeder A"),
            (75, 800, 460, "M1285", "Conveyor Feeder B"),
            (76, 750, 600, "M1286", "Conveyor Recycle"),
            (77, 330, 600, "M1287", "Thresher"),
            (78, 380, 460, "M1288", "Conveyor in Thresher"),
            (79, 300, 295, "M1289", "Conveyor Wadding"),
        ]
        self.lamps = {bit: create_manual_lamp(self, x, y, lbl, tip) for bit, x, y, lbl, tip in self.config}
        NavBar(self, controller).pack(side="bottom", fill="x")

    def update_ui(self, bits):
        for bit, (cvs, lamp) in self.lamps.items():
            if bit < len(bits):
                cvs.itemconfig(lamp, fill="green" if bits[bit] else "gray")
