
function downloadCSV(csvContent, fileName) {
    const link = document.createElement('a');
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);

    link.href = url;
    link.download = fileName;
    link.style.display = 'none';
    document.body.appendChild(link);

    link.click();

    document.body.removeChild(link);
    URL.revokeObjectURL(url);
}

// 假設你有一個按鈕元素
const downloadButton = document.getElementById('download');

// 當按鈕被點擊時，執行下載 CSV 的動作
downloadButton.addEventListener('click', () => {
    // 將資料轉換成 CSV 格式
    const csvContent = convertToCSV(data);

    // 下載 CSV 檔案
    downloadCSV(csvContent, 'data.csv');
});