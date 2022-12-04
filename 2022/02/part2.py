with open("input.txt") as f:
    data = f.read()

plays = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}

points = {'rock': 1, 'paper': 2, 'scissors': 3}

winning = dict([('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')])
lossing = dict(zip(winning.values(), winning.keys()))

data = data.split('\n')
score = 0
for game in data:
    if not game: continue
    elf, you = game.split(' ')
    elf = plays[elf]

    if you == 'X':  # should loose
        score += points[winning[elf]]
    elif you == 'Z':  #should win
        score += points[lossing[elf]] + 6
    else:  # should draw
        score += points[elf] + 3

print(score)

