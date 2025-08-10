import json
import os

def init_highscores_file():
    filename = "highscores.json"
    
    if not os.path.exists(filename):
        initial_scores = [
            {"name": "", "score": 0} for _ in range(5)
        ]
        
        with open(filename, 'w') as f:
            json.dump(initial_scores, f, indent=2)

def load_highscores():
    try:
        with open("highscores.json", 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        init_highscores_file()
        return load_highscores()

def save_highscores(scores):
    with open("highscores.json", 'w') as f:
        json.dump(scores, f, indent=2)

def add_score(name, score):
    scores = load_highscores()
    scores.append({"name": name, "score": score})
    
    scores.sort(key=lambda x: x["score"], reverse=True)
    scores = scores[:5]
    
    save_highscores(scores)
    return scores

def get_highscores():
    rows = load_highscores()
    return [el for el in rows if el['score']>0]

def get_min_score():
    names_and_scores = load_highscores()
    names_and_scores.sort(key=lambda x: x["score"])
    max_score = names_and_scores[0]['score']
    return max_score
