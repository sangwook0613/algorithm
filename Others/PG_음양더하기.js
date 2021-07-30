// 프로그래머스 음양더하기
// 간단한 배열문제


function solution(absolutes, signs) {
  var answer = 0;
  for (let i = 0; i < absolutes.length; i++) {
      if (signs[i]) {
          answer += absolutes[i]
      } else {
          answer += absolutes[i]*-1
      }
  }    
  return answer;
}