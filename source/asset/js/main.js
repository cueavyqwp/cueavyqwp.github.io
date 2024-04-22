var headings = document.querySelectorAll("#post h1, h2, h3, h4, h5, h6");
var len = headings.length;
for ( var i = 0 ; i < len ; i++ ){
    var heading = headings.item( i );
    heading.id = `heading-${i}`;
    heading.innerHTML += `<a href="#heading-${i}"><i class="fa-solid fa-link fa-fw"></i></a>`;
};

document.addEventListener("click", function(event){
    if ( event.target.classList.contains( "copy-button" ) ){
        var id = event.target.dataset.clipboardTarget;
        var element = document.querySelector( id );
        var clipboard = new ClipboardJS( event.target , {
            target: function(){
                return element;
            }
        });
        clipboard.on( "success" , function( event ){
            event.clearSelection();
        });
        clipboard.on( "error" , function( event ){
            console.error( event.action );
        });
    }
    if ( event.target.classList.contains( "packup-button" ) || event.target.parentElement.classList.contains( "packup-button" ) ){
        var button = event.target.closest( ".packup-button" );
        var pre = button.parentElement.nextElementSibling;
        var icon = button.querySelector( "i" );
        pre.style.display = pre.style.display === "none" ? "block" : "none";
        icon.className = pre.style.display === "none" ? "fas fa-angle-left" : "fas fa-angle-down";
    }
});

var divs = document.getElementsByClassName("highlight");
var len = divs.length;
for ( var i = 0 ; i < len ; i++ ){
    var div = divs.item( i );
    var target = "copy-" + i;
    div.children.item( 0 ).id = target;
    div.insertAdjacentHTML( "afterbegin" , `<div class=\"code-toolsbar\"><button class=\"copy-button\" type=\"button\" title=\"copy\" data-clipboard-target=\"#${target}\"><i class=\"fa-regular fa-clipboard\"></i></button><button class=\"packup-button\" type=\"button\" title=\"packup\"><i class=\"fas fa-angle-down\"></i></button></div>` );
}
