// 내 풀이
function solution(lottos, win_nums) {
  let answer = [];
  let cnt = 0
  let match = 0
  for (let n of lottos) {
      if (n === 0) {
          cnt++
      } else {
          for (let num of win_nums) {
              if (n === num) {
                  match++
                  break
              }
          }
      }
  }
  if (cnt + match >= 2) {
      answer.push(7-(match+cnt))
      match >= 2 ? answer.push(7-match) : answer.push(6)
  } else {
      answer = [6, 6]
  }
  return answer;
}


// 좋은 풀이
// array의 find와 map을 적절히 잘 사용했다!!
function solution(lottos, win_nums) {
  const rank = [6, 6, 5, 4, 3, 2, 1];
  let answer = [],
      ans = [],
      ans1 = [];

  lottos.map(x => {
      let val = win_nums.find(y => y == x); // 같은 값이 존재하면 val은 값이 아니면 val은 undefined
      
      if(x == 0) ans1.push(x)
      // undefined는 false이다!
      if(val) {
          ans.push(val)
          ans1.push(val)
      }
  })
  answer.push(rank[ans1.length])
  answer.push(rank[ans.length])

  return answer;
}