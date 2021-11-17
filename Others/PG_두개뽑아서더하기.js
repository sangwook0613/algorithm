// 프로그래머스 두 개 뽑아서 더하기
// Object의 특성을 활용했다
function solution(numbers) {
  let count = {}
  for (let a = 0; a < numbers.length; a++) {
      for (let b = a+1; b < numbers.length; b++) {
          count[numbers[a]+numbers[b]] ? count[numbers[a]+numbers[b]]++ : count[numbers[a]+numbers[b]] = 1
      }
  }
  return Object.keys(count).map(Number)
}

// 다른 풀이
// Set을 활용한 풀이
function solution(numbers) {
  const temp = []

  for (let i = 0; i < numbers.length; i++) {
      for (let j = i + 1; j < numbers.length; j++) {
          temp.push(numbers[i] + numbers[j])
      }
  }

  const answer = [...new Set(temp)]

  return answer.sort((a, b) => a - b)
}