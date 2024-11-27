import tkinter as tk

class Application:
  def __init__(self, master):
    self.window = master
    self.update_time = ''
    self.running = False
    self.hours = 0
    self.minutes = 0
    self.seconds = 0
    self.create_widgets()
    self.start()
    self.window.mainloop()

  def start(self):
      if not self.running:
          self.stopwatch_label.after(1000)
          self.update()
          self.running = True

  def create_widgets(self):
        self.stopwatch_label = tk.Label(self.window, text='00:00:00')
        self.stopwatch_label.pack()
        self.window.title('Stopwatch (Class)')

  def update(self):
        self.seconds += 1
        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0
        if self.minutes == 60:
            self.hours += 1
            self.minutes = 0
        hours_string = f'{self.hours}' if self.hours > 9 else f'0{self.hours}'
        minutes_string = f'{self.minutes}' if self.minutes > 9 else f'0{self.minutes}'
        seconds_string = f'{self.seconds}' if self.seconds > 9 else f'0{self.seconds}'
        self.stopwatch_label.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
        self.update_time = self.stopwatch_label.after(1000, self.update)



