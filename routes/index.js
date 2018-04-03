const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.render('index');
});

router.post('/', (req, res) => {
  const numToConv = req.body.numberToConvert;
  const baseFrom = req.body.baseFrom;
  const baseTo = req.body.baseTo;
  let answerString = "";
  const {spawn} = require('child_process');
  const pyProg = spawn('python', ['./baseConvert.py',
      numToConv,
      baseFrom,
      baseTo
    ]);

  pyProg.stdout.on('data', (data) => {
    answerString += data.toString('utf8');
  });

  pyProg.stderr.on('data', (data) => {
    console.log(data.toString('utf8'));
  });

  pyProg.on('exit', (code) => {
    console.log("Python code stopped with code : " + code);
    res.render('answer', {answerString});
  });


});

module.exports = router;
