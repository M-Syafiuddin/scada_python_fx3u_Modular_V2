import tkinter as tk
from ui_components import NavBar, create_manual_lamp, set_background

class Cleaning(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        set_background(self, "cleaning.jpg")
        tk.Label(self, text="CLEANING SECTION", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
        self.config = [
            (19, 160, 530, "M1214", "Conveyor Feed Dryer"),
            (25, 300, 500, "M1221", "Conveyor Pick NRTM 1"),
            (26, 350, 320, "M1222", "Conveyor Pick NRTM 2"),
            (27, 420, 500, "M1223", "Conveyor Out Vibratory Screen Separator"),
            (28, 480, 500, "M1224", "Coveyor In Scrap Dryer"),
            (29, 550, 350, "M1225", "Vibratory Screen Separator 3"),
            (30, 600, 300, "M1226", "Rotary Drum Screen Separator 2"),
            (31, 600, 400, "M1227", "Fan Separator"),
            (32, 484, 200, "M1228", "Vibratory Screen Separator 4"),
            (33, 600, 158, "M1229", "Vibratory Screen Separator 5"),
            (34, 640, 130, "M1230", "Conveyor In Vibratory Screen Separator 3"),
            (35, 830, 190, "M1231", "Conveyor Brocken Back"),
            (36, 950, 130, "M1232", "Conveyor Velcro"),
            (37, 950, 190, "M1233", "Conveyor in velcro"),
            (38, 930, 300, "M1234", "Conveyor Out Conveyor Pick NRTM"),
            (39, 705, 590, "M1235", "Conveyor Pick NRTM 1"),
            (40, 765, 590, "M1236", "Conveyor Pick NRTM 2"),
            (41, 825, 590, "M1237", "Conveyor Pick NRTM 3"),
            (42, 885, 590, "M1238", "Conveyor Pick NRTM 4"),
            (43, 890, 550, "M1239", "Conveyor Out Conditioning"),
        ]
        self.lamps = {bit: create_manual_lamp(self, x, y, lbl, tip) for bit, x, y, lbl, tip in self.config}
        NavBar(self, controller).pack(side="bottom", fill="x")

    def update_ui(self, bits):
        for bit, (cvs, lamp) in self.lamps.items():
            if bit < len(bits):
                cvs.itemconfig(lamp, fill="green" if bits[bit] else "gray")
