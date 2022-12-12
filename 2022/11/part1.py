from typing import List, Tuple


class Monkey:
    def __init__(
        self,
        items: List[int],
        op: str,
        test: int,
        action_true: int,
        action_false: int,
    ) -> None:
        self.items = items
        self.op = op
        self.test = test
        self.action_true = action_true
        self.action_false = action_false

        self.inspected_items = 0

    def investigate(self) -> List[Tuple[int, int]]:
        # old used in eval
        worries = [eval(self.op) // 3 for old in self.items]

        rests = [worry % self.test for worry in worries]
        monkey_throw = [self.action_true if rest == 0 else self.action_false for rest in rests]
        self.inspected_items += 1
        return list(zip(monkey_throw, worries))

    def add_item(self, item) -> None:
        self.items.append(item)


with open("input.txt") as f:
    data = f.readlines()

monkeys = []
while data:
    monkey = data.pop(0).split()[1].split(":")[0]
    items = list(map(int, data.pop(0).split(":")[1].strip().split(",")))
    operation = data.pop(0).split("=")[-1].strip()
    test = int(data.pop(0).split()[-1])
    action_true = int(data.pop(0).split()[-1])
    action_false = int(data.pop(0).split()[-1])
    monkeys.append(Monkey(items, operation, test, action_true, action_false))

    try: data.pop(0)
    except: pass

for _ in range(20):
    for idx, monkey in enumerate(monkeys):
        throw_to_and_worry = monkey.investigate()
        for throw_to, worry in throw_to_and_worry:
            monkeys[throw_to].add_item(worry)

a, b = sorted([monkey.inspected_items for monkey in monkeys])[-2:]
print(a*b)

