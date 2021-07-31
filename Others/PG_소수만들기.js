// 프로그래머스 소수 만들기
// 에라토스테네스의 체를 기반으로 소수 리스트를 만들어 풀었다.
// for문을 중첩하는 것이 아닌 재귀를 통해 푸는 연습도 해야겠다.

function getPrimeNum(num) {
  let prime = Array.from({length:num}, () => 1)
  prime[0] = 0
  prime[1] = 0
  for (let i = 2; i < num; i++) {
      if (prime[i] === 1) {
          for (let j = i*2; j < num; j += i) {
              prime[j] = 0
          }
      }
  }
  return prime
}


function solution(nums) {
  var answer = 0;
  
  let primeNums = getPrimeNum(50000)
  for (let a = 0; a < nums.length-2; a++) {
      for (let b = a+1; b < nums.length-1; b++) {
          for (let c=b+1; c < nums.length; c++) {
              if (primeNums[nums[a]+nums[b]+nums[c]] === 1) {
                  answer += 1
              }
          }
      }
  }
  
  return answer;
}