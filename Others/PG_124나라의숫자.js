// 프로그래머스 124 나라의 숫자
// 3진법 문제
// 간단한 규칙성을 파악하지 못해서 시간을 많이 날렸다..


function solution(n) {
  var answer = '';
  let order = ['4', '1', '2']
  let num = n
  
  while (num > 0) {
      if (num % 3 === 0) {
          answer = order[0] + answer
          num = num/3 - 1
      } else if (num % 3 === 1) {
          answer = order[1] + answer
          num = parseInt(num/3)
      } else {
          answer = order[2] + answer
          num = parseInt(num/3)
      }
  }
  
  return answer;
}