function solution(numbers) {
  var answer = '';
  
  // 끝에 0이 있는지 없는지 파악해서 정렬
  
  function setOrder(a, b) {
      let len = (a.length > b.length) ? a.length : b.length
      for (let i = 0; i < len; i++) {
          if (a[i] > b[i]) {
              return a
          }
      }
  }
  setOrder('123', '1123')
  
  
//     function setOrder(a, b) {
//         if (a < b) {
//             return 1
//         } else if (a > b) {
//             return -1
//         } else {
//             return 0
//         }
//     }
  
  let arr = []
  let idx = []
  for (let i in numbers) {
      if (numbers[i] % 10 === 0) {
          
      }
      arr.push(String(num))
  }
  arr.sort(setOrder)
  for (let n of arr) {
      answer += n
  }
  return answer;
}