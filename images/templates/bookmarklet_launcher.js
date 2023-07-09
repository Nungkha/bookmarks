//  Since the JavaScript code will be stored as a bookmark, we will not be able to update it after the user 
// has added it to their bookmarks bar. This is an important drawback that you can solve by implementing 
// a launcher script. Users will save the launcher script as a bookmark, and the launcher script will load 
// the actual JavaScript bookmarklet from a URL. By doing this, you will be able to update the code of the 
// bookmarklet at any time. This is the approach that we will take to build the bookmarklet. Let’s start! 


(function(){
    if(!window.bookmarklet) {
        bookmarklet_js = document.body.appendChild(document.createElement('script'));
        bookmarklet_js.src = '//127.0.0.1:8000/static/js/bookmarklet.js?r='+Math.floor(Math.random()*9999999999999999);
        window.bookmarklet = true;
    }
    else {
        bookmarkletLaunch();
    }
})();