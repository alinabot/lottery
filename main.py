lottery_numbers = {13, 21, 22, 5, 8}

players = [
    {
        'name': 'Rolf',
        'numbers': {13, 22, 3, 6, 9}
    },
    {
        'name': 'John',
        'numbers': {22, 3, 5, 7, 9}
    }
]

happy_numbers_player_one = lottery_numbers.intersection(players[0]["numbers"])
happy_numbers_player_two = lottery_numbers.intersection(players[1]["numbers"])

right_numbers_one = len(happy_numbers_player_one)
right_numbers_two = len(happy_numbers_player_two)



print("Player", players[0]["name"], "got", right_numbers_one, "numbers right")
print("Player", players[1]["name"], "got", right_numbers_two, "numbers right")
