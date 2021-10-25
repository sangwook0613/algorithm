// 프로그래머스 체육복
// for문을 사용하여 이해한 그대로 풀었다.
function solution(n, lost, reserve) {
    let ans = 0
    let count = []
    for (let i = 0; i < n; i++){
        count.push(1)
        lost.includes(i+1) ? count[i]-- : true
        reserve.includes(i+1) ? count[i]++ : true
    }

    for (let i = 0; i < n; i++) {
        ans++
        if (!count[i]) {
            if (count[i-1] === 2) {
                count[i-1]--
                count[i]++
            } else if (count[i+1] === 2) {
                count[i+1]--
                count[i]++
            } else {
                ans--
            }
        }
    }

    return ans;
}

// 참고할 풀이
// lost와 reserve가 겹치는 로직만 고려하지 못한 풀이
function solution(n, lost, reserve) {      
    return n - lost.filter(a => {
        const b = reserve.find(r => Math.abs(r-a) <= 1)
        if(!b) return true
        reserve = reserve.filter(r => r !== b)
    }).length
}