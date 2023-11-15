import tkinter as tk

class PlatformerGame:
    def __init__(self, master):
        self.master = master
        self.master.title("2D Platformer Game")
        self.master.geometry("400x300")
        
        # Create player character
        self.player = tk.Canvas(self.master, width=50, height=50, bg="blue")
        self.player_position = {"x": 50, "y": 250}
        self.player_id = self.player.create_rectangle(0, 0, 50, 50, fill="blue")
        self.player.place(x=self.player_position["x"], y=self.player_position["y"])

        # Bind arrow keys to player movement
        self.master.bind("<Left>", self.move_left)
        self.master.bind("<Right>", self.move_right)

    def move_left(self, event):
        self.player_position["x"] -= 10
        self.update_player_position()

    def move_right(self, event):
        self.player_position["x"] += 10
        self.update_player_position()

    def update_player_position(self):
        self.player.place(x=self.player_position["x"], y=self.player_position["y"])

if __name__ == "__main__":
    root = tk.Tk()
    game = PlatformerGame(root)
    root.mainloop()
