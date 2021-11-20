// 프로그래머스 영어 끝말잇기
// 계속 트래킹만 하면 되는 문제
function solution(n, words) {
  let check = {}
  let curr = words[0]
  check[curr] = 1
  let x = 1
  let y = 1
  
  for (let w = 1; w < words.length; w++) {
      x++        
      if (x > n) {
          x = 1
          y++
      }
      check[words[w]] ? check[words[w]]++ : check[words[w]] = 1
      if (check[words[w]] !== 1) {
          return [x, y]
      }
      if (curr[curr.length-1] !== words[w][0]) {
          return [x, y]
      }
      curr = words[w]
  }
  
  return [0, 0]
}