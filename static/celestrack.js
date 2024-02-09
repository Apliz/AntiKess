//The HTML this links to is /templates.html
//The JSON is currently returned into the console.
var celesTrack = "https://celestrak.org/NORAD/elements/gp.php?";

$(function () {
  $("#celestrackButton").on("click", function () {
    $.ajax({
      url: celesTrack,
      data: {
        GROUP: "stations",
        FORMAT: "JSON"
      },
      success: function (response, status) {
        console.log(status)
        console.log("#########")
        console.log(response)
      }
    });
  })
});