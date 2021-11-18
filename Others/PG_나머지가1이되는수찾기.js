// 프로그래머스 나머지가 1이 되는 수 찾기
// 간단한 문제
function solution(n) {
  for (let i = 2; i < n; i++) {
      if (n % i === 1) {
          return i
      }
  }
}