import random
import tkinter as tk
from tkinter import ttk

# Language strings
TRANSLATIONS = {
    "en": {
        "title": "Rock Paper Scissors",
        "heading": "Choose Rock, Paper, or Scissors",
        "rock": "Rock",
        "paper": "Paper",
        "scissors": "Scissors",
        "tie": "It's a tie!",
        "you_win": "You win!",
        "computer_win": "Computer wins!",
        "make_move": "Make your move!",
        "scoreboard": "Scoreboard",
        "quit": "Quit",
        "reset": "Reset Score",
        "you_chose": "You chose",
        "computer_chose": "Computer chose",
        "player": "Player",
        "computer": "Computer",
        "ties": "Ties",
        "total": "Total Games",
        "score_reset": "Score reset! Make your move!"
    },
    "pt": {
        "title": "Pedra Papel Tesoura",
        "heading": "Escolha Pedra, Papel ou Tesoura",
        "rock": "Pedra",
        "paper": "Papel",
        "scissors": "Tesoura",
        "tie": "Empate!",
        "you_win": "Você venceu!",
        "computer_win": "Computador venceu!",
        "make_move": "Faça seu movimento!",
        "scoreboard": "Placar",
        "quit": "Sair",
        "reset": "Resetar Placar",
        "you_chose": "Você escolheu",
        "computer_chose": "Computador escolheu",
        "player": "Jogador",
        "computer": "Computador",
        "ties": "Empates",
        "total": "Total de Jogos",
        "score_reset": "Placar resetado! Faça seu movimento!"
    }
}

def get_computer_choice() -> str:
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(player_choice: str, computer_choice: str, language: str) -> str:
    if player_choice == computer_choice:
        return TRANSLATIONS[language]["tie"]

    win_conditions = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper",
    }

    if win_conditions[player_choice] == computer_choice:
        return TRANSLATIONS[language]["you_win"]
    return TRANSLATIONS[language]["computer_win"]

class RockPaperScissorsApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.current_language = "en"
        self.title(TRANSLATIONS[self.current_language]["title"])
        self.geometry("450x420")
        self.resizable(False, False)
        
        self.player_wins = 0
        self.computer_wins = 0
        self.ties = 0
        
        self.create_widgets()

    def create_widgets(self):
        # Language selector (SWIFT-style segmented control)
        lang_frame = ttk.Frame(self)
        lang_frame.pack(pady=(8, 8))
        
        lang_label = ttk.Label(lang_frame, text="Language:", font=(None, 9))
        lang_label.pack(side="left", padx=(5, 8))
        
        # Create segmented control using buttons
        lang_buttons_frame = ttk.Frame(lang_frame)
        lang_buttons_frame.pack(side="left")
        
        self.en_button = tk.Button(
            lang_buttons_frame, text="EN", width=4, 
            command=lambda: self.change_language("en"),
            relief="raised", bd=2, bg="#E0E0E0", font=(None, 9, "bold")
        )
        self.en_button.pack(side="left", padx=0)
        
        self.pt_button = tk.Button(
            lang_buttons_frame, text="PT-BR", width=6,
            command=lambda: self.change_language("pt"),
            relief="sunken", bd=1, bg="white", font=(None, 9)
        )
        self.pt_button.pack(side="left", padx=0)
        
        self.update_language_buttons()
        
        heading = ttk.Label(self, text=TRANSLATIONS[self.current_language]["heading"], font=(None, 12, "bold"))
        heading.pack(pady=(8, 8))

        button_frame = ttk.Frame(self)
        button_frame.pack(pady=(0, 16))

        self.rock_button = ttk.Button(button_frame, text=TRANSLATIONS[self.current_language]["rock"], command=lambda: self.play("rock"))
        self.paper_button = ttk.Button(button_frame, text=TRANSLATIONS[self.current_language]["paper"], command=lambda: self.play("paper"))
        self.scissors_button = ttk.Button(button_frame, text=TRANSLATIONS[self.current_language]["scissors"], command=lambda: self.play("scissors"))

        self.rock_button.grid(row=0, column=0, padx=6, ipadx=10)
        self.paper_button.grid(row=0, column=1, padx=6, ipadx=10)
        self.scissors_button.grid(row=0, column=2, padx=6, ipadx=10)

        self.result_label = ttk.Label(self, text=TRANSLATIONS[self.current_language]["make_move"], font=(None, 11))
        self.result_label.pack(pady=(0, 8))

        self.details_label = ttk.Label(self, text="", font=(None, 10))
        self.details_label.pack()

        # Scoreboard section
        self.scoreboard_frame = ttk.LabelFrame(self, text=TRANSLATIONS[self.current_language]["scoreboard"], padding=10)
        self.scoreboard_frame.pack(pady=12, padx=10, fill="both")

        self.score_label = ttk.Label(self.scoreboard_frame, text="", font=(None, 10))
        self.score_label.pack()
        self.update_scoreboard()

        button_frame_bottom = ttk.Frame(self)
        button_frame_bottom.pack(pady=(10, 0))

        self.quit_button = ttk.Button(button_frame_bottom, text=TRANSLATIONS[self.current_language]["quit"], command=self.destroy)
        self.quit_button.pack(side="left", padx=5)

        self.reset_button = ttk.Button(button_frame_bottom, text=TRANSLATIONS[self.current_language]["reset"], command=self.reset_score)
        self.reset_button.pack(side="left", padx=5)

    def play(self, player_choice: str):
        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice, self.current_language)
        
        if result == TRANSLATIONS[self.current_language]["you_win"]:
            self.player_wins += 1
        elif result == TRANSLATIONS[self.current_language]["computer_win"]:
            self.computer_wins += 1
        else:
            self.ties += 1
        
        self.result_label.config(text=result)
        choice_names = {
            "rock": TRANSLATIONS[self.current_language]["rock"],
            "paper": TRANSLATIONS[self.current_language]["paper"],
            "scissors": TRANSLATIONS[self.current_language]["scissors"]
        }
        self.details_label.config(
            text=f"{TRANSLATIONS[self.current_language]['you_chose']} {choice_names[player_choice]}. {TRANSLATIONS[self.current_language]['computer_chose']} {choice_names[computer_choice]}."
        )
        self.update_scoreboard()

    def update_scoreboard(self):
        total_games = self.player_wins + self.computer_wins + self.ties
        lang = TRANSLATIONS[self.current_language]
        scoreboard_text = f"{lang['player']}: {self.player_wins}  |  {lang['computer']}: {self.computer_wins}  |  {lang['ties']}: {self.ties}\n{lang['total']}: {total_games}"
        self.score_label.config(text=scoreboard_text)

    def reset_score(self):
        self.player_wins = 0
        self.computer_wins = 0
        self.ties = 0
        self.result_label.config(text=TRANSLATIONS[self.current_language]["score_reset"])
        self.details_label.config(text="")
        self.update_scoreboard()
    
    def change_language(self, new_language: str):
        self.current_language = new_language
        self.title(TRANSLATIONS[self.current_language]["title"])
        self.update_language_buttons()
        
        # Update all labels
        self.scoreboard_frame.config(text=TRANSLATIONS[self.current_language]["scoreboard"])
        
        # Update heading
        for widget in self.winfo_children():
            if isinstance(widget, ttk.Label) and widget != self.result_label and widget != self.details_label and widget != self.score_label:
                if "Choose" in widget.cget("text") or "Escolha" in widget.cget("text"):
                    widget.config(text=TRANSLATIONS[self.current_language]["heading"])
        
        # Update buttons
        self.rock_button.config(text=TRANSLATIONS[self.current_language]["rock"])
        self.paper_button.config(text=TRANSLATIONS[self.current_language]["paper"])
        self.scissors_button.config(text=TRANSLATIONS[self.current_language]["scissors"])
        self.quit_button.config(text=TRANSLATIONS[self.current_language]["quit"])
        self.reset_button.config(text=TRANSLATIONS[self.current_language]["reset"])
        
        # Reset message
        self.result_label.config(text=TRANSLATIONS[self.current_language]["make_move"])
        self.details_label.config(text="")
        self.update_scoreboard()
    
    def update_language_buttons(self):
        if self.current_language == "en":
            self.en_button.config(relief="raised", bd=2, bg="#E0E0E0", font=(None, 9, "bold"))
            self.pt_button.config(relief="sunken", bd=1, bg="white", font=(None, 9))
        else:
            self.en_button.config(relief="sunken", bd=1, bg="white", font=(None, 9))
            self.pt_button.config(relief="raised", bd=2, bg="#E0E0E0", font=(None, 9, "bold"))

if __name__ == '__main__':
    app = RockPaperScissorsApp()
    app.mainloop()
