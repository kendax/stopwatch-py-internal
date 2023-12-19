import tkinter as tk
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")

        self.is_running = False
        self.elapsed_time = 0
        self.start_time = None
        self.heading = tk.Label(root, text="Stopwatch", font=("Arial", 24), foreground="blue")
        self.heading.pack(padx=20, pady=20)
        self.time_display = tk.Label(root, text="00:00.00", font=("Arial", 30))
        self.time_display.pack(padx=20, pady=20, side=tk.TOP, fill="both", expand=True)
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side=tk.BOTTOM, pady=20)

        self.start_button = tk.Button(self.button_frame, image=play_icon, command=self.start_stop)
        self.start_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.reset_button = tk.Button(self.button_frame, image=reset_icon, command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10, pady=5)

        self.update_time()

    def start_stop(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = time.time() - self.elapsed_time
            self.start_button.config(image=pause_icon)
            self.update_time()
        else:
            self.is_running = False
            self.start_button.config(image=play_icon)
            self.elapsed_time = time.time() - self.start_time

    def reset(self):
        self.is_running = False
        self.elapsed_time = 0
        self.start_time = None
        self.start_button.config(image=play_icon)
        self.update_time()

    def update_time(self):
        if self.is_running:
            self.elapsed_time = time.time() - self.start_time

        minutes = int(self.elapsed_time // 60)
        seconds = int(self.elapsed_time % 60)
        centiseconds = int((self.elapsed_time % 1) * 100)

        if minutes >= 60:  # Limit to 60 minutes
            self.is_running = False
            self.start_button.config(image=play_icon)

        time_str = f"{minutes:02d}:{seconds:02d}.{centiseconds:02d}"
        self.time_display.config(text=time_str)
        self.root.after(10, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    play_icon = tk.PhotoImage(file='play-solid.png')
    reset_icon = tk.PhotoImage(file='trash-alt-solid.png')
    pause_icon = tk.PhotoImage(file='pause-solid.png')
    stopwatch = Stopwatch(root)
    root.geometry("700x500+360+175")
    root.mainloop()
