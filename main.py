import tkinter as tk
from config import WINDOW_GEOMETRY, POLLING_RATE
from plc_handler import PLCHandler
from pages import MainMenu, Dryer, Cleaning, ByProduct, Conditioning, Feeding, AlarmLog

class ScadaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SCADA REDRY LINE - FULL SYSTEM CONTROL")
        self.geometry(WINDOW_GEOMETRY)
        
        # Inisialisasi Handler PLC
        self.plc = PLCHandler()
        self.alarm_history = []

        # Container Frame
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        # List halaman
        all_pages = (MainMenu, Dryer, Cleaning, ByProduct, Conditioning, Feeding, AlarmLog)

        for F in all_pages:
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")
        self.update_data_loop()

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
        if page_name == "AlarmLog": 
            frame.refresh_log()

    def pulse_plc(self, address):
        print(f"Sending Pulse to Address: {address}")
        self.plc.write_coil(address, True)
        self.after(300, lambda: self.plc.write_coil(address, False))

    def update_data_loop(self):
        bits = self.plc.read_data()
        if bits:
            for frame in self.frames.values():
                if hasattr(frame, 'update_ui'):
                    frame.update_ui(bits)
        
        self.after(POLLING_RATE, self.update_data_loop)

if __name__ == "__main__":
    app = ScadaApp()
    app.mainloop()
