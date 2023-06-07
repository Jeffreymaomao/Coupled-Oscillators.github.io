const amplitude = document.getElementById("amplitude");

amplitude.addEventListener("input", e => {
    balls.amplitude = amplitude.value;
})

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


const tclear = document.getElementById("clear");
tclear.addEventListener("click", e => {
    if (confirm("Are you sure to clean table ?")) {
        tbody.innerHTML = "";
        CSVdata = "";
    }
})