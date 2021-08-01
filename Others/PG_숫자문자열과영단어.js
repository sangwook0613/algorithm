// 프로그래머스 숫자 문자열과 영단어
// 오브젝트를 다루는 문제
// 문자열과 숫자를 구분하여 판단하는 스킬만 있으면 충분


function solution(s) {
  var answer = '';
  let dict = {
      'zero':0, 'one':1, 'two':2, 'three':3, 'four':4,
      'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9
  }
  let word = ''
  
  for (let i of s) {
      if(isNaN(i)) {
          word+= i
          if (dict[word] !== undefined) {
              answer += dict[word]
              word = ''
          }
      } else {
          answer += i
      }
  }
  let ans = parseInt(answer)
  
  return ans;
}