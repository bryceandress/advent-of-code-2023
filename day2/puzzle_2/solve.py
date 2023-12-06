# opening the data file
file = open("input.txt")

# reading the file as a list line by line
content = file.readlines()

# closing the file
file.close()
result = 0

game_number = None
for game in content:
    game_data = game.strip()
    chunks = game_data.strip(';').split(';')
    game_possible = True
    max_counts = {'red': 0, 'blue': 0, 'green': 0}
    # Probably a better way to get game number out of this
    for chunk in chunks:
        chunk = chunk.strip(':').split(':')
        data = None
        if len(chunk) > 1:
            game_number = chunk[0]
            data = chunk[1]
        else:
            data = chunk[0]
        game_data = data.strip(',').split(',')
        # Each game in a round
        for round_number in game_data:
            color = round_number.split()[1]
            count = round_number.split()[0]
            if int(count) > max_counts[color]:
                max_counts[color] = int(count)

    # increase result by multiplication of the dict
    result += (max_counts['blue'] * max_counts['red'] * max_counts['green'])
print(result)
