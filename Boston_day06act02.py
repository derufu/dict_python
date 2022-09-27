winning = {10,11,8,1,5,20}

players = {
    "Jo":{1,8,10,27,12,15},
    "JoJo":{1,8,27,3,4,9},
    "Joe":{9,4,3,12,15,21},
}
# No Cheating
# for players in players.items():
#     if players[0] == "Jo":
#         result = winning.intersection(players[1])
#         if len(result) :
#             print(players[0], "Won", len(result) * 100, "Pesos!")
#         else: print(players[0], "Won Nothing!")
#     if players[0] == "JoJo":
#         result = winning.intersection(players[1])
#         if len(result):
#             print(players[0], "Won", len(result) * 100, "Pesos!")
#         else:
#             print(players[0], "Won Nothing!")
#     if players[0] == "Joe":
#         result = winning.intersection(players[1])
#         if len(result):
#             print(players[0], "Won", len(result) * 100, "Pesos!")
#         else:
#             print(players[0], "Won Nothing!")

# Cheating
# AMBOT NGANO MO LOOP UG KADUHA MAO AKONG GI BREAK PARA MAG BULAG NA SILA
for players in players.items():
    for each in players:
        result = winning.intersection(players[1])
        if len(result):
            print(players[0], "Won", len(result) * 100, "Pesos!")
        else:
            print(players[0], "Won Nothing!")
        break

