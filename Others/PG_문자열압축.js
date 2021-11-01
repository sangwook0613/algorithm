// 프로그래머스 문자열 압축
// 문자열 슬라이싱은 slice()
function solution(s) {
  var answer = s.length;
  for (let i = 1; i < s.length; i++) {
      let word = s
      let current = word.slice(0, i)
      let cnt = 1
      let newWord = ''
      for (let j = i; j < s.length; j+=i) {
          let temp = word.slice(j, j+i)
          if (temp === current) {
              cnt++
          } else {
              if (cnt > 1) {
                  newWord += `${cnt}${current}`
              } else {
                  newWord += `${current}`
              }
              cnt = 1
          }
          current = temp
      }
      if (cnt > 1) {
          newWord += `${cnt}${current}`
      } else {
          newWord += `${current}`
      }
      
      if (newWord.length < answer) {
          answer = newWord.length
      }
  }
  return answer;
}