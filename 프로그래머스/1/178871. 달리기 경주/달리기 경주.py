def solution(players, callings):
    # 각 player의 인덱스를 저장할 dictionary
    player_index = {player: idx for idx, player in enumerate(players)}
    
    for call in callings:
        idx = player_index[call]
        if idx > 0:
            # Swap players
            players[idx], players[idx-1] = players[idx-1], players[idx]
            # Update indices in the dictionary
            player_index[players[idx]] = idx
            player_index[players[idx-1]] = idx - 1
    
    return players