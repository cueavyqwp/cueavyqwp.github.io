// 页面元素加载完时再执行
document.addEventListener( "DOMContentLoaded" , function(){
    // 添加锚链接
    var headings = document.querySelectorAll(".heading");
    var heading_names = new Array();
    for ( var i = 0 ; i < headings.length ; i++ ){
        var heading = headings.item( i );
        heading.id = heading.innerText;
        if ( heading.id in heading_names ){
            heading_names[ heading.id ] += 1;
            heading.id = `${heading.id}-${heading_names[ heading.id ]}`
        } else {
            heading_names[ heading.id ] = 0;
        }
        heading.innerHTML += `<a href="#${heading.id}"><i class="fa-solid fa-link fa-fw"></i></a>`;
    };
    // 代码块复制事件
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
    // 代码块工具栏
    var divs = document.getElementsByClassName("highlight");
    for ( var i = 0 ; i < divs.length ; i++ ){
        var div = divs.item( i );
        var target = "copy-" + i;
        div.children.item( 0 ).id = target;
        div.insertAdjacentHTML( "afterbegin" , `<div class=\"code-toolsbar\"><button class=\"copy-button\" type=\"button\" title=\"copy\" data-clipboard-target=\"#${target}\"><i class=\"fa-regular fa-clipboard\"></i></button><button class=\"packup-button\" type=\"button\" title=\"packup\"><i class=\"fas fa-angle-down\"></i></button></div>` );
    }
})