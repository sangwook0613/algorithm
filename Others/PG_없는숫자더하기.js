// 내 풀이
function solution(numbers) {
  let answer = 45
  for (let n of numbers) {
      answer -= n
  }
  
  return answer;
}


// 좋은 풀이
// array의 reduce를 활용하여 간단하게 처리
function solution(numbers) {
  return 45 - numbers.reduce((acc, curr) => acc + curr)
}