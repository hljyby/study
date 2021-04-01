```
container.addEventListener("touchstart", dragStart, false);// 进入
container.addEventListener("touchend", dragEnd, false); // 离开
container.addEventListener("touchmove", drag, false); // 移动

container.addEventListener("mousedown", dragStart, false); // 进入
container.addEventListener("mouseup", dragEnd, false); // 离开
container.addEventListener("mousemove", drag, false);// 移动
```

***1\***|***2\*****Element.getBoundingClientRect()**

返回元素的大小及其相对视口的位置,以css设置宽高作为衡量准备

***1\***|***3\*****offset(只读)**

```
Element.offsetWidth` css宽度,包括`border,padding,scrollbar(水平滚动条),width
Element.offsetHeight` css 高度,包括 `border,padding,scrollbar(垂直滚动条),height
```

`Element.offsetLeft` 左边的偏移值

`Element.offsetTop` 距离顶部的偏移值

```
Element.offsetParent
```

- 如果父级有定位,返回带有定位的父级dom
- 如果父级没有定位,返回body

***1\***|***4\*****client(只读)**

可视区域

`MouseEvent.clientWidth` 元素内部宽度(包括`padding`,不包括`scrollBar,border,margin`)

`MouseEvent.clientHeight` 元素内部高度(包括`padding`,不包括`scrollBar,border,margin`)

`MouseEvent.clientX` 鼠标距离可视区域左边的距离

`MouseEvent.clientY` ... 上边的距离

`Element.clientTop` dom 上边框(`border`)的宽度

`Element.clientLeft` dom 左边框(`border`)的宽度

***1\***|***5\*****scroll**

距离: 可视区域+滚动隐藏的部分

`Element.scrollTop` 读取设置, 距离顶部的距离

`Element.scrollLeft` 读取设置, 距离元素left的距离