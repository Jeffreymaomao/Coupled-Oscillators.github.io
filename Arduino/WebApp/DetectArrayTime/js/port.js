function Utf8ArrayToStr(array) {
	// http://www.onicos.com/staff/iz/amuse/javascript/expert/utf.txt

	/* utf.js - UTF-8 <=> UTF-16 convertion
	 *
	 * Copyright (C) 1999 Masanao Izumo <iz@onicos.co.jp>
	 * Version: 1.0
	 * LastModified: Dec 25 1999
	 * This library is free.  You can redistribute it and/or modify it.
	 */
    var out, i, len, c;
    var char2, char3;

    out = "";
    len = array.length;
    var i = 0;
    while (i < len) {
        c = array[i++];
        switch (c >> 4) {
            case 0:case 1:case 2:case 3:case 4:case 5:case 6:case 7:
                // 0xxxxxxx
                out += String.fromCharCode(c);
                break;
            case 12:
            case 13:
                // 110x xxxx   10xx xxxx
                char2 = array[i++];
                out += String.fromCharCode(((c & 0x1F) << 6) | (char2 & 0x3F));
                break;
            case 14:
                // 1110 xxxx  10xx xxxx  10xx xxxx
                char2 = array[i++];
                char3 = array[i++];
                out += String.fromCharCode(((c & 0x0F) << 12) |
                    ((char2 & 0x3F) << 6) |
                    ((char3 & 0x3F) << 0));
                break;
        }
    }

    return out;
}

var record = false;
var CSVdata = '';
var time = 0.0;

if('serial' in navigator){
	const selectPort = document.getElementById('selectPort');
	if(selectPort){
		// when click, call a async function
		selectPort.addEventListener('click', async () => {
		    // select Port 
		    const port = await navigator.serial.requestPort();
		    // setting baudRate
		    await port.open({
		    	baudRate: 9600,
		    	dataBits: 8,
		    	flowControl: "none",
		    	parity: "none",
		    	stopBits: 2,
		    });


		    while (port.readable) {
		    	console.log("The port is connected.");
		    	// selectPort.remove();
		        const reader = port.readable.getReader();
		        try {
		        	var dataBuffer = '';
		            while (true) {
		                const { value, done } = await reader.read();
		                if (done) {
		                    reader.releaseLock();
		                    break;
		                }
		                if (value) {
		                	var data = Utf8ArrayToStr(value);
		                	data = data.replace(/\s\n/g, '');
		                	if(typeof(data)==='string'){
		                		dataBuffer += data;
							}
							const index = dataBuffer.indexOf("#");
							if(index!=-1){
								let arr = dataBuffer.substring(0,index).split(",");
								arr = arr.map(str => {return Number(str);});
								// console.log(arr)
								time = arr[0]
								arr.shift();
								/* update animation */
								balls.update(arr);
								/* update data */
								if(record){
									CSVdata += time+",";
									CSVdata += arr+"\n";
									arr.unshift(time);
									addDataToExcel(arr);
								}
								/* clear buffer */
								dataBuffer = dataBuffer.substring(index+1);
							}
		                }
		            }
		        } catch (err) {
		            console.log(err);
		        }

		    }

		});
	}
}else{
	alert("The Serial API is NOT supported.\nYour browser can not use Serial Port.");
}




