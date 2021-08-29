function solution(priorities, location) {
  var answer = 0;
  let order = []
  let deleteNums = []
  let sorted = Array.from(priorities)
  sorted.sort((a, b) => b-a)
  let idx = 0
  let p = 0
  let total = sorted.reduce((a, b) => a+b)
  console.log('total', total)
  while (total > 0) {
      if (p === priorities.length) {
          console.log(p)
          for (let d of deleteNums) {
              total -= priorities[d]
              priorities.splice(d, 1, 0)
          }
          console.log(total, deleteNums)
          deleteNums = []
          break
          p = 0
      }
      if (priorities[p] === sorted[idx]) {
          order.push(p)
          sorted.shift()
          deleteNums.push(p)
          idx++
          console.log(order, sorted, priorities, idx)
      }
      p++
  }
  return answer;
}