// 프로그래머스 가운데 글자 가져오기
// 간단한 문제
function solution(s) {
  let num = Math.floor(s.length / 2)
  return (s.length % 2) ? s[num] : s[num-1] + s[num]
}