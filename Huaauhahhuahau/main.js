const laughter = require("fs").readFileSync(0, "utf8");

function reverseString(str){
	return str.split("").reverse().join("");
}

let vowels = "";
for(let i = 0; i < laughter.length; i++){
  let c = laughter[i];
  if(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'){
    vowels += c;
  }
}

let str = reverseString(vowels);
for(let i = 0; i < str.length; i++){
	if(str[i] != vowels[i]){
    console.log('N');
    return
	}
}
console.log('S');