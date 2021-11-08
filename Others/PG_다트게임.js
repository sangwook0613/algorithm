// 프로그래머스 다트 게임
// 하나하나 if문으로 처리
function solution(dartResult) {
  let result = dartResult.split('')
  let num = [0, 0, 0]
  let prev = 'a'
  let idx = -1
  
  for (let s of result) {
      if (isNaN(parseInt(s))) {
          if (s === 'D') {
              num[idx] = num[idx]**2
          } else if (s === 'T') {
              num[idx] = num[idx]**3
          } else if (s === '#') {
              num[idx] *= -1
          } else if (s === '*') {
              for (let i = idx -1; i <= idx; i++) {
                  if (i >= 0){
                      num[i]*=2
                  }
              }
          } 
      } else {
          if (isNaN(parseInt(prev))) {
              idx++
              num[idx] = parseInt(s)
          } else {
              prev += s
              num[idx] = parseInt(prev)
          }            
      }
      prev = s
  }
  return num.reduce((prev, cur) => prev + cur)
}

// 다른 풀이
// 정규표현식을 활용
function solution(dartResult) {
  const bonus = { 'S': 1, 'D': 2, 'T': 3 },
        options = { '*': 2, '#': -1, undefined: 1 };

  let darts = dartResult.match(/\d.?\D/g);

  for (let i = 0; i < darts.length; i++) {
      let split = darts[i].match(/(^\d{1,})(S|D|T)(\*|#)?/),
          score = Math.pow(split[1], bonus[split[2]]) * options[split[3]];

      if (split[3] === '*' && darts[i - 1]) darts[i - 1] *= options['*'];

      darts[i] = score;
  }

  return darts.reduce((a, b) => a + b);
}
