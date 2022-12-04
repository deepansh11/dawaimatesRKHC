function loginCheck(){
    var body=JSON.stringify({
         email:$('#email').val(),
         password:$('#password').val(),
         fromMobile:false,
        });
    $.ajax({
        method: "POST",
        url: "/login/validateCreds/",
        data: body,
        success: function (response) {
          if (response["status"] == "error") {
            $("#loginFail").toast("show");
            $("#email").val(""); 
            $("#password").val("");
          } else if (response["status"] == "successForWeb"){
            $("#loginSuccess").toast("show");
            setTimeout(function() {
                $(location).prop('href', '../home/dashboard/');
                }, 200);
          } 
        },
      })
}