const express = require('express');
const router = express.Router();


const indexController = require('../controllers/indexController');

router.get('/', indexController.index);

router.post('/scan', async (req, res) => {
   
  });

router.post('/checkout', async (req, res) => {

});

module.exports = router;
