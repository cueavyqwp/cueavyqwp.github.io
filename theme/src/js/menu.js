var headings = document.querySelectorAll("#post h1, h2, h3, h4, h5, h6");
var menu = document.getElementById("menu");
var len = headings.length;
for ( var i = 0 ; i < len ; i++ ){
    var heading = headings.item( i );
    heading.innerHTML += `<a href=\"#${heading.id}\"></i><i class=\"fa-solid fa-link fa-fw\"></i></a>`;
    menu.insertAdjacentHTML( "beforeend" , `<a href=\"#${heading.id}\" class=\"menu-${heading.nodeName.toLowerCase()}\">a</a>` );
};