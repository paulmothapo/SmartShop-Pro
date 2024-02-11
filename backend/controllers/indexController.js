
const { spawn } = require('child_process');

exports.scanBarcode = async (req, res) => {
    try {

      const { barcode } = req.body;
  
      const product = await recognizeProduct(barcode);

      const pythonProcess = spawn('python', ['deep_learning/scan_product.py', barcode]);
      
      pythonProcess.stdout.on('data', (data) => {
        const product = data.toString().trim(); 
        res.json({ product });
      });
  
      pythonProcess.stderr.on('data', (data) => {
        console.error('Error:', data.toString());
        res.status(500).json({ message: 'Internal server error' });
      });

      res.json({ product });
    } catch (error) {
      console.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  };
  
  exports.processCheckout = async (req, res) => {
    try {
      res.json({ message: 'Checkout successful' });
    } 
    
    catch (error) {
      console.error(error);
      res.status(500).json({ message: 'Internal server error' });
    }
  };
  