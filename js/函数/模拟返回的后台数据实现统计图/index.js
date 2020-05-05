var vm = new Vue({

    el: '#vmchart',

    data: {

        // 绘制统计图（横纵坐标，数据从后台会返回一个数组，数组由对象组成）
        // 统计图数据（timeline：时间轴x）(datanum：数据y)
        chartData: [
            { timeline: "2018-02-01", datanum: "1" },
            { timeline: "2018-02-03", datanum: "2" },
            { timeline: "2018-02-04", datanum: "5" },
            { timeline: "2018-02-06", datanum: "8" }
        ],

        timeline: [], // 时间轴

        datanum: [] // 阅读数

    },

    methods: {

        /**
         * [将时间转换为标准]
         * @param  {[String]} datestr [2018-01-02]
         * @return {[Object]}         [Fri Feb 02 2018 00:00:00 GMT+0800 (中国标准时间)]
         */
        timeDate: function(datestr) {

            var temp = datestr.split("-"); //["2018","01","02"]

            var date = new Date(temp[0], temp[1], temp[2]); // 年月日

            return date;

        },

        /**
         * [给出开始日期和结束日期计算每天日期]
         * @param {[String]} [st] [开始时间]
         *        {[String]} [et] [结束时间]
         *        {[Array]}  [receive] [接收参数]
         * @return {[Array]} [日期数组]
         */
        timer: function(st,et,receive) {
            
            // 开始和结束时间
            var start = st; // 开始时间轴
            
            var end = et; // 结束时间轴
            
            var startTime = this.timeDate(start);
            
            var endTime = this.timeDate(end);
            
            // 判断循环
            while ((endTime.getTime() - startTime.getTime()) >= 0) {
            
                var year = startTime.getFullYear();
            
                var month = startTime.getMonth().toString().length == 1 ? "0" + startTime.getMonth().toString() : startTime.getMonth();
            
                var day = startTime.getDate().toString().length == 1 ? "0" + startTime.getDate() : startTime.getDate();
            
                receive.push(year + "-" + month + "-" + day);
            
                startTime.setDate(startTime.getDate() + 1);
            
            }
            
            return receive;
        },

    }

});

// 执行函数
vm.timer(vm.chartData[0].timeline,vm.chartData[vm.chartData.length - 1].timeline,vm.timeline);

// 定义一个空数组用于存放阅读数
var timeObj = {};

// 先定义新的时间数组 设置默认阅读数为0（数组去重思想）
$.each(vm.timeline,function(i,v){

    timeObj[v] = "0";

});

// 在定义后台返回的数组，赋值到对象中以取代应该不为0的数组
$.each(vm.chartData,function(i,v){

    timeObj[v.timeline] = v.datanum;

});

// 将对象的value值（阅读数）拿出来组成数组
for (var index in timeObj) {

    vm.datanum.push(timeObj[index]);

}

/**
 * 统计图
 */

// 基于准备好的dom，初始化echarts实例
var myChart = echarts.init(document.getElementById('chart'));

// 指定图表的配置项和数据
var option = {
    title: {
        text: '例：文章阅读数'
    },
    tooltip: {},
    legend: {
        data: ['阅读量']
    },
    xAxis: {
        data: vm.timeline //timeline
    },
    yAxis: {},
    series: [{
        name: '阅读量',
        type: 'line',
        data: vm.datanum // datanum
    }]
};

// 使用刚指定的配置项和数据显示图表。
myChart.setOption(option);