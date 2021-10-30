// 구름 소수 판별
// 구름 IDE 의 새로운 입출력에 적응하기 위한 연습
const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

const checkNum = (num) => {
	let result = new Array(num+1).fill(1)
	result[0] = result[1] = 0
	
	for (let i = 2; i <= num; i++) {
		if (result[i]) {
			for (let j = i*2; j < result.length; j += i) {
				result[j] = 0
			}
		}
	}
	return result[num] ? "True" : "False"
}

rl.on("line", function(line) {
	console.log(checkNum(parseInt(line)))
	rl.close();
}).on("close", function() {
	process.exit();
});