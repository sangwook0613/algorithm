// 프로그래머스 기능개발
// 큐 / 스택 지식만 있으면 쉽게 푸는 문제
// JS에서 배열을 다루는 push와 pop, shift와 unshift의 차이를 잘 알아두자


function solution(progresses, speeds) {
  var answer = [];
  let cnt = 0
  
  while (progresses.length > 0) {
    if (progresses[0] >= 100) {
      while (progresses[0] >= 100 && progresses.length > 0) {
        cnt++
        progresses.shift()
        speeds.shift()
      }
      answer.push(cnt)
      cnt = 0
    }
    for (let i = 0; i < progresses.length; i++) {
      progresses[i] += speeds[i]
    }
  }
  return answer;
}