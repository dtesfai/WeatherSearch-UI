function getJson(callback){
    let city = $('#city').val();
    $.ajax({
        type: "GET",
        url: "/api/city/" + city,
        success: callback
    })
}

results = {"Snow": "It's snowing!", "Rain": "It's raining.", "Clouds": "It's cloudy."}

$(document).ready(function () {
    // $("#results").hide();
    $("#city").keyup(
        function (e) {
        	if (e.keyCode == 13){
                getJson(function(response){
                    console.log(response);
                    $("#search").hide();
                    $("#name").append(response['name'] + " " + response['country']);
                    $("#sunrise").append(response['sunrise']);
                    $("#sunset").append(response['sunset']);
                    $("#conditions").append(results[response['condit']]);
                    $("#results").show();
                })
        	}
        }
    );
})
