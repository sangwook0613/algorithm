// 프로그래머스 큰 수 만들기
// 스택 과 그리디를 활용해야하는 문제!
function solution(number, k) {
  let nums = []
  for (let i = 0; i < number.length; i++) {
      let now = number[i]
      
      while (k > 0 && nums[nums.length - 1] < now) {
          nums.pop()
          k--
      }
      nums.push(now)
  }
  
  nums.splice(nums.length - k, k)
  
  return nums.join('')
}