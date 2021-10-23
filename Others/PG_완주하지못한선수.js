// PG 완주하지 못한 선수

// 내 풀이
// Object를 활용하여 풀었다
// Object는 for in을 Array는 for of를 사용하는 연습을 하자!
function solution(participant, completion) {
  let chk = {}
  for (let name of participant) {
      if (chk[name]) {
          chk[name]++
      } else {
          chk[name] = 1
      }
  }
  
  for (let name of completion) {
      chk[name]--
  }
  
  for (let a in chk) {
      if (chk[a] === 1) {
          return a
      }
  }
}

// 좋은 풀이
// reduce와 find, 삼항연산자를 이렇게 잘 활용할 수 있구나..
function solution(participant, completion) {
  var dic = completion.reduce((obj, t)=> (obj[t]= obj[t] ? obj[t]+1 : 1 , obj) ,{});
  return participant.find(t=> {
      if(dic[t])
          dic[t] = dic[t]-1;
      else 
          return true;
  });
}