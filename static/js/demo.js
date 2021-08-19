var img = $('#img')[0]
img.onchange = upload_img

function upload_img() {
    console.log('upload')
    let formData = new FormData($("#img-form")[0])
    $.ajax({
        url: '/upload', //请求路径
        type: 'POST', // 请求类型
        data: formData, // 请求数据
        dataType: "JSON", // 返回数据格式
        contentType: false, //表示不处理数据
        processData: false,
        cache: false,
        success: function (data) {
            console.log(data)
            if (data.result === 1) {
                alert("上传成功")
            }else if (data.result === 0) {
                alert("上传失败")
            }
        },
        error: function (data) {
            console.log(data)
        }
    })
}