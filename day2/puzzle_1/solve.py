# opening the data file
file = open("input.txt")

# reading the file as a list line by line
content = file.readlines()

# closing the file
file.close()

available = {'red': 12, 'green': 13, 'blue': 14}
possible = 0

game_number = None
for game in content:
    game_data = game.strip()
    chunks = game_data.strip(';').split(';')
    game_possible = True
    for chunk in chunks:
        chunk = chunk.strip(':').split(':')
        data = None
        if len(chunk) > 1:
            game_number = chunk[0]
            data = chunk[1]
        else:
            data = chunk[0]
        more_data = data.strip(',').split(',')
        blue = 0
        red = 0
        green = 0
        for each in more_data:
            color = each.split()[1]
            if color == "red":
                red += int(each.split()[0])
            elif color == "blue":
                blue += int(each.split()[0])
            elif color == "green":
                green += int(each.split()[0])
        if blue > available['blue']:
            game_possible = False
        elif green > available['green']:
            game_possible = False
        if red > available['red']:
            game_possible = False

    if game_possible:
        game_number = game_number.split()
        print(game_number[1])
        possible += int(game_number[1])
        game_possible = False

print(possible)
