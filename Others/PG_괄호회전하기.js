// 프로그래머스 괄호 회전하기
// string을 array로 풀어서 해결
function solution(s) {
  var answer = 0;
  let brackets = {
      '[': 1, ']': 2, '{': 3, '}': 4, '(': 5, ')': 6
  }
  let inputs = s.split('')
  for (let i = 0; i < s.length; i++) {
      let chk = []
      let idx = 0
      while (idx < inputs.length) {
          if (brackets[inputs[idx]] % 2) {
              chk.push(brackets[inputs[idx]])
          } else {
              if (chk[chk.length-1] % 2 === 0) {
                  chk.push(brackets[inputs[idx]])
              } else {
                  if (chk[chk.length-1]+1 === brackets[inputs[idx]]) {
                      chk.pop()
                  } else {
                      chk.push(7)
                      break
                  }
              }
          }
          idx++
      }
      
      if (chk.length === 0) {
          answer++
      }
      let temp = inputs.shift()
      inputs.push(temp)
  }
  
  return answer;
}