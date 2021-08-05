// 프로그래머스 가장 큰 수
// 문자열 정렬의 특징을 잘 이해하자!
// 문자열로 합해서 비교하는 것이 핵심!!!
// 0 만 있는 예외 케이스도 항상 고려하자!


function solution(numbers) {
    var answer = '';
    let arr = []
    for (let i in numbers) {
        arr.push(String(numbers[i]))
    }
    
    arr.sort(((a, b) => (b+a) - (a+b)))
    
    for (let n of arr) {
        answer += n
    }
    if (parseInt(answer) === 0) {
        return '0'
    }
    return answer;
}