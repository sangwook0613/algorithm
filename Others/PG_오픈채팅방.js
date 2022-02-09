// 프로그래머스 오픈채팅방 - JS 풀이
// Object 를 활용하여 닉네임 변경을 추적하여 풀이
// 깔끔한 풀이
// map 이 아닌 forEach 를 사용해서 풀었다.
// map 은 return 이 존재하고 기존 array 를 변경하는데 비해 
// forEach 는 return 이 존재하지 않으며 기존 array 를 건들지 않는다.
function solution(record) {
  const nickname = {}
  const order = []
  record.forEach((r) => {
    // 구조 분해 할당을 사용
      const [state, id, nick] = r.split(' ')
      
      if (state === 'Enter') {
          nickname[id] = nick
          order.push([state, id])
      } else if (state === 'Change') {
          nickname[id] = nick
      } else {
          order.push([state, id])
      }
  })
  
  return order.map(([state, id]) => {
      return state === 'Enter' ? `${nickname[id]}님이 들어왔습니다.` : `${nickname[id]}님이 나갔습니다.`
  })
}


// 초기 풀이
function solution(record) {
  var answer = [];
  const nickname = {}
  const order = []
  record.map((r) => {
      const words = r.split(' ')
      if (words[0] === 'Enter') {
          nickname[words[1]] = words[2]
          order.push([words[0], words[1]])
      } else if (words[0] === 'Change') {
          nickname[words[1]] = words[2]
      } else {
          order.push([words[0], words[1]])
      }
  })
  
  answer = order.map((a) => {
      return a[0] === 'Enter' ? `${nickname[a[1]]}님이 들어왔습니다.` : `${nickname[a[1]]}님이 나갔습니다.`
  })
  return answer;
}