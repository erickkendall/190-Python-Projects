deck={}
for key in ['clubs','diamonds','hearts','spades']:
    for value in ['1','2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']:
        deck[key] = value

print(str(deck))
