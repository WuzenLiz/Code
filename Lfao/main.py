"""
implement the UI for game using tkinter
"""
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from core import Chessboard


import sv_ttk

#write setting to registry
import winreg
RESOLUTION_LIST = ["800x600", "1024x768", "1280x720", "1366x768"]

def _write_to_registry(key, value):
    value = str(value)
    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, "Software\\GameOfDots")
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\GameOfDots", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, key, 0, winreg.REG_SZ, value)
        winreg.CloseKey(registry_key)
        return True
    except WindowsError:
        return False

def _read_from_registry(key):
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Software\\GameOfDots", 0, winreg.KEY_READ)
        value, regtype = winreg.QueryValueEx(registry_key, key)
        winreg.CloseKey(registry_key)
        return value
    except WindowsError:
        return None

def _get_or_create_size():
    try:
        size = int(_read_from_registry("size"))
    except:
        size = 12
        _write_to_registry("size", size)
    return size

def _get_or_create_resolution():
    try:
        resolution = _read_from_registry("resolution")
        if resolution not in RESOLUTION_LIST:
            resolution = RESOLUTION_LIST[0]
            _write_to_registry("resolution", resolution)
    except:
        resolution = RESOLUTION_LIST[0]
        _write_to_registry("resolution", resolution)
    return resolution

