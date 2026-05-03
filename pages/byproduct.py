import tkinter as tk
from ui_components import NavBar, create_manual_lamp, set_background

class ByProduct(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        set_background(self, "by poduct.jpg")
        tk.Label(self, text="BY-PRODUCT SECTION", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
        self.config = [
            (45, 520, 375, "M1250", "Vibratory Screen Separator 1"),
            (46, 590, 375, "M1251", "Vibratory Screen Separator 2"),
            (47, 650, 375, "M1252", "Screw Scrap Dryer 1"),
            (48, 670, 410, "M1253", "Rotary Drum Screen Separator"),
            (49, 670, 300, "M1254", "Fan Cyclone Separator"),
            (50, 721, 370, "M1255", "Airlock Cyclone Separator"),
            (51, 950, 540, "M1256", "Screw Scrap Dryer 3"),
            (52, 950, 570, "M1257", "Screw Scrap Dryer 2"),
            (53, 700, 200, "M1258", "Mini Dust Colector"),
            (54, 340, 250, "M1259", "Fan Dust Colector"),
            (55, 200, 200, "M1260", "Airlock Dust Colector 1"),
            (56, 270, 200, "M1261", "Airlock Dust Colector 2"),
            (57, 200, 130, "M1262", "Z Brush"),
        ]
        self.lamps = {bit: create_manual_lamp(self, x, y, lbl, tip) for bit, x, y, lbl, tip in self.config}
        NavBar(self, controller).pack(side="bottom", fill="x")

    def update_ui(self, bits):
        for bit, (cvs, lamp) in self.lamps.items():
            if bit < len(bits):
                cvs.itemconfig(lamp, fill="green" if bits[bit] else "gray")
