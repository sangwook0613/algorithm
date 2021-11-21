//프로그래머스 약수의 개수와 덧셈

function solution(left, right) {
  let answer = 0
  function getPrimeNum(n) {
      let result = [2]
      let chk = new Array(n+1).fill(0)
      let i = 2
      while (i <= n) {
          if (chk[i] === 0) {
              chk[i] = 1
              result.push(i)
              for (let a = i*2; a <= n; a += i) {
                  chk[a] = 1
              }
          }
          i++
      }
      return result
  }
  console.log(getPrimeNum(right))
  return answer
}