class GameUI:
    title = "Game of Dots"
    def __init__(self, size, resolution):
        # Broad init
        self.size = size
        self.resolution = resolution
        self.size_of_unit = self._caculate_size_of_unit()
        self.chessboard = Chessboard(size=size)
        # UI init
        self.window = tk.Tk()
        self.window.title(self.title)
        self.window.geometry(self.resolution)
        self.window.resizable(0, 0)
        # menu bar
        self.menu_bar = tk.Menu(self.window)
        self.menu_bar.add_command(label="Reset", command=self.reset)
        self.menu_bar.add_command(label="Settings", command=self.setting)
        self.window.config(menu=self.menu_bar)
        # Canvas
        self.canvas = tk.Canvas(self.window, bg="white", height=self.size_of_unit * self.size, width=self.size_of_unit * self.size)
        self.canvas.pack()
        # Status bar
        self.status_bar = ttk.Frame(self.window, relief=tk.SUNKEN)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        # score of two player in status bar
        self.player1_score_label = ttk.Label(self.status_bar, text=f"Human: 0", relief=tk.SUNKEN)
        self.player1_score_label.pack(side=tk.LEFT, fill=tk.X)
        self.player2_score_label = ttk.Label(self.status_bar, text=f"Com: 0", relief=tk.SUNKEN)
        self.player2_score_label.pack(side=tk.RIGHT, fill=tk.X)
        
        # Bind event
        ## "R" to reset the game
        self.canvas.bind("<Key>", lambda event: self.reset() if event.char == "r" else None)
        
        # allow the canvas to focus on the event
        self.canvas.focus_set()

        # allow console to print the event
        self.canvas.bind("<Button-1>", lambda event: print(f"Clicked at: {event.x}, {event.y}"))

        # print the board
        self.draw_board()

    def draw_board(self):
        for row in range(self.size):
            for col in range(self.size):
                self.canvas.create_rectangle(
                    self.size_of_unit * col,
                    self.size_of_unit * row,
                    self.size_of_unit * (col + 1),
                    self.size_of_unit * (row + 1),
                    fill="white"
                )

    def add_unit(self, event):
        col = event.x // self.size_of_unit
        row = event.y // self.size_of_unit

        if self.chessboard.board[row][col] != 0:
            return
        
        self.chessboard.add_unit(row, col ,player=self.chessboard._PLAYER_1)
        self.chessboard._convert_surrounding_units(row, col, player=self.chessboard._PLAYER_1)
        self.chessboard.make_com_move()
        self.update_score()
        self.draw_units()
    
    def draw_units(self):
        self.canvas.delete("unit")

        for row in range(self.size):
            for col in range(self.size):
                if self.chessboard.board[row][col] == self.chessboard._PLAYER_UNIT:
                    self.canvas.create_oval(
                        self.size_of_unit * col + 10,
                        self.size_of_unit * row + 10,
                        self.size_of_unit * (col + 1) - 10,
                        self.size_of_unit * (row + 1) - 10,
                        fill="red",
                        tags="unit"
                    )
                elif self.chessboard.board[row][col] == self.chessboard._MACHINE_UNIT:
                    self.canvas.create_oval(
                        self.size_of_unit * col + 10,
                        self.size_of_unit * row + 10,
                        self.size_of_unit * (col + 1) - 10,
                        self.size_of_unit * (row + 1) - 10,
                        fill="blue",
                        tags="unit"
                    )

    def reset(self):
        self.canvas.delete("unit")
        self.chessboard = Chessboard(size=self.size)
        self.draw_board()
        self.update_score()
        self.start()
        
    def is_ended(self):
        return self.chessboard._is_ended()
    
    def start(self):
        if not self.is_ended():
            self.canvas.bind("<Button-1>", self.add_unit)
            self.window.after(1000, self.start)
        else:
            print(self.is_ended())
            print(f"Game is ended, no more move! {self.chessboard.player1_score} - {self.chessboard.player2_score}")
            if self.chessboard.player1_score > self.chessboard.player2_score:
                messagebox.showinfo("Game Over", "HUMAN wins! R to reset")
            elif self.chessboard.player1_score < self.chessboard.player2_score:
                messagebox.showinfo("Game Over", "COM wins! R to reset")
            else:
                messagebox.showinfo("Game Over", "Draw! R to reset")
        
    def setting(self):
        # Setting window
        setting_window = tk.Toplevel(self.window)
        setting_window.title("Settings")
        setting_window.geometry("300x200")
        setting_window.resizable(0, 0)
        # Setting window content
        setting_window_label = ttk.Label(setting_window, text="Setting")
        setting_window_label.pack()
        # Setting window protocol
        setting_window.protocol("WM_DELETE_WINDOW", lambda: self._on_setting_window_close(setting_window))

        # Setting for Broard size| user input box
        setting_window_size_label = ttk.Label(setting_window, text="Board size")
        setting_window_size_label.pack()
        setting_window_size_entry = ttk.Entry(setting_window)
        setting_window_size_entry.pack()
        setting_window_size_entry.insert(0, self.size)
        # bind event for user input box
        # bind enter key to the user input box
        setting_window_size_entry.bind("<Return>", lambda event: self._on_size_entry_change(size=setting_window_size_entry.get()))
        # bind focus out to the user input box
        setting_window_size_entry.bind("<FocusOut>", lambda event: self._on_size_entry_change(size=setting_window_size_entry.get()))
        
        # dropdown setting for resolution size (RESOLUTION_LIST) drop down
        setting_window_resolution_label = ttk.Label(setting_window, text="Resolution")
        setting_window_resolution_label.pack()
        resorution_var = tk.StringVar()
        resorution_var.set(self.resolution)
        setting_window_resolution_drop_down = ttk.OptionMenu(
            setting_window, 
            resorution_var, 
            *RESOLUTION_LIST,
            command=lambda _: self._on_resolution_drop_down_click(resorution_var.get()))
        setting_window_resolution_drop_down.pack()
        
    def _on_setting_window_close(self, setting_window):
        resolution = self.resolution
        size = self.size
        _write_to_registry('resolution', resolution)
        _write_to_registry('size', size)
        setting_window.destroy()
    
    def _caculate_size_of_unit(self):
        # current height and width of the window
        resolution = self.resolution
        current_height = int(resolution.split("x")[1])
        current_width = int(resolution.split("x")[0])
        # caculate the size of unit
        size_of_unit = min(current_height, current_width) // self.size - 5
        
        return size_of_unit
    
    def _on_resolution_drop_down_click(self, resolution):
        self.resolution = resolution
        self._update_UX()
    
    def _on_size_entry_change(self, size):
        self.size = int(size)
        self.reset()
        self._update_UX()
    
    def _update_UX(self):
        self.size_of_unit = self._caculate_size_of_unit()
        self.canvas.config(width=self.size_of_unit * self.size, height=self.size_of_unit * self.size)
        self.window.geometry(self.resolution)
        self.canvas.delete('all')
        self.draw_board()
        self.window.update()
    
    def update_score(self):
        self.player1_score_label.config(text=f"Human: {self.chessboard.player1_score}")
        self.player2_score_label.config(text=f"Com: {self.chessboard.player2_score}")
    
if __name__ == "__main__":
    game = GameUI(size=_get_or_create_size(), resolution=_get_or_create_resolution())
    game.window.after(1000, game.start)
    sv_ttk.set_theme("dark")
    game.window.mainloop()