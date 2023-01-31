const input = require("fs").readFileSync(0, "utf8");

function fib(n){
	if (n == 1 || n == 0 ){
		return 1;
	}
	return fib(n-1) + fib(n-2);
}
result = fib(parseInt(input));
console.log(result);