use std::collections::HashMap;
use std::str::FromStr;

#[derive(Debug, PartialEq, PartialOrd, Hash, Eq, Clone, Copy, Ord)]
// order is important as it defines what cards is greater
enum Card {
    J,  // use for part 2
    TW,
    TH,
    FO,
    FI,
    SI,
    SE,
    E,
    N,
    T,
    // J,  // use for part 1
    Q,
    K,
    A,
}

impl FromStr for Card {
    type Err = String;

    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "2" => Ok(Card::TW),
            "3" => Ok(Card::TH),
            "4" => Ok(Card::FO),
            "5" => Ok(Card::FI),
            "6" => Ok(Card::SI),
            "7" => Ok(Card::SE),
            "8" => Ok(Card::E),
            "9" => Ok(Card::N),
            "T" => Ok(Card::T),
            "J" => Ok(Card::J),
            "Q" => Ok(Card::Q),
            "K" => Ok(Card::K),
            "A" => Ok(Card::A),
            _ => Err(String::from("Unexpected char")),
        }
    }
}

#[derive(Debug, PartialEq, PartialOrd)]
// order is important as it defines which hand is more valuable
enum HandType {
    HighCard,
    OnePair,
    TwoPair,
    Three,
    FullHouse,
    Four,
    Five,
}

#[derive(Debug, PartialEq, Eq, Ord)]
struct Hand {
    cards: [Card; 5],
    is_part_2: bool,
}

impl FromStr for Hand {
    type Err = String;
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        let cards = s
            .chars()
            .map(|c| c.to_string().parse::<Card>().unwrap())
            .collect::<Vec<Card>>()
            .try_into()
            .unwrap();
        return Ok(Hand { cards, is_part_2: false });
    }
}

impl PartialOrd for Hand {
    fn partial_cmp(&self, other: &Self) -> Option<std::cmp::Ordering> {
        let my_type = self.hand_type();
        let other_type = other.hand_type();
        if my_type != other_type {
            return my_type.partial_cmp(&other_type);
        } else {
            for (mc, oc) in self.cards.iter().zip(other.cards.iter()) {
                let card_cmp = mc.partial_cmp(oc);
                match card_cmp {
                    Some(std::cmp::Ordering::Equal) => (),
                    None => (),
                    _ => return card_cmp,
                }
            }
            return None;
        }
    }
}

impl Hand {
    fn hand_type(&self) -> HandType {
        let mut counts: HashMap<Card, u32> = HashMap::new();
        for c in self.cards.iter() {
            let count = counts.entry(c.clone()).or_insert(0);
            *count += 1;
        }
        let mut j_value = 0;
        if self.is_part_2 {
            if let Some(v) = counts.remove(&Card::J) {
                j_value = v;
            }
        }
        let mut seen = 0;
        let mut counts = counts.values().collect::<Vec<_>>();
        counts.sort();

        // part 2 specific but doesn't impact part 1
        let new_max = counts.pop().unwrap_or(&0) + j_value;
        counts.push(&new_max);

        for &v in counts.into_iter().rev() {
            match v {
                5 => return HandType::Five,
                4 => return HandType::Four,
                3 => seen += v,
                2 => {
                    if seen == 3 {
                        return HandType::FullHouse;
                    } else if seen == 2 {
                        return HandType::TwoPair;
                    } else {
                        seen += v;
                    }
                }
                1 => {
                    if seen == 3 {
                        return HandType::Three;
                    } else if seen == 2 {
                        return HandType::OnePair;
                    }
                }
                _ => continue,
            }
        }
        return HandType::HighCard;
    }
}


fn main() {
    let mut hands: Vec<(Hand, u32)> = include_str!("../input.txt")
        .lines()
        .map(|l| {
            let mut split = l.split_whitespace().into_iter();
            let mut hand: Hand = split.next().unwrap().parse().unwrap();
            hand.is_part_2 = true;  // use only for part 2
            (hand, split.next().unwrap().parse::<u32>().unwrap())
        })
        .collect::<>();
    hands.sort_by(|(h1, _), (h2, _)| h1.partial_cmp(h2).unwrap());

    let result: u32 = hands
        .into_iter()
        .enumerate()
        .map(|(idx, (_, bid))| bid * (idx as u32 + 1))
        .sum();
    println!("{:?}", result);
}

