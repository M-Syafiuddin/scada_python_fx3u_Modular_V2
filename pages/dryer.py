import tkinter as tk
from ui_components import NavBar, create_manual_lamp, set_background

class Dryer(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        set_background(self, "redray.jpg")
        tk.Label(self, text="DRYER SECTION", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
        self.config = [
            (5, 110, 430, "M1200", "Conveyor Feeder Packing"),
            (6, 190, 490, "M1201", "Conveyor Out Dryer"),
            (7, 900, 540, "M1202", "Fan Zone 1 (Up Draft)"),
            (8, 810, 540, "M1203", "Fan Zone 2 (Up Draft)"),
            (9, 720, 390, "M1204", "Fan Zone 3 (Down Draft)"),
            (10, 850, 260, "M1205", "Exhaust Fan 1"),
            (11, 600, 300, "M1206", "Exhaus Fan 2"),
            (12, 550, 400, "M1207", "Cooler Fan"),
            (13, 450, 400, "M1208", "Ordering Fan 1 (Up Draft)"),
            (14, 400, 400, "M1209", "Ordering Fan 2 (Down Draft)"),
            (15, 315, 400, "M1210", "Ordering Fan 3 (Up Draft)"),
            (16, 270, 400, "M1211", "Ordering Fan 4 (Down Draft)"),
            (17, 270, 490, "M1212", "Apron Conveyor"),
            (18, 950, 380, "M1213", "Conveyor Distributor"),
            (19, 980, 280, "M1214", "Conveyor Feed Dryer"),
        ]
        self.lamps = {bit: create_manual_lamp(self, x, y, lbl, tip) for bit, x, y, lbl, tip in self.config}
        NavBar(self, controller).pack(side="bottom", fill="x")

    def update_ui(self, bits):
        for bit, (cvs, lamp) in self.lamps.items():
            if bit < len(bits):
                cvs.itemconfig(lamp, fill="green" if bits[bit] else "gray")
