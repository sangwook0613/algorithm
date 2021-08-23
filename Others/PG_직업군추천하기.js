// 프로그래머스 직업군 추천하기
// 좀더 JS스럽게 다시 한번 풀어보자!


function solution(table, languages, preference) {
  var answer = '';
  const jobs = ["SI", "CONTENTS", "HARDWARE", "PORTAL", "GAME"]
  let points = [0, 0, 0, 0, 0]
  for (let t of table) {
      let temp = t.split(' ')
      for (let j in jobs) {
          if (temp[0] === jobs[j]) {
              for (let l in languages) {
                  for (let i = 1; i <= 5; i++) {
                      if (languages[l] == temp[i]) {
                          points[j] += (6-i)*preference[l]
                          break
                      }
                  }
              }
              break
          }
      }
  }
  
  let ans = 0
  for (let p in points) {
      if (points[p] > ans) {
          answer = jobs[p]
          ans = points[p]
      } else if (points[p] === ans) {
          answer = jobs[p] < answer ? jobs[p] : answer
      }
  }
  
  return answer;
}