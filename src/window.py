from tkinter import Tk, BOTH, Canvas

class Window:
  def __init__(self, width, height):
    self.root_widget = Tk()
    self.root_widget.title("Maze Solver")
    self.root_widget.protocol("WM_DELETE_WINDOW", self.close)
    self.canvas_widget = Canvas(self.root_widget, bg="white", width=width)
    self.canvas_widget.pack(fill=BOTH, expand=1)
    self.is_windows_running = False

  def redraw(self):
    self.root_widget.update_idletasks()
    self.root_widget.update()
  
  def wait_for_close(self):
    self.is_windows_running = True
    while self.is_windows_running == True:
      self.redraw()

  def close(self):
    self.is_windows_running = False   

  def draw_line(self, line, filler_color="black"):
    line.draw(self.canvas_widget, filler_color)  
