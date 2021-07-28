// 프로그래머스 모의고사
// 첫 JS로 풀어본 알고리즘 문제
// 쉬운 문제들을 풀어보면서 JS 문법에 대해 조금씩 익숙해지자!

function solution(answers) {
    var answer = [];
    let p1 = 1;
    let p2 = 1;
    let p3 = 1;
    let count = [0, 0, 0];
    const p2Order = [1, 3, 4, 5];
    const p3Order = [3, 1, 2, 4, 5];
    for(let i = 0; i < answers.length; i++) {
        if (p1 % 6 === 0) {
            p1 = 1
        }
        if (p1 === answers[i]) {
            count[0]++
        }
        p1++
        if ( i % 2 !== 0) {
            if (p2Order[p2-1] === answers[i]) {
                count[1]++
            }
            if (p3Order[p3-1] === answers[i]) {
                count[2]++
            }
            
            if ( p2 % 4 === 0) {
                p2 = 1
            } else {
                p2++
            }
            if ( p3 % 5 === 0) {
                p3 = 1
            } else {
                p3++
            }
        } else {
            if (answers[i] === 2) {
                count[1]++
            }
            if (p3Order[p3-1] === answers[i]) {
                count[2]++
            }
        }
    }
    
    let maxNum = count[0]
    for (let k = 1; k < 3; k++) {
        if (count[k] > maxNum) {
            maxNum = count[k]
        }
    }
    
    for (let k = 0; k < 3; k++) {
        if (count[k] === maxNum) {
            answer.push(k+1)
        }
    }
    
    return answer;
}