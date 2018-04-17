var x = 9;
var d = 0,001;

var a = x;
var boki = [0]
boki[0] = a;
boki[1] = x / a;
var i = 2;
while (a - x / a > d) {
	a = (a + x / a) / 2
	console.log(a);
	boki[i] = a;
	boki[i+1] = x / a;
	i++;
}

console.log(boki)

function setup() {
	// put setup code here
	createCanvas(600, 600);
}

function draw() {
	background(200);
	for (j=0; j < i; j++)
		rect(10 + 10 * j, 10 + 10 * j, boki[j] * 20, boki[j+1] * 20)
}