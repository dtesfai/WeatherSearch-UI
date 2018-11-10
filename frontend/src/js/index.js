$(document).ready(function () {
    $("#city").keyup(
        function (e) {
        	if (e.keyCode == 13){
			    let city = $('#city').val();
                $.ajax({
                	type: "GET",
                	url: "/api/city/" + city
                })
        	}
        }
    );
})
