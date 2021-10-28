// 프로그래머스 크레인 인형뽑기
function solution(board, moves) {
  let answer = 0;
  let boardRow = []
  let basket = []
  for (let a = 0; a < board[0].length; a++) {
      let temp = []
      for (let b = 0; b < board.length; b++) {
          board[b][a] ? temp.push(board[b][a]) : true
      }
      boardRow.push(temp)
  }
  
  for (let i of moves) {
      if (boardRow[i-1].length) {
          let num = boardRow[i-1].shift()
      
          if (basket.length) {
              if (num === basket[basket.length - 1]) {
                  basket.pop()
                  answer+=2
              } else {
                  basket.push(num)
              }
          } else {
              basket.push(num)
          }
      }
  }
  return answer;
}