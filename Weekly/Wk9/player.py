class Player():
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def best_score(players):
        if p2.score > p3.score > p1.score:
            return p2

p1 = Player('Candy', 50)
p2 = Player('Ferb', 250)
p3 = Player('Phineas', 150)

ls = [p1, p2, p3]
best = Player.best_score(ls)
print(best.name)
print(best.score)
msg = '{} has the best score, with {} points!'.format(best.name, best.score)
print(msg)