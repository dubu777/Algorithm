function solution(players, callings) {
  const rank_lst = {}
  players.forEach((item, index) => 
  rank_lst[item] = index
  ) 
  for ( let call of callings ) {
    let call_idx = rank_lst[call]
    let front_name = players[call_idx-1]
    rank_lst[call] -= 1
    rank_lst[front_name] += 1
    players[call_idx-1] = players[call_idx]
    players[call_idx] = front_name
  }
  
  return players
}