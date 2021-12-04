// 프로그래머스 피보나치 수
// 간단한 DP 문제
function solution(n) {
  let arr = new Array(n+1).fill(0)
  arr[1] = 1
  for (let i = 2; i <= n; i++) {
      arr[i] = (arr[i-1] + arr[i-2]) % 1234567
  }
  
  return arr[n]
}