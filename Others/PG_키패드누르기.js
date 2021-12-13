// 프로그래머스 키패드 누르기
// 문제 그대로 풀어나가면 되는 문제
// if문과 for문 만 사용
// map도 써먹어보자...
function solution(numbers, hand) {
  let answer = ''
  let left_num = [1, 4, 7]
  let right_num = [3, 6, 9]
  let left_curr = [3, 0]
  let right_curr = [3, 2]
  for (let num of numbers) {
      if (left_num.includes(num)) {
          answer += 'L'
          left_curr = [parseInt((num-1) / 3), (num-1) % 3]
      } else if (right_num.includes(num)) {
          answer += 'R'
          right_curr =[parseInt((num-1) / 3), (num-1) % 3]
      } else {
          if (num === 0) {
              let left_dist = Math.abs(3 - left_curr[0]) + Math.abs(1 - left_curr[1])
              let right_dist = Math.abs(3 - right_curr[0]) + Math.abs(1 - right_curr[1])
              if (left_dist < right_dist) {
                  answer += 'L'
                  left_curr =[3, 1]
              } else if (left_dist > right_dist) {
                  answer += 'R'
                  right_curr =[3, 1]
              } else {
                  if (hand === "right") {
                      answer += 'R'
                      right_curr =[3, 1]
                  } else {
                      answer += 'L'
                      left_curr =[3, 1]
                  }
              }
              continue
          }
          let left_dist = Math.abs(parseInt((num-1) / 3) - left_curr[0]) + Math.abs((num-1) % 3 - left_curr[1])
          let right_dist = Math.abs(parseInt((num-1) / 3) - right_curr[0]) + Math.abs((num-1) % 3 - right_curr[1])
          if (left_dist < right_dist) {
              answer += 'L'
              left_curr =[parseInt((num-1) / 3), (num-1) % 3]
          } else if (left_dist > right_dist) {
              answer += 'R'
              right_curr =[parseInt((num-1) / 3), (num-1) % 3]                
          } else {
              if (hand === "right") {
                  answer += 'R'
                  right_curr =[parseInt((num-1) / 3), (num-1) % 3]     
              } else {
                  answer += 'L'
                  left_curr =[parseInt((num-1) / 3), (num-1) % 3]
              }
          }
      }
  }
  
  return answer
}