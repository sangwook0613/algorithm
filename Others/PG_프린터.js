// 프로그래머스 프린터
// 큐를 응용한 문제, js에서 인덱스와 값을 접근하는 방식을 잘 익히자!

function solution(priorities, location) {
    let paper = []
    for (let i in priorities) {
        paper.push([parseInt(i), priorities[i]])
    }
    let answer = []
    
    while (paper.length > 0) {
        let temp = []
        for (let p of paper) {
            temp.push(p[1])
        }
        let current = paper.shift()
        
        if (current[1] >= Math.max(...temp)) {
            answer.push(current[0])
        } else {
            paper.push(current)
        }
    }
    
    let ans = 1
    for (let a of answer) {
        if (a == location) {
            return ans
        }
        ans++
    }
}