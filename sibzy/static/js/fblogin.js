var me;

function updateLoginStatus(response) {
  return;
  // Here we specify what we do with the response anytime this event occurs. 
  if (response.status === 'connected') {
    
    if (!server_status) {
      $.ajax({
        type: 'POST',
        url: '/!/auth/login/fb',
        data: { 'access_token': response.authResponse.accessToken },
        dataType: 'json',
        success: function (response) {
          if (response.status == 'success') {
            // We are logged in on the server. Reload the page.
            document.location.reload();
          } else {
            // Server authentication was not successful. Alert the user.
            alert('Server authentication failed. Code: 1');
          }
        }
      })
    }
    
    /*
    console.log('Welcome!  Fetching your information.... ');
    FB.api('/me', function(response) {
      console.log('Good to see you, ' + response.name + '.');
      console.log(response);
      $('.fb-name').text(response.name);
      $('.fb-firstname').text(response.first_name);
      $('.fb-lastname').text(response.last_name);
      $('.fb-username').text(response.username);
      $('.fb-picture').attr('src', 'http://graph.facebook.com/' + response.username + '/picture?type=square');
      me = response;
    });
    
    $('.fb-nologin').hide();   
    $('.fb-login').show();
    */
    //alert('connect');
  } else {
    if (server_status) {
      document.location = '/auth/logout';
    }
    /*$('.fb-nologin').show();
    $('.fb-login').hide();
    if (document.cookie.indexOf('fbid=') != -1)
      */
    // alert('connectnot');
  }
}

window.fbAsyncInit = function() {
  FB.init({
    appId      : '259749734165537',
    channelUrl : '//www.sibzy.com/channel.html',
    status     : true, // check login status
    cookie     : true, // enable cookies to allow the server to access the session
    xfbml      : true  // parse XFBML
  });
  //console.log('fbinit');
  //$('.fb-login').hide();
  //$('.fb-nologin').hide();
  // Here we subscribe to the auth.authResponseChange JavaScript event. This event is fired
  // for any authentication related change, such as login, logout or session refresh. This means that
  // whenever someone who was previously logged out tries to log in again, the correct case below 
  // will be handled. 
  FB.getLoginStatus(function(response) {
    updateLoginStatus(response);
  });
  FB.Event.subscribe('auth.authResponseChange', function(response) {
    updateLoginStatus(response);
  });
};

// Load the SDK asynchronously
(function(d){
 var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
 if (d.getElementById(id)) {return;}
 js = d.createElement('script'); js.id = id; js.async = true;
 js.src = "//connect.facebook.net/en_US/all.js";
 ref.parentNode.insertBefore(js, ref);
}(document));

// Here we run a very simple test of the Graph API after login is successful. 
// This testAPI() function is only called in those cases. 
//function testAPI() {
//  console.log('Welcome!  Fetching your information.... ');
//  FB.api('/me', function(response) {
//    console.log('Good to see you, ' + response.name + '.');
//  });
//}