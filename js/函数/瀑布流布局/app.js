window.onload = () => {
    var heightArr = imgLocation();
    this.onresize = () => {
        heightArr = imgLocation();
    }

    // 检测是否能滚动
    let app = document.getElementById('app');
    var timer = setInterval(() => {
        if (app.scrollTop + app.clientHeight > Math.min.apply(null, heightArr)) {
            heightArr = checkScroll(app, heightArr)
        } else {
            clearInterval(timer)
        }
    }, 200)
    app.onscroll = () => {
        heightArr = checkScroll(app, heightArr)
    }
}
// 检测滚动
const checkScroll = (scrollElement, heightArr) => {
    if (scrollElement.scrollTop + scrollElement.clientHeight > Math.min.apply(null, heightArr)) {
        for (let i = 0; i < heightArr.length; i++) {
            var item = document.createElement('div');
            item.className = 'item';
            document.getElementById('box').appendChild(item)
            var imgBox = document.createElement('div');
            imgBox.className = 'imgBox';
            item.appendChild(imgBox);
            var img = document.createElement('img');
            var imgName = Math.floor(Math.random() * 10 + 1);
            img.src = "imgs/" + (imgName < 10 ? ('0' + imgName) : '10') + ".jpg"
            imgBox.appendChild(img)
        }
    }
    return imgLocation();
}
// 图片位置
const imgLocation = () => {
    let box = document.getElementById('box');
    let item = document.getElementsByClassName('item'); // 所有图片集合
    let viewWidth = document.documentElement.clientWidth;
    let imgWidth = item[0].offsetWidth;
    let colNum = Math.floor(viewWidth / imgWidth)
    box.style.width = imgWidth * (colNum < item.length ? colNum : item.length) + 'px';
    let itemHeightArr = [];
    for (let i = 0; i < item.length; i++) {
        if (i < colNum) {
            itemHeightArr[i] = item[i].offsetHeight;
            item[i].style.top = '0px';
            item[i].style.left = imgWidth * i + 'px';
        } else {
            let minHeight = Math.min.apply(null, itemHeightArr)
            item[i].style.top = minHeight + 'px';
            item[i].style.left = imgWidth * itemHeightArr.indexOf(minHeight) + 'px';
            itemHeightArr[itemHeightArr.indexOf(minHeight)] += item[i].offsetHeight;
        }
    }
    return itemHeightArr;
}