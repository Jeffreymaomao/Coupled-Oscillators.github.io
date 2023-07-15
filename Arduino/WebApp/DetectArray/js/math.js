/*----------------------------------------------------------------------------
https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects/Math

print all properties: 

Object.getOwnPropertyNames(Math).forEach((eq)=>{
	console.log(eq)
})
  ----------------------------------------------------------------------------*/
const abs = Math.abs
const acos = Math.acos
const acosh = Math.acosh
const asin = Math.asin
const asinh = Math.asinh
const atan = Math.atan
const atanh = Math.atanh
const atan2 = Math.atan2
const ceil = Math.ceil
const cbrt = Math.cbrt
const expm1 = Math.expm1
const clz32 = Math.clz32
const cos = Math.cos
const cosh = Math.cosh
const exp = Math.exp
const floor = Math.floor
const fround = Math.fround
const hypot = Math.hypot
const imul = Math.imul
const log = Math.log
const log1p = Math.log1p
const log2 = Math.log2
const log10 = Math.log10
const max = Math.max
const min = Math.min
const pow = Math.pow
const random = Math.random
const round = Math.round
const sign = Math.sign
const sin = Math.sin
const sinh = Math.sinh
const sqrt = Math.sqrt
const tan = Math.tan
const tanh = Math.tanh
const trunc = Math.trunc
const E = Math.E
const LN10 = Math.LN10
const LN2 = Math.LN2
const LOG10E = Math.LOG10E
const LOG2E = Math.LOG2E
const pi = Math.PI
const PI = Math.PI
const SQRT1_2 = Math.SQRT1_2
const SQRT2 = Math.SQRT2
/* ============================================ */
function around(x,n){
	if(n==undefined){n=0;}
	return Math.round(x * 10**n)/10**n
}