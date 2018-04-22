
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

    $.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
}});



$("#sel_level").click(
	function(e){

		if($("#sel_level").val()=="block_level")
		{
			$("#sel_dist").prop("disabled",false);

			$.ajax({
                url: "{% url 'district:get_feature' %}",
                method: "POST",
                data:
                {
                    district:"Hello",
                    feature: "World",
                },
                datatype: "json",
                success: function(data) {
                console.log(data);
            }})

		}
		else if($("#sel_level").val()=="village_level")
		{
			$("#sel_dist").prop("disabled",false);	
			$("#get_tlk").prop("disabled",false);
		}
		else{
			$("#sel_dist").prop("disabled",true);	
			$("#get_tlk").prop("disabled",true);	
		}
	}
	);