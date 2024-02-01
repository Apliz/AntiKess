var celesTrack = "https://celestrak.org/NORAD/elements/gp.php?";

$(function () {
  $.ajax({
    url: celesTrack,
    data: {
      GROUP: "cosmos-2251-debris",
      FORMAT: "JSON"
    },
    success: function (data, status, jqXHR) {
      console.log(status);
      console.log("#################");
      //TLE string
      console.log(data);
      console.log("#################");
      //Object
      console.log(jqXHR);
      $("#canvas").append(JSON.stringify(data));
    }
  });
});