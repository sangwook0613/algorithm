// 프로그래머스 위클리챌린지 1주차 - 부족한 금액 계산하기
// 간단한 수학 문제

function solution(price, money, count) {
  let answer = -1;
  let total = 0;
  for (let i = 1; i <= count; i++) {
      total += i;
  }
  answer = price*total - money;
  if (answer < 0) {
      answer = 0;
  }
  return answer;
}