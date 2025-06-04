const XLSX = require('xlsx');

// Load the workbook
const workbook = XLSX.readFile('grdetgl-5450.xls');

// Choose the first sheet (you can change this if needed)
const sheetName = workbook.SheetNames[0];
const worksheet = workbook.Sheets[sheetName];

// Convert to JSON to work with the data
const dataRows = XLSX.utils.sheet_to_json(worksheet, { defval: "" });
const filteredData = []

for (let i = 7; i < dataRows.length; i++) {
  const row = dataRows[i];
  // Check if the row has an invoice number
  if (row['__EMPTY_9'] && row['__EMPTY_12']) {
    filteredData.push({
      'Invoice number': row['__EMPTY_9'],
      'Description': row['__EMPTY_12']
    })
  }
}


// Convert filtered data back to a sheet
const newSheet = XLSX.utils.json_to_sheet(filteredData);

// Create a new workbook and add the new sheet
const newWorkbook = XLSX.utils.book_new();
XLSX.utils.book_append_sheet(newWorkbook, newSheet, 'Invoices');

// Write the new file
XLSX.writeFile(newWorkbook, 'invoices_only.xlsx');
