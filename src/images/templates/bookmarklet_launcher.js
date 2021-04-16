(function(){
if (window.myBookmarklet !== undefined){
myBookmarklet();
}
else {
document.body.appendChild(
document.createElement('script')
).src='https://15d5f6d133c7.ngrok.io/static/js/bookmarklet.js?r=' +
Match.floor(Match.random()*99999999999999999999);
}
})();



(function(){
    if (window.myBookmarklet !== undefined){
        myBookmarklet();
    }
    else {
        document.body.appendChild(document.createElement('script')).src='https://15d5f6d133c7.ngrok.io/static/js/bookmarklet.js?r='+Math.floor(Math.random()*99999999999999999999);
    }
})();