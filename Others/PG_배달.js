// 프로그래머스 배달
// 최소비용 문제 - 다익스트라
// 파이썬으로 푼 문제를 JS로 풀어보았다.

function solution(N, road, K) {
  var answer = 0;
  let nodes = Array.from(Array(N+1), () => new Array())
  
  // nodes 정리
  for (let i in road) {
    nodes[road[i][0]].push([road[i][1], road[i][2]])
    nodes[road[i][1]].push([road[i][0], road[i][2]])
  }
  
  // 다익스트라
  let time = new Array(N+1).fill(Infinity) // 각 마을까지 도달하는 최소 시간 정리
  time[1] = 0
  let q = [[1, 0]]
  
  while (q.length > 0) {
    let info = q.shift()
    if (time[info[0]] < info[1]) {
      continue
    }
    for (let node of nodes[info[0]]) {
      if (time[node[0]] > info[1] + node[1]) {
        time[node[0]] = info[1] + node[1]
        q.push([node[0], time[node[0]]])
      }
    }
  }
  
  for (let t in time) {
    if (time[t] <= K) {
      answer++
    }
  }
  
  return answer;
}