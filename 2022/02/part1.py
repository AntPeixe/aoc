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

winning = {('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')}

data = data.split('\n')
score = 0
for game in data:
    if not game: continue
    elf, you = game.split(' ')
    elf, you = plays[elf], plays[you]

    if (you, elf) in winning:
        score += points[you] + 6
    elif (elf, you) in winning:
        score += points[you] + 0
    else:
        score += points[you] + 3

print(score)
