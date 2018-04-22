$('#b1').on('click', function(event){
    event.preventDefault();
    console.log("working")
    create_post();
});
var i=1;
function create_post(){
    console.log("post working")

    $.ajax({
        url : "new_form",

    success: function(form) { // on success..
        console.log('<div id="adiv'+ parseInt(i+1) +'"></div>')
         $('#adiv'+i).html(form+'<div id="adiv'+ parseInt(i+1) +'"></div>')
         i++;
        }

        });
};
//Function To Submit Form------------

$('#form1').on('submit', function(event){
    event.preventDefault();
    console.log("form function")  // sanity check
    submit_form();
});

function submit_form(){
    console.log("submit_form working");
    $.ajax({
        url : $('#form1').attr('action'),
        type : $('#form1').attr('method'),
        data : $('#form1').serialize(),

        success : function(data){
        console.log(data)
            $('#did').html(data)
        }
    });
};
