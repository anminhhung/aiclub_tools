var index = 0;
var total_of_images = 0;

function loadpage(){
    getImgFileName(1);
    index = 1
}

function getImgFileName(index){
    $.ajax({
        url: '/get_img_name?index='+index,
        type: 'get',
        dataType: 'json',
        contentType: 'application/json',  
        success: function (response) {
            if (response['code'] == 1001) {
                alert("[Lỗi] Không nhận được phản hồi từ server, vui lòng kiểm tra lại!");
            }
            console.log(response);
            filepath = response['data']['image_path'];
            number_index = response['data']['index'];
            total_file = response['data']['total_file'];

            total_of_images = parseInt(total_file);
            
            // console.log(number_index)
            // document.getElementById(number_index).value = String(number_index);
            // drawImagePath("/get_img?filepath="+filepath);
            // drawbox("https://miro.medium.com/max/3840/1*_o9Z6bf_hnHlHcuEz5RUoA.jpeg");
            drawbox("/get_img?filepath="+filepath)
            // document.getElementById("total_file").innerHTML = total_file;
        }
    }).done(function() {
        
    }).fail(function() {
        alert('Fail!');
    });
}

function drawImagePath(src) {
    var canvas = document.getElementById("preview_img");
    IMGSRC = src;
    var context = canvas.getContext('2d');
    var imageObj = new Image();
    imageObj.onload = function() {
        canvas.width = this.width;
        canvas.height = this.height;
        context.drawImage(imageObj, 0, 0, this.width,this.height);
    };
    imageObj.src = src;
}

// $(document).ready(function () {
function drawbox(image_path) {
    // Initialize the bounding-box annotator.
    var annotator = new BBoxAnnotator({
    url: image_path,
    input_method: 'fixed',    // Can be one of ['text', 'select', 'fixed']
    labels: "object",
    guide: true,
    onchange: function (entries) {
        // Input the text area on change. Use "hidden" input tag unless debugging.
        // <input id="annotation_data" name="annotation_data" type="hidden" />
        // $("#annotation_data").val(JSON.stringify(entries))
        $("#annotation_data").text(JSON.stringify(entries, null, "  "));
        console.log("entries: " + entries);
    }
    });
    // Initialize the reset button.
    $("#reset_button").click(function (e) {
    annotator.clear_all();
    })
};

function view_previous_image(){
    index = parseInt(index)
    if (index > 0) {
        index = index - 1;
    }

    document.getElementById("bbox_annotator").innerHTML = "";
    getImgFileName(index);
}

function view_next_image(){
    index = parseInt(index) ;

    if (index <  total_of_images-1){
        index += 1;
    }
    else{
        index = 0;
    }
    document.getElementById("bbox_annotator").innerHTML = "";
    getImgFileName(index);
}

document.onkeydown = function(evt) {
    evt = evt || window.event;
    switch (evt.keyCode) {
        // case 13:
        //     save_info_idcard();
        //     break;
        case 37:
           view_previous_image();
           break;
        case 39:
           view_next_image();
           break;
    }
};
