def best_set(votes):
    dictionry_votes = {}
    for v in votes.values():
        if v not in dictionry_votes:
            dictionry_votes[v] = 1
        else:
            dictionry_votes[v] += 1
    winner = "boo"
    max_votes = 0
    for k, v in dictionry_votes.items():
        if v > max_votes:
            winner = k
            max_votes = v
    return winner

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))