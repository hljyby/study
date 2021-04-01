var mysql = require('mysql')
var fs = require('fs')


/**
 * mysql数据库
 * user:'用户名'
 * password：‘密码’
 * database：‘数据库名’
 * 在node这个单线程里可以不断开mysql链接一直用一条
 * 用链接池的时候要释放使用完的链接
 * 如果连接断开可以百度搜索
 */
var connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  password: '1234',
  database: 'bluedata',
  multipleStatements: true //可以同时查多条sql语句,但是有被sql注入的风险
});

connection.connect(function (err) {
  if (err) {
    console.error('error connecting: ' + err.stack);
    return;
  }
  console.log('connected as id ' + connection.threadId);
});
//------------------------------------------------------------------------------------
/**
 * 
 * 连接池
 * 
 * 
 * 
 */

// var connection = mysql.createPool({
//   host: 'localhost',
//   user: 'root',
//   password: '1234',
//   database: 'bluedata',
//   multipleStatements: true //可以同时查多条sql语句,但是有被sql注入的风险
// });



//-------------------------------------------------------------------------------------

// var values;
// fs.readFile('./blueData.json', 'utf8', (err, data) => {
//   // console.log(data)

//   values = JSON.parse(data).map(v => {
//     return Object.values(v)
//   })
//   /**
//    * 
//    * mysql 批量新增
//    * 
//    */
//   // var sql = "INSERT INTO main(`url`,`title`,`parentsUrl`, `page`,`date`,`type`,`company`) VALUES ?";
//   // connection.query(sql, [values], function (err, rows, fields) {
//   //   if (err) {
//   //     console.log('INSERT ERROR - ', err.message);
//   //     return;
//   //   }
//   //   console.log(rows)
//   //   console.log(fields)
//   //   console.log("INSERT SUCCESS");
//   // })


//------------------------------------------------------------------------------------

//   /**
//    * 
//    * mysql 删除
//    * 
//    * 
//    */
//   // var delSql = `DELETE FROM main where title='SM'`;
//   // connection.query(delSql, function (err, rows, fields) {
//   //   if (err) {
//   //     console.log('INSERT ERROR - ', err.message);
//   //     return;
//   //   }
//   //   console.log(rows)
//   //   console.log(fields)
//   //   console.log("DEL SUCCESS");
//   // })
// })

//------------------------------------------------------------------------------------
/*
 * 
 * 增加单条数据
 * mysql
 * 
 * 
 */

//方法一
// let data = [['http://38.103.161.16/forum/thread-10782128-1-3.html', '国内SM大神现场教学玩出性爱新境界【帝王调教女奴】首次双飞调教玩操两白嫩淫荡小母狗', 'http://38.103.161.16/forum/forum-25-4.html', '4', '2020-8-16', '国产', '第一会所']]
// var sql = "INSERT INTO main(`url`,`title`,`parentsUrl`, `page`,`date`,`type`,`company`) VALUES ?";
// connection.query(sql, [data], function (err, result) {
//   if (err) {
//     console.log('INSERT ERROR - ', err.message);
//     return;
//   }+
//   console.log(result)
//   console.log("ONE INSERT SUCCESS");
// })


//方法二
// let data = {
//   url: 'http://38.103.161.16/forum/thread-10782128-1-3.html',
//   title: '国内SM大神现场教学玩出性爱新境界【帝王调教女奴】首次双飞调教玩操两白嫩淫荡小母狗',
//   parentsUrl: 'http://38.103.161.16/forum/forum-25-4.html',
//   page: '4',
//   date: '2020-8-16',
//   type: '国产',
//   company: '第一会所'
// }
// var sql = "INSERT INTO main SET ?";
// [1, 2, 3, 4, 5].forEach(v => {
//   connection.query(sql, data, function (err, result) {
//     if (err) {
//       console.log('INSERT ERROR - ', err.message);
//       return;
//     } +
//     console.log(result)
//     console.log("ONE INSERT SUCCESS");
//   })
// })

//------------------------------------------------------------------------------------


module.exports = connection