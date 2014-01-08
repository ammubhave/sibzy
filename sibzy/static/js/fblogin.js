var me;

function updateLoginStatus(response) {
  // Here we specify what we do with the response anytime this event occurs. 
  if (response.status === 'connected') {
    // The response object is returned with a status field that lets the app know the current
    // login status of the person. In this case, we're handling the situation where they 
    // have logged in to the app.
    if (document.cookie.indexOf('fbid=') != -1) {
      console.log('Already logged in!');
    } else {
      console.log(response);
      $.ajax({
        type: 'POST',
        url: '/!/auth/login/fb',
        data: { 'access_token': response.authResponse.accessToken },
        dataType: 'json',
        success: function (response) {
          if (response.status == 'success') {
            console.log('Server authentication successful');
          } else {
            console.log('Server authentication failed');
            alert('Server authentication failed');
          }
        }
      }) 
    }
    console.log('Welcome!  Fetching your information.... ');
    FB.api('/me', function(response) {
      console.log('Good to see you, ' + response.name + '.');
      console.log(response);
      $('.fb-name').text(response.name);
      $('.fb-firstname').text(response.first_name);
      $('.fb-lastname').text(response.last_name);
      $('.fb-username').text(response.username);
      me = response;
    });
    
    $('.fb-nologin').hide();   
    $('.fb-login').show();
    //alert('connect');
  } else if (response.status === 'not_authorized') {
    // In this case, the person is logged into Facebook, but not into the app, so we call
    // FB.login() to prompt them to do so. 
    // In real-life usage, you wouldn't want to immediately prompt someone to login 
    // like this, for two reasons:
    // (1) JavaScript created popup windows are blocked by most browsers unless they 
    // result from direct interaction from people using the app (such as a mouse click)
    // (2) it is a bad experience to be continually prompted to login upon page load.
    //FB.login();
    $('.fb-nologin').show();
    $('.fb-login').hide();
    if (document.cookie.indexOf('fbid=') != -1)
      $.ajax({ url: '/!/auth/logout' });

    //alert('connectnotauthorized');
  } else {
    // In this case, t alert('connectnot');he person is not logged into Facebook, so we call the login() 
    // function to prompt them to do so. Note that at this stage there is no indication
    // of whether they are logged into the app. If they aren't then they'll see the Login
    // dialog right after they log in to Facebook. 
    // The same caveats as above apply to the FB.login() call here.
    //FB.login();
    $('.fb-nologin').show();
    $('.fb-login').hide();
    if (document.cookie.indexOf('fbid=') != -1)
      $.ajax({ url: '/!/auth/logout' });

     //alert('connectnot');
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
  console.log('fbinit');
  // Here we subscribe to the auth.authResponseChange JavaScript event. This event is fired
  // for any authentication related change, such as login, logout or session refresh. This means that
  // whenever someone who was previously logged out tries to log in again, the correct case below 
  // will be handled. 
  FB.getLoginStatus(function(response) {
 //   updateLoginStatus(response);
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