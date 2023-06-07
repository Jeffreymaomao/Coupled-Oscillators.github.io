

/** ---------------------------------------------------------------------------- */
// canvas setting
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext("2d");
const scale = 2;
const size = {
	width: window.innerWidth/2,
	height: window.innerHeight,
};
[canvas.style.width, canvas.style.height] = [`${size.width}px`, `${size.height}px`];
[canvas.width, canvas.height] = [parseInt(canvas.style.width) * scale, parseInt(canvas.style.height) * scale];
const center = {
	x: canvas.width/2, 
	y: canvas.height/2,
	max: max(canvas.width/2,canvas.height/2)
};

window.addEventListener("resize",()=>{
	size.width = window.innerWidth/2;
	size.height = window.innerHeight;
	[canvas.style.width, canvas.style.height] = [`${size.width}px`, `${size.height}px`];
	[canvas.width, canvas.height] = [parseInt(canvas.style.width) * scale, parseInt(canvas.style.height) * scale];
	center.x = canvas.width/2;
	center.y_ = canvas.height/2;
	center.max = max(canvas.width/2,canvas.height/2);
})

class Axis{
	constructor(){
		this.color = "#000";
	}
	draw(){
		ctx.strokeStyle = this.color;
		ctx.strokeStyle = this.linewidth;
		ctx.beginPath();
		ctx.moveTo(center.x,0);
		ctx.lineTo(center.x,canvas.height);
		ctx.stroke();
		ctx.closePath();
	}
	update(){

	}
}

class Balls{
	constructor(x=[]){
		this.x = x;
		this.n = x.length;
		this.radius = 20;
		this.amplitude = 20;
		this.colors = ['red','blue'];
		this.strokeStyle = "#000";
		this.linewidth = 1;
		this.duration = 500;
	}
	draw(){
		/* ---- */
		for(var i=0;i<this.n;i++){
			ctx.fillStyle = this.colors[i%this.colors.length];
			ctx.lineWidth = this.linewidth;
			ctx.strokeStyle = this.strokeStyle;
			ctx.beginPath();
			ctx.arc(
				center.x + this.amplitude *this.x[i],
				(1+i)*canvas.height/(this.n+1), 
				this.radius, 0, 2*pi);
			ctx.fill();
			ctx.stroke();
			ctx.closePath();
		}
	}
	update(x){
		this.x = x;
		this.n = x.length;
	}
}
/** ---------------------------------------------------------------------------- */
// main

const balls = new Balls();
const axis = new Axis();

function draw() {
	ctx.fillStyle = '#fff';
    ctx.fillRect(0, 0, canvas.width, canvas.height);
    axis.draw();
    balls.draw();
}

function update() {

}

function loop() {
    draw();
    update();
    requestAnimationFrame(loop);
}

loop();

/** ---------------------------------------------------------------------------- */



