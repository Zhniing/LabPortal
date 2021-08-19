window.onload = function () {
    var oPre = document.getElementsByClassName('dir')[0];
    var oNext = document.getElementsByClassName('dir')[1];
    var aLi = document.getElementsByTagName('li');
    var arr = [];
    for (var i = 0; i < aLi.length; i++) {
        var oImg = aLi[i].getElementsByTagName('img')[0];
        // console.log(getStyle(aLi[i],'left'));
        // console.log(parseInt(getStyle(aLi[i],'opacity')*100));
        // console.log(getStyle(aLi[i],'z-index'));
        // console.log(oImg.width);
        arr.push([
            parseInt(getStyle(aLi[i], 'top')),
            parseInt(getStyle(aLi[i], 'opacity') * 100),
            parseInt(getStyle(aLi[i], 'z-index')),
            oImg.width
        ]);
        // console.log(arr[i][2]);
    }
    // console.dir(arr);
    oPre.onclick = function () {//左
        arr.push(arr[0]);
        arr.shift();
        for (var i = 0; i < aLi.length; i++) {

            var oImg = aLi[i].getElementsByTagName('img')[0];
            //console.log(arr[i][2]);
            startMove(aLi[i], {
                left: arr[i][0],
                top: arr[i][1],
                opacity: arr[i][2],
            });
            aLi[i].style.zIndex = arr[i][3];
            startMove(oImg, { width: arr[i][4] });
        }
    };
    oNext.onclick = function () {//右
        arr.unshift(arr[arr.length - 1]);
        arr.pop();
        for (var i = 0; i < aLi.length; i++) {

            var oImg = aLi[i].getElementsByTagName('img')[0];

            startMove(aLi[i], {
                left: arr[i][0],
                top: arr[i][1],
                opacity: arr[i][2],
            });

            aLi[i].style.zIndex = arr[i][3];
            startMove(oImg, { width: arr[i][4] });
        }
    };
    function getStyle(obj, attr) {//得到是带单位的数值
        if (obj.currentStyle) {
            return obj.currentStyle[attr];
        } else {
            return getComputedStyle(obj, false)[attr];
        }
    }
}