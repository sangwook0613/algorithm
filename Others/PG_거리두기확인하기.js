function solution(places) {
  var answer = [];
  let dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]
  
  function bfs(x, y, board) {
      let q = [[x, y, 0]]
      let movingCheck = Array.from(Array(5), () => new Array(5).fill(0))
      movingCheck[x][y] = 1
      console.log(x, y, board)
      while (q.length > 0) {
          let a = q.shift()
          console.log(a)
          for (let d of dir) {
              let dx = a[0] + d[0]
              let dy = a[1] + d[1]
              console.log(dx, dy, board[dx])
              return 1
              if (0 <= dx < 5 && 0 <= dy < 5) {
                  // console.log(board[dx][dy] === 'P', board[dx][dy])
                  // return 1
                  if (board[dx][dy] === 'P') {
                      if (a[2] <= 1) {
                          return 0
                      }
                  } else if (board[dx][dy] === 'X') {
                      continue
                  } else {
                      if (movingCheck[dx][dy] === 0) {
                          movingCheck[dx][dy] = a[2] + 1
                          q.push([dx, dy, a[2]+1])
                      }
                  }
              }
          }
      }
      
      return 1
  }
  
  for (let place of places) {
      let points = []
      for (let i = 0; i < 5; i++) {
          for (let j = 0; j < 5; j++) {
              if (place[i][j] === 'P') {
                  points.push([i, j])
              }
          }
      }
      console.log(points)
      let total = 0
      for (let p of points) {
          total += bfs(p[0], p[1], place)
      }
      answer.push((total === 5) ? 1 : 0)
      console.log(answer)
  }
  
  return answer;
}