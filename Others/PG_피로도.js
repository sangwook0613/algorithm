// 프로그래머스 피로도
// 재귀를 통해 조합을 구하는 것이 핵심인 풀이
// 아래 조합을 귀하는 재귀함수는 꼭 알아두자!!
function solution(k, dungeons) {
    var answer = -1;
    let order = []
    for (let i = 0; i < dungeons.length; i++) {
        order.push(i)
    }
    
    // 재귀를 통해 조합 구하기
    function combination(arr, num) {
      let result = [];
      if(num == 1) return arr.map(e => [e]);

      arr.forEach((e,i,array) => {
        let rest = [...array.slice(0,i), ...array.slice(i+1)];
        let combinations = combination(rest,num-1);
        let combiArr = combinations.map(x => [e, ...x])
        result.push(...combiArr);
      }) 
      return result;
    }
    
    let orders = combination(order, order.length)
    
    for (let order of orders) {
        let temp = k
        let cnt = 0
        for (let n of order) {
            if (temp >= dungeons[n][0]) {
                temp -= dungeons[n][1]
                cnt++
            } else {
                break
            }
        }
        if (cnt > answer) {
            answer = cnt
        }
    }
    
    return answer;
}