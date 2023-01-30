const input = require("fs").readFileSync(0, "utf8");
const lines = input.split("\n");

let size = lines[0];
let numbers = lines[1].split(' ');
let count = 0;

for(let i = 0; i < size-2; i++){
	if(numbers[i] == 1 && numbers[i+1] == 0 && numbers[i+2] == 0){
		count++;
		i += 2;
	}
}
console.log(count);