from tkinter import *  
from tkinter.scrolledtext import ScrolledText
from tkinter.messagebox import *

import itertools

from team_chooser import *


def parse_players(players_text):
    lines = players_text.splitlines()
    for sep in ["\t", ","]:
        if lines[0].count(sep) > 0:
            break
            
    players = []
    for l in lines:
        name, score = l.split(sep)
        score = int(score)
        players.append((name, score))
    return players


def parse_seperations(seperations_text):
    lines = seperations_text.splitlines()
    groups = []
    g = []
    for l in lines:
        if l:
            g.append(l)
        else:
            groups.append(g)
            g = []
            
    if g:
        groups.append(g)
        
    bad_pairs = []
    for g in groups:
        if len(g) > 3:
            showerror(title="Error", message=f"Seperation group size cant be above 3, {g}")
            raise Exception()
        bad_pairs += list(itertools.combinations(g, 2))
    
    return bad_pairs
        

def calc_teams(players_text, seperations_text, output_widget):
    players = parse_players(players_text)
    bad_pairs = parse_seperations(seperations_text)
    good_teams = good_build_teams(players, bad_pairs)
    output_widget.delete(1.0, "end")
    for i in range(len(good_teams)):
        output_widget.insert("end", f"Team {i+1}: {calc_team_score(good_teams[i])}\n")
        for player in good_teams[i]:
            output_widget.insert("end", f"{player[0]}\n")
        output_widget.insert("end", "\n")


def main():
    window = Tk()

    window.title("TeamChooser")

    window.geometry('600x800')

    lbl = Label(window, text="Players: (name, score)")

    lbl.grid(column=0, row=0)

    
    txt = ScrolledText(window, width=25)
    txt.grid(column=0, row=1, pady=10, padx=10)
    txt.focus()
    
    lbl2 = Label(window, text="Seperations:")

    lbl2.grid(column=0, row=2)

    
    txt2 = ScrolledText(window, width=25, height=10)
    txt2.grid(column=0, row=3, pady=10, padx=10)
    
    
    lbl3 = Label(window, text="Results")
    lbl3.grid(column=1, row=0)
    
    txt3 = ScrolledText(window, width=25)
    txt3.grid(column=1, row=1, pady=10, padx=10)
    
    btn = Button(window, text="Run Algorithm", command=lambda: calc_teams(txt.get(1.0, "end"), txt2.get(1.0, "end"), txt3))
    btn.grid(column=0, row=4)

    window.mainloop()


if __name__ == '__main__':
    main()