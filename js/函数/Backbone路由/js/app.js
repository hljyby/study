$(function(){
    var Workspace = Backbone.Router.extend({

        routes: {
            "": "help", // 默认地址
            "help": "help", // #help
            "search/:query": "search", // #search/kiwis
            "search/:query/p:page": "search" // #search/kiwis/p7
        },
    
        help: function () {
            console.log('help页面');
            $('#content').load('pages/help.htm');
        },
    
        search: function (query, page) {
            console.log('search页面: ', query, page);
            $('#content').load('pages/search.htm');
        },
    
        initialize: function () { // 自执行
            console.log(window.location.hash.replace(/^#+/, ''));
        },
    
        interface: {
            forward: function (url) {
                console.log(url)
                window.location.href = ('#' + url).replace(/^#+/, '#');
            }
        }
    
    });
    
    // 实例化
    new Workspace();
    
    // 开启路由控制
    Backbone.history.start();
})


