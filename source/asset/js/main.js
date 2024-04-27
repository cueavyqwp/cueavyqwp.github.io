// 页面元素加载完时再执行
document.addEventListener( "DOMContentLoaded" , function(){
    // 设置目录按钮
    document.getElementById( "post" ).insertAdjacentHTML( "afterbegin" , "<button id=\"menu-button\" type=\"button\" title=\"目录\"><i class=\"fa-solid fa-bars\"></i></i></button>" )
    document.getElementById( "main" ).insertAdjacentHTML( "beforeend" , "<div id=\"menu\" style=\"display: none;\"></div>" )
    // 添加锚链接与目录
    var headings = document.querySelectorAll(".heading");
    var menu = document.getElementById("menu");
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
        heading.insertAdjacentHTML( "beforeend" , `<a href="#${heading.id}" title="${heading.id}"><i class="fa-solid fa-link fa-fw"></i></a>` );
        menu.insertAdjacentHTML( "beforeend" , `<p>${"-".repeat( parseInt( heading.nodeName.slice( 1 ) ) ).replace( "-" , "|" )}><a href="#${heading.id}" title="${heading.id}">${heading.innerText}</i></a></p>` );
    };
    // 代码块复制事件
    document.addEventListener("click", function( event ){
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
        if ( event.target.parentElement.classList.contains( "packup-button" ) ){
            var pre = event.target.parentElement.parentElement.parentElement.querySelector( "pre" );
            pre.style.display = pre.style.display === "none" ? "block" : "none";
            event.target.parentElement.title = pre.style.display === "none" ? "展开" : "收起";
            event.target.className = pre.style.display === "none" ? "fas fa-angle-left" : "fas fa-angle-down";
        }
        if ( event.target.parentElement.id === "menu-button" ){
            var div = document.getElementById( "menu" );
            div.style.display = div.style.display === "none" ? "flex" : "none";
        }
    });
    // 代码块工具栏
    var divs = document.getElementsByClassName("highlight");
    for ( var i = 0 ; i < divs.length ; i++ ){
        var div = divs.item( i );
        var target = "copy-" + i;
        div.children.item( 0 ).id = target;
        div.insertAdjacentHTML( "afterbegin" , `<div class=\"code-toolsbar\"><button class=\"copy-button\" type=\"button\" title=\"复制\" data-clipboard-target=\"#${target}\"><i class=\"fa-regular fa-clipboard\"></i></button><button class=\"packup-button\" type=\"button\" title=\"收起\"><i class=\"fas fa-angle-down\"></i></button></div>` );
    }
})
