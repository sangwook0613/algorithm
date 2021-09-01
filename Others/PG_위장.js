// 프로그래머스 위장
// 좀 더 간단하게 풀어보자!!

function solution(clothes) {
  let clothType = []
  for (let cloth of clothes) {
    if (!clothType.includes(cloth[1])) {
      clothType.push(cloth[1])
    }
  }
  
  let cnt = new Array(clothType.length).fill(1)
  for (let cloth of clothes) {
    for (let t in clothType) {
      if (cloth[1] === clothType[t]) {
        cnt[t]++
        break
      }
    }
  }
  
  let answer = 1
  for (let num of cnt) {
    answer *= num
  }
  return answer -1;
}