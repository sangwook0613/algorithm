// 프로그래머스 예산
// 문제를 우습게 보지말고 항상 꼼꼼하게 생각해보자...


function solution(d, budget) {
  var answer = 0
  let sum = 0
  d.sort((a, b) => a-b)
  for (let i = 0; i < d.length; i++) {
      answer++
      sum += d[i]
      
      if (sum > budget) {
          answer--
          break
      }
  }

  return answer
}