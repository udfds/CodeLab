var express = require('express');
var router = express.Router();

router.use(function (req, res) {
  console.time('duration');
  next();
})

/* GET users listing. */
router.get('/', function(req, res, next) {
  res.send('respond with a resource');
});

router.get('/time', function (req, res) {
  const duration = console.timeEnd('duration');
  res.send("--" + duration);
});

module.exports = router;
