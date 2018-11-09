// $('#city').keydown(function (e){
//     if(e.keyCode == 13){
//       let city = $('#city').val();
//       $.ajax({
//       	type: "GET",
//       	url: "localhost:5000/api/city/" + city
//       })
//     }
// })


$(document).ready(function () {
    $("#city").keyup(
        function (e) {
        	if (e.keyCode == 13){
						let city = $('#city').val();
			      $.ajax({
			      	type: "GET",
			      	url: "localhost:5000/api/city/" + city
			      })
        	}
        }
    );
})
