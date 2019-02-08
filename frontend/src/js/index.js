function getJson(callback){
    let city = $('#city').val();
    $.ajax({
        type: "GET",
        url: "/api/city/" + city,
        success: callback
    })
}

function formatTemp(val){
    return val + '\u00b0C';
}

results = {"Snow": "It's snowing!", "Rain": "It's raining.", "Clouds": "It's cloudy.",
 "Drizzle": "It's kinda raining.", "Clear": "Clear skies!"}

$(document).ready(function () {
    // $("#results").hide();
    $("#city").keyup(
        function (e) {
        	if (e.keyCode == 13){
                getJson(function(response){
                    $("#search").hide();
                    $("#name").append(response['name']);
                    $("#conditions").append(results[response['condit']]);
                    $("#temperature").append(formatTemp(response['temp']) + ' (High: ' +
                     formatTemp(response['temp_max']) + ' - Low: ' + formatTemp(response['temp_min']) + '),');
                    $("#wind").append(response['wind_speed'] + 'm/s ' + response['wind_deg'] + '.');
                    $("#results").show();
                })
        	}
        }
    );

    $(".modal-button").click(function() {
        $(".modal").addClass('is-active');
    });

    $(".modal-close, .modal-background").click(function() {
        $(".modal").removeClass('is-active');
    });
})
