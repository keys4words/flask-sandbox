// $(document).ready(function() {

//     $('.updateButton').on('click', function() {
//         var member_id = $(this).attr('member_id');
//         var name = $('#nameInput'+member_id).val();
//         var email = $('#emailInput'+member_id).val();

//         req = $.ajax({
//             url : '/update',
//             type : 'POST',
//             data : { name : name, email : email, id : member_id }
//         });

//         req.done(function(data) {
//             $('#memberSection'+member_id).fadeOut(1000).fadeIn(1000);
//             $('#memberNumber'+member_id).text(data.member_num);
//         });
//     });
// });

$('#popupbtn').click(function(event) {
    event.preventDefault();
    $.post('\popup', data=$('#editForm').serialize(), function(data) {
      if (data.status == 'ok') {
        $('#exampleModal').modal('hide');
        location.reload();
      }
      else {
        console.log('else clause');
        $('#exampleModal .modal-content').html(data);
      }
    });
  })