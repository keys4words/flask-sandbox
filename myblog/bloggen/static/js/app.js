// Get the current year for the copyright
$("#year").text(new Date().getFullYear());
CKEDITOR.replace('editor1');

// modals
$('input.add-post').click(function(event) {
    event.preventDefault();
    $.post('\\', data=$('#addpost').serialize(), function(data) {
      if (data.status == 'ok') {
        $('#addPostModal').modal('hide');
        location.reload();
      }
      else {
        $('#addPostModal .modal-content').html(data);
      }
    });
  })