 (function(d, s, id) {
      var js, fjs = d.getElementsByTagName(s)[0];
      if (d.getElementById(id)) return;
      js = d.createElement(s); js.id = id;
      js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&version=v2.5";
      fjs.parentNode.insertBefore(js, fjs);
      }(document, 'script', 'facebook-jssdk'));

    $(".comment-reply-btn").click(function(event){
        event.preventDefault();
        $(this).parent().next(".comment-reply").fadeToggle();
    })


$('#likes').click(function(){
    var postid;
    postid = $(this).attr("data-postid");
    $.get('/posts/like/', {slug: postid}, function(data){
               $('#like_count').html(data);
               $('#likes').hide();
    });
});


//AJAX Like buttons (Stackoverflow)

//$('#like').click(function(){
// console.log('am i called');

//      $.ajax({
//               type: "POST",
//               url: "/posts/like/",
//               data: {'slug': $(this).attr('data'), 'csrfmiddlewaretoken': '{{ csrf_token }}'},
//               dataType: "json",
//               success: function(response) {
//                      alert(response.message);
//                      alert('Stories likes count is now ' + response.likes_count);
//                },
//                error: function(rs, e) {
//                       alert(rs.responseText);
//                }
//          }); 
//    })



// AJAX POST
//    $('#a').click(function(){
//      console.log('am i called');

//        $.ajax({
//            type: "POST",
//            url: "{% url 'posts:like' %}",
//            dataType: "json",
//            data: { "id": $(".a").val(), 'csrfmiddlewaretoken': '{{ csrf_token }}' },
//            success: function(data) {
//                alert(data.a);
//            }
//        });

//    });
