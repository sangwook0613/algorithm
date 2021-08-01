// 프로그래머스 폰켓몬
// 배열을 다뤄볼 수 있는 문제
// 문제 풀이는 쉽다!


function solution(nums) {
  var answer = 0;
  nums.sort((a, b) => a-b)
  
  let numberSet = []
  let currentNum = nums[0]
  numberSet.push(nums[0])
  for (let n of nums) {
      if (n !== currentNum) {
          numberSet.push(n)
          currentNum = n
      }
  }
  if (numberSet.length >= nums.length/2) {
      answer = nums.length/2
  } else {
      answer = numberSet.length
  }
  return answer;
}