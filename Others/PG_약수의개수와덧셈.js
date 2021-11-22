//프로그래머스 약수의 개수와 덧셈
function solution(left, right) {
    let answer = 0
    function getPrimeNum(n) {
        let result = 2
        for (let i = 2; i < Math.ceil(Math.sqrt(n)); i++) {
            if (n % i === 0) {
                result += 2
            }
        }
        if (Math.ceil(Math.sqrt(n))**2 === n) {
            result++
        }
        return result
    }
    
    for (let a = left; a <= right; a++) {
        let num = getPrimeNum(a)
        answer += (num % 2 ? -a : a)
    }
    return answer
}

// 다른 풀이
// 약수의 특징을 생각하자!
// 제곱근이 정수면 약수의 개수는 홀수다!
function solution(left, right) {
    var answer = 0;
    for (let i = left; i <= right; i++) {
        if (Number.isInteger(Math.sqrt(i))) {
            answer -= i;
        } else {
            answer += i;
        }
    }
    return answer;
}