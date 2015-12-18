/**
 * Created by andyyang on 15/12/18.
 */
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
$(document).ready(
    function(){
        $(".savebtn").hide();
        $(".emailbtn").click(
            function(){
                $(this).hide();
                $(".emailtd").html("<input type='email' class='change_email'></input>");
                $(".savebtn").show();
            }
        );
        $(".pswbtn").click(
            function(){
                $(".pswtd").html("<input type='password' class='change_psw'></input>");
                $(".savebtn").show();
            }
        );
        $(".savebtn").click(
            function(){
                //email_value = "";
                email_value = $(".change_email").val();
                if(!email_value)
                    email_value = "";
                psw_value = $(".change_psw").val();
                if(!psw_value)
                    psw_value = "";
                $.post('change_account',{email_value:email_value,psw_value:psw_value},
                function(data){
                    $('.savebtn').hide();
                    $(".emailtd").html(data);
                    $('.emailbtn').show();
                    $(".pswtd").html('<button type="button" class="btn btn-default pswbtn">修改</button>');
                });
            }
        );
    }
);