// 프로그래머스 짝지어 제거하기
// 스택을 활용해야하는 문제
function solution(s) {
  // 만약 홀수면 어차피 모두 제거할 수 없기에 0을 return
  if (s.length % 2 !== 0) {
      return 0
  }

  let stack = [] // 앞에서 뽑은 문자를 담을 stack 배열
  // for문을 돌면서 차례대로 앞의 문자를 하나씩 뽑아낸다.
  for (let n of s) {
      // stack 에서도 가장 최근에 들어온 문자(word)를 뽑아낸다.
      let word = stack.pop()
      // 만약 같다면 이후 진행 - 둘 다 같은 문자기에 제거된 것
      if (word !== n) {
          // 만약 word 가 undefined 가 아니면(즉, 빈 stack에서 pop 을 진행한게 아니면) 다시 stack에 넣어준다
          word && stack.push(word)
          // n 도 stack에 push
          stack.push(n)
      }
  }
  
  return stack.length ? 0 : 1
}