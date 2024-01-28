var celesTrack = "https://celestrak.org/NORAD/elements/gp.php?";

$(function () {
  $.ajax({
    url: celesTrack,
    data: {
      CATNR: "25544",
      FORMAT: "TLE"
    },
    success: function (data, status, jqXHR) {
      console.log("success!");
      console.log(data);
      console.log("#################");
      console.log(status);
      console.log("#################");
      console.log(jqXHR);
    }
  });
});