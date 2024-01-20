var headings = document.querySelectorAll("#post h1, h2, h3, h4, h5, h6");
var len = headings.length;
for ( var i = 0 ; i < len ; i++ ){
    var heading = headings.item( i );
    heading.innerHTML += `<a href=\"#${heading.id}\"></i><i class=\"fa-solid fa-link fa-fw\"></i></a>`;
};

var clipboard = new ClipboardJS("#post .copy-button");
clipboard.on("success" , function( event ) {
    event.clearSelection();
});
clipboard.on( "error" , function( event ) {
    console.log( event );
});
var divs = document.getElementsByClassName("highlight");
var len = divs.length;
for ( var i = 0 ; i < len ; i++ ){
    var div = divs.item( i );
    var target = "copy-" + i;
    div.children.item( 0 ).id = target;
    div.insertAdjacentHTML( "afterbegin" , `<div class=\"code-toolsbar\"><button class=\"copy-button\" type=\"button\" title=\"copy\" data-clipboard-target=\"#${target}\"><i class=\"fa-regular fa-clipboard\"></i></button><button class=\"packup-button\" type=\"button\" title=\"packup\"><i class=\"fas fa-angle-down\"></i></button></div>` );
    var button = div.children.item( 0 ).children.item( 1 );
    var icon = button.children.item( 0 );
    var pre = div.children.item( 1 );
    button.onclick = function(){
        if ( pre.style.display === "none" ){
            pre.style.display = "block";
            icon.setAttribute( "class" , "fas fa-angle-down" );
        }else{
            pre.style.display = "none";
            icon.setAttribute( "class" , "fas fa-angle-left" );
        }
    };
}
