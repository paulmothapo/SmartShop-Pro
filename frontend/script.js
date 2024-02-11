
const scanBarcode = async (barcode) => {
    try {
      const response = await fetch('/scan', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ barcode })
      });
  
      const data = await response.json();
  
      console.log('Recognized Product:', data.product);
    } catch (error) {
      console.error('Error:', error);
    }
  };
  

  const scannedBarcode = '1234567890'; 
  scanBarcode(scannedBarcode);
  