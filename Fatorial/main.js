const input = require("fs").readFileSync(0, "utf8");

function fatorial(n){
	if (n == 0){
		return 1;
	}
	return n * fatorial(n-1);
}

let n = parseInt(input);
console.log(fatorial(n));