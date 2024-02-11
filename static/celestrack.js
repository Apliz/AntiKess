//The HTML this links to is /templates.html
//The JSON is currently returned into the console.
var celesTrack = "https://celestrak.org/NORAD/elements/gp.php?";
// console.log("the file is called.")
$(function () {
  // console.log("document.ready")
  $("#celestrackButton").on("click", function () {
    // console.log("the click callback..")
    $.ajax({
      url: celesTrack,
      data: {
        GROUP: "stations",
        FORMAT: "JSON"
      },
      success: function (response, status) {
        $.ajax({
          type: "POST",
          url: "/",
          contentType: "application/json",
          dataType: "json",
          data: JSON.stringify(response),
          success: function (successMessage) {
            console.log("ajax orbitalBodies POST to flask function completed!")
            $(p).append(successMessage)
          },
          error: function (err) {
            console.log(err)
          }
        })
      },
      error: function (err) {
        console.log(err);
      }
    });
  })
});