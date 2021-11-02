// 프로그래머스 3진법 뒤집기
// 내 풀이
// reduce를 활용했다.
function solution(n) {
  let answer = 0;
  let threes = 1
  let num = []
  let threeDigit = []
  while (threes <= n) {
      num.unshift(threes)
      threes *= 3
  }
  
  for (let i = 0; i < num.length; i++) {
      let temp = parseInt(n / num[i])
      n -= num[i]*temp
      threeDigit.push(temp)
  }
  
  threes = 1
  answer = threeDigit.reduce((acc, cur) => {
      let result = cur*threes
      threes *= 3
      return acc + result
  }, 0)
  return answer;
}

// 다른 풀이
// toString의 진법 변환을 활용
const solution = (n) => {
    return parseInt([...n.toString(3)].reverse().join(""), 3);
}