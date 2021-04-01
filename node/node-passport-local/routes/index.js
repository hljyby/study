var express = require('express');
var router = express.Router();
var mysql = require('../sql/index')

/* GET home page. */
router.get('/:page', function (req, res, next) {
  console.log(req.query)
  console.log(req.params)
  let pageSize = 20;
  let sql =
    `
    SELECT * FROM main WHERE title like '%${req.query.message}%' ORDER BY page limit ${((req.params.page - 1)) * 10},${pageSize} ;SELECT COUNT(id) as total FROM main WHERE title like '%${req.query.message}%';
    `;
  // mysql.query(sql, (err, result) => {
  //   if (err) {
  //     console.log(err)
  //     return
  //   }
  // let sql = `SELECT COUNT(id) as total FROM main WHERE title like '%${req.query.message}%';`
  // mysql.getConnection((err, mysql) => { //这个是用线程池实现的，如果工作中用的话可以考虑封装一下
  //   if (err) {
  //     console.log('数据库连接失败')
  //     returny
  //   }
    mysql.query(sql, (err, result1) => {
      // mysql.release();  //把不用的线程放回线程池里，还可以用mysql.end(),结束，这个mysql关键字是线程池的命，我建的变量名是一样的所以，分清。end()函数作用于线程池，release()函数作用于单条线程，destory函数销毁这条线程。
      if (err) {
        console.log(err)
        return
      }
      console.log(result1[1])
      res.render('index', {
        resultdata: result1[0],
        total: result1[1][0].total
      });
      // })


    // })
  })



});

module.exports = router;