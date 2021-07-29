// 프로그래머스 K번째수
// 배열을 다룰 때 사용하는 다양한 for문과 sort()의 원리를 이해할 수 있는 문제
// sort()는 배열의 인자를 string으로 처리한다!
// 그렇기에 수로 받아들여 정렬하기 위해서는 안에 compare 함수가 필요하며
// 화살표 함수를 통해 간단하게 작성할 수 있다.


function solution(array, commands) {
  var answer = [];
  for (let command of commands) {
      let temp = []
      for (let i = command[0]-1; i < command[1]; i++) {
          temp.push(array[i])
      }
      temp.sort((a, b) => a-b)
      answer.push(temp[command[2]-1])
  }
  return answer;
}