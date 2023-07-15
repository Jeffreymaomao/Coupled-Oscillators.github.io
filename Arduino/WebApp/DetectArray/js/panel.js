/* ----------------------------------------------
-------------   Amplitude button ----------------
------------------------------------------------- */
const amplitude = document.getElementById("amplitude");
amplitude.addEventListener("input", e => {
    balls.amplitude = amplitude.value;
})

/* ----------------------------------------------
-------------   Table Updator -------------------
------------------------------------------------- */
const table = document.getElementById('excel');
const tbody = table.querySelector('tbody');
const theadtr = table.querySelector("thead tr");

var rowCount = 1;
var colCount = 0;

function addDataToExcel(data) {
    /* -------------------- thead -------------------- */
	if(data.length!=colCount){
    	colCount = data.length;
		theadtr.innerHTML = '';
		const indexCell = document.createElement("td");
		indexCell.textContent = "#";
		theadtr.appendChild(indexCell);
    	for(var i=0;i<colCount;i++){
    		const cell = document.createElement("th");
    		cell.textContent = "x"+(i+1);
    		theadtr.appendChild(cell);
    	}
    }

    /* -------------------- tbody -------------------- */
    const row = document.createElement('tr');

    // 新增行數列
    const indexCell = document.createElement('td');
    indexCell.textContent = rowCount;
    row.appendChild(indexCell);

    // 新增資料列
    data.forEach(cellData => {
        const cell = document.createElement('td');
        cell.textContent = cellData;
        row.appendChild(cell);
    });

    tbody.appendChild(row);
    rowCount++;
}

/* ----------------------------------------------
-------------   Table Cleaner -------------------
------------------------------------------------- */
const tclear = document.getElementById("clear");
tclear.addEventListener("click", e => {
    if (confirm("Are you sure to clean table and data?")) {
        tbody.innerHTML = "";
        CSVdata = "";
    }
})
/* ----------------------------------------------
-------------   Download to CSV -------------------
------------------------------------------------- */
const csvDownload = document.getElementById("download");
csvDownload.addEventListener("click",e =>{

	const fileName = prompt("Download file name :");
	if(fileName!=null){
		const link = document.createElement('a');
	    const blob = new Blob([CSVdata], { type: 'text/csv;charset=utf-8;' });
	    const url = URL.createObjectURL(blob);
	    document.body.appendChild(link);

	    link.href = url;
	    link.style.display = 'none';
	    link.download = fileName;
	    if(link.download==''){
	    	let date = new Date(Date.now());
	        dataValues = date.getFullYear()+"-"+String(date.getMonth() + 1)+"-"+date.getDate()+"-"+date.getHours()+"-"+date.getMinutes();
	        link.download = dataValues;
	    }
	    link.click();
	    document.body.removeChild(link);
	    URL.revokeObjectURL(url);
	}
})
/* ----------------------------------------------
-------------   Record button -------------------
------------------------------------------------- */
const recordBTN = document.getElementById("record");
recordBTN.addEventListener("click",e =>{
	record = !record;
	if(record){
		recordBTN.innerHTML = "Recording...";
	}else{
		recordBTN.innerHTML = "Record";
	}
	
	recordBTN.classList.toggle("recording");
})






