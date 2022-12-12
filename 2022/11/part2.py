"""
Disclaimer:
    I didn't solve the modulus arithmetic and got it explained.
    I also didn't subtmit the answer to part 2
"""
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

    def investigate(self, all_monkeys_test) -> List[Tuple[int, int]]:
        # old used in eval
        worries = [eval(self.op) for old in self.items]

        rests = [worry % self.test for worry in worries]
        monkey_throw = [self.action_true if rest == 0 else self.action_false for rest in rests]

        # from the wiki 
        # """
        #   k a ≡ k b (mod kn) and k ≠ 0, then a ≡ b (mod n)
        # """
        # 
        # basically if a % b = c then ka % kb = kc
        # so we can take the mod test from all monkeys to be the constant K
        new_worries = [worry % all_monkeys_test for worry in worries]

        self.items = []
        self.inspected_items += len(worries)

        return list(zip(monkey_throw, new_worries))

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

all_monkeys_test = 1
for monkey in monkeys:
    all_monkeys_test *= monkey.test

n_rounds = 10000
for r in range(n_rounds):
    for monkey in monkeys:
        throw_to_and_worry = monkey.investigate(all_monkeys_test)
        for throw_to, worry in throw_to_and_worry:
            monkeys[throw_to].add_item(worry)

a, b = sorted([monkey.inspected_items for monkey in monkeys])[-2:]
print(a*b)
