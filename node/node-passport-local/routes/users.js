var express = require('express');
var router = express.Router();
var mysql = require('../sql/index')
var passport = require('passport')
const jwt = require('jsonwebtoken');

/* GET users listing. */
// 批量化删除
router.get('/del', function (req, res, next) {
  let id = [994, 995]
  let sql = `DELETE FROM main WHERE id in (?);`
  mysql.query(sql, [id], (err, result1) => {
    if (err) {
      console.log(err)
      return
    }
    res.json({
      code: 200,
      message: '删除成功'
    });
  })
});
// ,{session:false}
router.post('/test', passport.authenticate('jwt'), function (req, res, next) {
  console.log(req.user)
  console.log(req.body)
  console.log(req.session)
  // req.session.name = req.user.id
  res.json({
    code: 200,
    message: '测试成功'
  })
});


router.post('/login', function (req, res, next) {
  jwt.sign({
    id: 2
  }, 'yby', {
    expiresIn: 3600
  }, (err, token) => {
    if (err) throw err;
    res.json({
      success: true,
      token: "Bearer " + token
    });
  })
  // console.log(req.session)
  // req.session.name = 'yby'
  // res.json({
  //   success: true,
  //   token: "Bearer "
  // });
});

module.exports = router;