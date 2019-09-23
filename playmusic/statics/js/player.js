var root = '/music/' ;
var path = [];

function init() {
    load(path);
    $('#player').bind('ended', next);
    $('#btn').click(next);
}

function load(path)  {
    var url = root + path.join('/');
    $.ajax({
            url: url,
            dataType: "json",
            success: function(data) {
                listFile(data)
            },
        });
}
function listFile(files) {
    var $b = $('#playlist').empty();
    function addToList(i, f) {
        if (f.Name[0] == '.' || f.Name[0] == ':') return;
        var dir = f.IsDir;
        if(dir) return;
        $('<a></a>').text(f.Name).data('file', f)
            .addClass("file")
            .appendTo($b)
            .click(clickFile);
    }
    $.each(files, addToList);
}

function clickFile(e) {
    var f = $(e.target).data('file');
    var url= 'download/?file='+f.Name;
    $('#playlist a').removeClass('playing');
    $(e.target).addClass('playing')
    $('#player').attr('src', url);
    $('#player').play();
}
function next() {
    var $next = $('#playlist a.playing').next();
    if ($next.length) $next.click();
}

(function() {
    google.load("jquery", "1.3.1");
    google.setOnLoadCallback(init);
    $('#refresh').on('click',function(){
        load(path);
    });
}());

