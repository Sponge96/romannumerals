const romanNumerals = {
  M: 1000,
  CM: 900,
  D: 500,
  CD: 400,
  C: 100,
  XC: 90,
  L: 50,
  XL: 40,
  X: 10,
  IX: 9,
  V: 5,
  IV: 4,
  I: 1
};

function run(n) {
	let converted = "";
	for(let i of Object.keys(romanNumerals)) {
		let x = Math.floor(n / romanNumerals[i]);
		n -= x * romanNumerals[i];
		converted += i.repeat(x);
		
	}
  return converted;
}

