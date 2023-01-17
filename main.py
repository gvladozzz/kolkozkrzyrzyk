import tkinter as tk

def startgame():
    global player1_name, player2_name
    player1_name = player1_name_entry.get()
    player2_name = player2_name_entry.get()
    registration_window.destroy()
    game_window.mainloop()

player1_name = None
player2_name = None
player1_name_points = None
player2_name_points = None
"""variable"""
#___REGISTRATION-WINDOW___
#windows
registration_window = tk.Tk()
game_window = tk.Tk()
#frame
reg_frame = tk.Frame(registration_window)
game_player1_info_frame = tk.Frame(game_window)
game_player2_info_frame = tk.Frame(game_window)
game_xo_frame = tk.Frame(game_window)
#label
player1_name_label = tk.Label(reg_frame, text="PLAYER-1 NICKNAME:")
player2_name_label = tk.Label(reg_frame, text="PLAYER-2 NICKNAME:")
#entry
player1_name_entry = tk.Entry(reg_frame)
player2_name_entry = tk.Entry(reg_frame)
#buttons
registration_button = tk.Button(reg_frame, text="START GAME", command=startgame)
#___GAME-WINDOW___
#label
player1_nickname_label = tk.Label(game_player1_info_frame, text = f"Nickname1: {player1_name}")
player2_nickname_label = tk.Label(game_player2_info_frame, text = f"Nickname2: {player2_name}")
player1_points_label = tk.Label(game_player1_info_frame, text = f"Points1: {player1_name_points}")
player2_points_label = tk.Label(game_player2_info_frame, text = f"Points2: {player2_name_points}")
"""placing"""
#___REGISTRATION-WINDOW___
reg_frame.pack(padx=10, pady=50)
player1_name_label.pack()
player1_name_entry.pack(pady=10)
player2_name_label.pack()
player2_name_entry.pack(pady=10)
#buttons
registration_button.pack()
#___GAME-WINDOW___
#frames
game_player1_info_frame.pack(anchor=tk.NW)
game_player2_info_frame.pack(anchor=tk.NE)
game_xo_frame.pack(anchor=tk.CENTER)
#label
player1_nickname_label.pack()
player2_nickname_label.pack()
player1_points_label.pack()
player2_points_label.pack()
#buttons
f=[]
for i in range(3):
    l=[]
    for j in range(3):
        button=tk.Button(game_xo_frame, text="0", width=4, height=2).grid(column=i,row=j)
        button.grid(row=i, column=j)
        list.append(button)
        l.append(button)
    f.append(l)
print(f)

"""config"""
#windows
registration_window.title("REGISTRATION FORM")
game_window.title("GAME")
registration_window.geometry("300x300")
game_window.geometry("500x500")
"""main"""


"""other"""
registration_window.mainloop()
