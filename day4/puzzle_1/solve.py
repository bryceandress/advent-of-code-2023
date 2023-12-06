with open("input.txt") as f:
   input = [line.strip() for line in f.readlines()]
card_scores = []
num_cards = [1] * len(input)
for lno, line in enumerate(input):
   _, all_numbers = line.split(": ")
   winners_str, numbers_str = all_numbers.split(" | ")
   winners: set[int] = set(int(number) for number in winners_str.split())
   numbers: set[int] = set(int(number) for number in numbers_str.split())

   num_winners = len(winners & numbers)

   card_scores.append(2 ** (num_winners - 1) if num_winners > 0 else 0)

   #part 2
   for n in range(lno + 1, min(lno + 1 + num_winners, len(num_cards))):
       num_cards[n] += num_cards[lno]

#print(sum(card_scores))
print(sum(card_scores), sum(num_cards))
