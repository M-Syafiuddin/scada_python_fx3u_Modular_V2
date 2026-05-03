import tkinter as tk
from ui_components import NavBar, create_manual_lamp, set_background

class Conditioning(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        set_background(self, "conditioning.jpg")
        tk.Label(self, text="CONDITIONING SECTION", font=("Arial", 16, "bold"), bg="white").pack(pady=10)
        self.config = [
            (61, 900, 100, "M1270", "Exhaust Fan"),
            (62, 600, 350, "M1271", "Separator Screen Drum Conditioning"),
            (63, 550, 300, "M1272", "Fan Circulator"),
            (64, 690, 400, "M1273", "Main Drive"),
            (65, 450, 450, "M1274", "Vibratory screen separator 6"),
        ]
        self.lamps = {bit: create_manual_lamp(self, x, y, lbl, tip) for bit, x, y, lbl, tip in self.config}
        NavBar(self, controller).pack(side="bottom", fill="x")

    def update_ui(self, bits):
        for bit, (cvs, lamp) in self.lamps.items():
            if bit < len(bits):
                cvs.itemconfig(lamp, fill="green" if bits[bit] else "gray")
