const express = require('express');
const app = express();
const port = process.env.PORT || 5000;

app.use(express.json());

const indexRoutes = require('./routes/index');
app.use('/', indexRoutes);

app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something went wrong!');
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
