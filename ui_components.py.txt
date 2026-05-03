import tkinter as tk
from PIL import Image, ImageTk

class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tip_window = None
        self.widget.bind("<Enter>", self.show_tip)
        self.widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event=None):
        if self.tip_window or not self.text: return
        x = self.widget.winfo_rootx() + 25
        y = self.widget.winfo_rooty() + 25
        self.tip_window = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        tk.Label(tw, text=self.text, justify='left', background="#ffffca", 
                 relief='solid', borderwidth=1, font=("Arial", 9)).pack(ipadx=1)

    def hide_tip(self, event=None):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None

class NavBar(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#d1d1d1", height=80)
        pages = [
            ("Main Menu", "MainMenu"), ("Dryer", "Dryer"), 
            ("Cleaning", "Cleaning"), ("ByProduct", "ByProduct"),
            ("Conditioning", "Conditioning"), ("Feeding", "Feeding"),
            ("ALARM LOG", "AlarmLog")
        ]
        for txt, target in pages:
            color = "#ffc107" if target == "AlarmLog" else "SystemButtonFace"
            tk.Button(self, text=txt, width=12, height=2, font=("Arial", 8, "bold"),
                      bg=color, command=lambda t=target: controller.show_frame(t)).pack(side="left", padx=2, pady=10)

def create_manual_lamp(parent, x, y, label_text, tooltip_text):
    canvas = tk.Canvas(parent, width=15, height=15, bg=parent['bg'], highlightthickness=0)
    lamp = canvas.create_rectangle(0, 0, 15, 15, fill="gray")
    canvas.place(x=x, y=y)
    tk.Label(parent, text=label_text, padx=0, pady=0, bg=parent['bg'], font=("Arial", 8, "bold")).place(x=x, y=y+15)
    Tooltip(canvas, tooltip_text)
    return canvas, lamp

def set_background(parent, image_path):
    from config import BG_SIZE
    try:
        img = Image.open(image_path)
        img = img.resize(BG_SIZE, Image.LANCZOS)
        parent.bg_img = ImageTk.PhotoImage(img)
        bg_label = tk.Label(parent, image=parent.bg_img)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except:
        tk.Label(parent, text=f"Gbr {image_path} tdk ditemukan", bg="gray").place(x=0,y=0)
