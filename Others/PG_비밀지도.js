// 프로그래머스 비밀지도
// for 문 무한 반복과 toString 활용
function solution(n, arr1, arr2) {
  let answer = [];
  let binArr1 = []
  let binArr2 = []
  for (let i of arr1) {
      let temp = i.toString(2)
      if (temp.length === n) {
          binArr1.push(temp)
      } else {
          let temp2 = ''
          for (let a = 0; a < n-temp.length; a++) {
              temp2 += '0'
          }
          temp2 += temp
          binArr1.push(temp2)
      }
  }
  
  for (let i of arr2) {
      let temp = i.toString(2)
      if (temp.length === n) {
          binArr2.push(temp)
      } else {
          let temp2 = ''
          for (let a = 0; a < n-temp.length; a++) {
              temp2 += '0'
          }
          temp2 += temp
          binArr2.push(temp2)
      }
  }
  
  for (let k = 0; k < n; k++) {
      let string1 = binArr1[k].split('')
      let string2 = binArr2[k].split('')
      let ans = ''
      for (let j = 0; j < n; j++) {
          if (string1[j] === '1' || string2[j] === '1') {
              ans += '#'
          } else {
              ans += ' '
          }
      }
      answer.push(ans)
  }
  return answer;
}

// 다른 풀이
// repeat와 replace를 활용한 풀이
function solution(n, arr1, arr2) {
  return arr1.map((v, i) => addZero(n, (v | arr2[i]).toString(2)).replace(/1|0/g, a => +a ? '#' : ' '));
}

const addZero = (n, s) => {
  return '0'.repeat(n - s.length) + s;
}