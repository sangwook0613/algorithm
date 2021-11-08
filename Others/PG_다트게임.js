// 프로그래머스 다트 게임

function solution(dartResult) {
  let result = dartResult.split('')
  let num = [0, 0, 0]
  let prev = 'a'
  let idx = 0
  console.log(result)
  for (let s of result) {
      if (isNaN(parseInt(s))) {
          if (s === 'D') {
              num[idx] = (idx+1)**2
          } else if (s === 'T') {
              num[idx] = (idx+1)**3
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
              if (idx === 0) {
                  num[idx] 
              }
          } else {
              prev += s
          }
          
          idx = parseInt(s) - 1
          
      }
      prev = s
      console.log(s, num)
  }
  return num.reduce((prev, cur) => prev + cur)
}