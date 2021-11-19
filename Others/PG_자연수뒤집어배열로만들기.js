// 프로그래머스 자연수 뒤집어 배열로 만들기
// 숫자 - 문자열 - 숫자 변환으로 풀음
function solution(n) {
  let answer = []
  let temp = n.toString().split('')
  for (let i of temp) {
      answer.unshift(parseInt(i))
  }
  return answer;
}