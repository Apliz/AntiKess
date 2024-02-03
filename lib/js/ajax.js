
var celesTrack = "https://celestrak.org/NORAD/elements/gp.php?";

$(function () {
  $.ajax({
    url: celesTrack,
    data: {
      GROUP: "stations",
      FORMAT: "JSON"
    },
    success: function (response) {
      console.log(response);
      $.ajax({
        type: "GET",
        dataType: 'json',
        async: false,
        url: 'http://localhost:8080/lib/php/WriteToFile.php',
        data: { data: JSON.stringify(response) },
        success: function () { alert("Thanks!"); },
        failure: function () { alert("Error!"); }

      })
    }
  });
});