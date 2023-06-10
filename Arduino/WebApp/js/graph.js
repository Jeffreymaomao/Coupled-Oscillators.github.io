

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
		this.x_ = new Array(this.n);
		this.n_ = 10;
		this.radius = 15;
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
			ctx.strokeStyle = this.strokeStyle;
			ctx.lineWidth = this.linewidth;
			/* --- path line ---*/
			ctx.beginPath();
			for(var j=0; j<this.n_;j++){
				ctx.globalAlpha = 0.1*pow(j/this.n_,0.5);
				ctx.arc(
					center.x + this.amplitude * this.x_[i][j],
					(1+i)*canvas.height/(this.n+1),
					this.radius, 0, 2*pi);
				ctx.fill();
			}
			ctx.stroke();
			ctx.closePath();

			/* --- Circle ---*/
			ctx.globalAlpha = 1;
			ctx.beginPath();
			ctx.arc(
				center.x + this.amplitude * this.x[i],
				(1+i)*canvas.height/(this.n+1), 
				this.radius, 0, 2*pi);
			ctx.fill();
			ctx.stroke();
			ctx.closePath();
		}
	}
	update(x){
		this.x = x;
		if(this.n!=x.length){
			this.n = x.length;
			this.x_ = new Array(this.n);
			for(var i=0;i < this.n;i++){
				this.x_[i] = new Array(this.n_)
			}
		}
		for(var i=0;i<this.n;i++){
			this.x_[i].pop();
			this.x_[i].unshift(x[i]);
		}
	}
}

class PseudoPort{
	constructor(Balls){
		this.t = 0.0;
		this.dt = 0.005;
		this.format = 100;
		setInterval(() => {
			this.t = this.t + this.dt;
			const arr = [this.x1(this.t),this.x2(this.t),this.x3(this.t),this.x4(this.t)]
			/* update animation */
			Balls.update(arr);
			/* update data */
			if(record){
				CSVdata += arr+"\n";
				addDataToExcel(arr);
			}

		}, 10);
	}
	x1(t){
		return floor(20*sin(5*t)*cos(3.2*t)*this.format)/this.format
	}
	x2(t){
		return floor(20*cos(6*t)*cos(4*t)*this.format)/this.format
	}
	x3(t){
		return floor(20*sin(7*t)*cos(3.2*t)*this.format)/this.format
	}
	x4(t){
		return floor(20*cos(3*t)*cos(4*t)*this.format)/this.format
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

new PseudoPort(balls)