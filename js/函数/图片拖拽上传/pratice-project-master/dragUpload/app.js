var fs = require("fs");
var express = require("express");
var multer = require("multer");

var app = express();
var upload = multer({ dest: "upload/" });
//设置跨域访问
app.all("*", function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "X-Requested-With");
  res.header("Access-Control-Allow-Methods", "PUT,POST,GET,DELETE,OPTIONS");
  res.header("X-Powered-By", " 3.2.1");
  // res.header("Content-Type", "application/json;charset=utf-8");
  next();
});
// 单图上传
// app.post("/upload", upload.single("file"), function(req, res, next) {
//   console.log('请求',req)
//   var file = req.file;
//   // console.log(file);
//   var fileName = "";
//   if (file != undefined) {
//     fileName = new Date().getTime() + "-"+ file.originalname;
//     fs.renameSync(req.file.path, __dirname + "\\upload" + "\\" + fileName);
//   }
//   res.send({ code: 1, url: "127.0.0.1:3000/upload/" + fileName });
// });

// 多图上传
app.post("/upload-multiply", upload.array("file", 2), function(req, res, next) {
  var files = req.files;
  var fileName = "";
  if (files.length > 0) {
    files.forEach(item => {
      fileName = new Date().getTime() + "-" + item.originalname;
      fs.renameSync(item.path, __dirname + "\\upload" + "\\" + fileName);
    });
    res.send({ code: 1, url: "127.0.0.1:3000/upload/" + fileName });
  } else {
    res.send({ code: 0 });
  }
});

//访问上传后图片
app.get("/upload/*", function(req, res) {
  res.sendFile(__dirname + req.url);
  console.log("Request for " + req.url + " received.");
  // res.send(req.url)
});

app.listen(3000);
