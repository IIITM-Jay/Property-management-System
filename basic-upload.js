/* Adapted from https://simpleisbetterthancomplex.com/tutorial/2016/11/22/django-multiple-file-upload-using-ajax.html
   Uploads the users selected files showing them a progress bar.
*/
$(function (){

  $(".js-upload-photos").click(function (){
    $("#fileupload").click();
  });

  $("#fileupload").fileupload({
    dataType:'json',
    sequentialUploads: true,
    start: function(e) {
      $("#modal-progress").modal("show");
    },
    stop: function(e) {
      $("#modal-progress").modal("hide");
    },
    progressall: function (e,data) {
      var progress = parseInt(data.loaded / data.total * 100, 10);
      var strProgress = progress + "%";
      $(".progress-bar").css({"width": strProgress});
      $(".progress-bar").text(strProgress);
    },
    done: function (e,data) {
      if (data.result.is_valid) {
        console.log("I ran")
        $("#gallery tbody").prepend(
          "<tr><td><a href='" + data.result.url +"'>" + data.result.name + "<a/></td></tr>"
        )
      }
    }
  });
});
