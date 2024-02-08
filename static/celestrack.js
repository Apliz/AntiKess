//The html ID is "test" and this is incorrect. Needs changing to something better
//The HTML this links to is /templates.html
//The JSON is currently returned into the console.
var celesTrack = "https://celestrak.org/NORAD/elements/gp.php?";
$(function () {
  $("#test").on("click", function () {
    console.log("test")
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