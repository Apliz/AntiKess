
//The HTML this links to is /templates.html
var celesTrack = "https://celestrak.org/NORAD/elements/gp.php?";

$(function () {
  /* 
  The AJAX GET request to celestrack.org should remain commented out during development to prevent
  overloading their servers during development.

  The commented out ajax is the GET call

  The currently used ajax POST was removed from the SUCCESS callback function() of the celestrack GET
  It currently uses a STUB JSON that mimics an orbital body JSON object.

  When moving from development into production, the POST should be moved back into the ajax GET callback function.

  Custom succes and error messages should be created at some point to deal with the most common basic errors.
  Currently the successMessage parameter in the success callback function returns HTML...
  */
  $("#celestrackButton").on("click", function () {
    $.ajax({
      type: "POST",
      url: "/",
      contentType: "application/json",
      data: JSON.stringify({ "OBJECT_NAME": "ISS (ZARYA)" }),
      success: function (successMessage) {
        console.log(`ajax orbitalBodies POST to flask function completed with message: \n ${successMessage}`)
      },
      error: function (err) {
        console.log(err)
      }
    })
    // $.ajax({
    //   url: celesTrack,
    //   data: {
    //     GROUP: "stations",
    //     FORMAT: "JSON"
    //   },
    //   success: function (response, status) {
    //     console.log(typeof JSON.stringify(response))
    //     $.ajax({
    //       type: "POST",
    //       url: "/",
    //       contentType: "application/json",
    //       data: JSON.parse(response),
    //       success: function (successMessage) {
    //         // console.log(`ajax orbitalBodies POST to flask function completed with message: \n ${successMessage}`)
    //       },
    //       error: function (err) {
    //         console.log(err)
    //       }
    //     })
    //   },
    //   error: function (err) {
    //     console.log(err);
    //   }
    // });
  })
});