from typing import List, Tuple

with open("input.txt") as f:
    data = f.read().strip()

PIECES: List[List[Tuple[int, int]]] = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 2), (0, 1), (1, 1), (2, 1), (1, 0)],
    [(2, 2), (2, 1), (0, 0), (1, 0), (2, 0)],
    [(0, 3), (0, 2), (0, 1), (0, 0)],
    [(0, 1), (1, 1), (0, 0), (1, 0)],
]

class Tetris:
    def __init__(self, points: List[Tuple[int, int]], start_x, start_y) -> None:
        self.points = list(map(lambda p: (p[0] + start_x, p[1] + start_y), points))

    @property
    def bottom(self):
        return min(p[1] for p in self.points)

    @property
    def top(self):
        return max(p[1] for p in self.points)

    @property
    def left(self):
        return min(p[0] for p in self.points)

    @property
    def right(self):
        return max(p[0] for p in self.points)
    
    def move_right(self, cave: set):
        if self.right < 6:
            new_points = [(p[0] + 1, p[1]) for p in self.points]
            if not cave.intersection(set(new_points)): self.points = new_points

    def move_left(self, cave: set):
        if self.left > 0:
            new_points = [(p[0] - 1, p[1]) for p in self.points]
            if not cave.intersection(set(new_points)): self.points = new_points

    def move_down(self, cave: set):
        new_points = [(p[0], p[1] - 1) for p in self.points]
        if cave.intersection(set(new_points)): return False
        else:
            self.points = new_points
            return True


if __name__ == "__main__":
    cave = set([(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)])
    cave_top = max(p[1] for p in cave)
    fallen = 0
    move = 0
    while fallen < 2022:
        piece = Tetris(PIECES[fallen % 5], 2, cave_top + 4)
        moved = True
        while moved:
            mov = data[move]
            move = (move + 1) % len(data)
            if mov == ">": piece.move_right(cave)
            else: piece.move_left(cave)
            moved = piece.move_down(cave)
        cave = cave.union(set(piece.points))
        cave_top = max(cave_top, piece.top)
        fallen += 1

    print(cave_top)
