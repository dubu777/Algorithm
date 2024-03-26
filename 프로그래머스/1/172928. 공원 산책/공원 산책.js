function solution(park, routes) {
  const dirs = {'E': [0, 1], 'W': [0, -1], 'S': [1, 0], 'N': [-1, 0]}
  let [x, y] = [0, 0]
  for ( let i = 0; i < park.length; i++) {
    if ( park[i].includes('S') ) {
      [x, y] = [i, park[i].indexOf('S')]
      break
    }
  }

  routes.forEach((route) => {
    let [nx, ny] = [x, y]
    let [dir, len] = route.split(' ')
    for ( let i = 0; i < Number(len); i++) {
      [nx, ny] = [nx + dirs[dir][0], ny + dirs[dir][1]]
      if (!park[nx] || !park[nx][ny] || park[nx][ny] == 'X') break
      if (i == len-1) [x, y] = [nx, ny]
    }
  })
  return [x, y]
}