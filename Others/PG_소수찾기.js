// 순열 알고리즘 연습

function solution(numbers) {
  var answer = 0;
  const num = 1000000
  let chk = new Array(num).fill(1)
  chk[0] = chk[1] = 0
  let idx = 2
  while (idx < num) {
      if (chk[idx] === 1) {
          for (let i = idx*2; i < num; i += idx) {
              chk[i] = 0
          }
      }
      idx++
  }
  let powerSetCheck = new Array(numbers.length).fill(0);
  let powerSetArr = []
  const solve = (depth) => {
      if (depth === powerSetCheck.length) {
          let temp = ''
          for (let i = 0; i < numbers.length; i++) {
              if (powerSetCheck[i] === 1) {
                  temp += numbers[i]
              }
          }
          powerSetArr.push(temp)
      } else {
          //포함되는 경우
          powerSetCheck[depth] = 1
          solve(depth + 1)
          //포함되지 않는 경우
          powerSetCheck[depth] = 0
          solve(depth + 1)
      }
  }
  solve(0)
  console.log(powerSetArr)
  // for (let arr of powerSetArr) {
  //     if (arr.length > 0) {
  //         let prime = parseInt(arr.reduce((a, b) => a+b))
  //         console.log(prime, chk[prime])
  //         if (chk[prime] === 1) {
  //             answer++
  //             chk[prime] = 2
  //             console.log(prime, chk[prime])
  //         }
  //     }        
  // }
  console.log(parseInt("011"))
  console.log(parseInt(numbers[0]))
  
  return answer;
}