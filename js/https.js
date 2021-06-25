var pinables = document.querySelectorAll('img');

Array.prototype.forEach.call(pinables, function(el, i){
    data = el.dataset;
    if (data.pin=='pinIt') {
        el.insertAdjacentHTML('beforebegin', '<a href="http://www.pinterest.com/pin/create/button/?url=' + encodeURIComponent(window.location.href) + '&media=' + encodeURIComponent(el.src) + '&description=' + encodeURIComponent(el.alt) + '" target="_blank" class="pinterest-anchor pinterest-hidden"><div class="pinterest-logo"> </div></a>');
        el.onmouseover = function(){ this.previousSibling.style.display='block'; }
        el.onmouseout = function(){ this.previousSibling.style.display='none'; }
    }
});
