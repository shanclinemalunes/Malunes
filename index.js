const express = require('express');

const app = express()

app.get('/', (req, res) => {
    res.send(`WASSUP MANANAP`)
})

app.listen(1228, () => {
    console.log('Server is running on http://localhost:1228')
})

