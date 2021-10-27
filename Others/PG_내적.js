// 프로그래머스 내적
// 내 풀이
// for을 사용
function solution(a, b) {
  let ans = 0
  for (let i = 0; i < a.length; i++) {
      ans += a[i]*b[i]
  }
  return ans;
}

// 좋은 풀이
// reduce 를 활용하여 간단하게 처리!
function solution(a, b) {
  return a.reduce((acc, _, i) => acc += a[i] * b[i], 0);
}