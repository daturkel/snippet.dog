// https://stackoverflow.com/a/18484799/8284351
var delay = (function() {
    var timer = 0;
    return function(callback, ms) {
        clearTimeout(timer);
        timer = setTimeout(callback, ms);
    };
})();

var render = (function() {
    var body = {
        code: $('.textarea').val(),
        language: $('#language').val(),
        style: $('#style').val(),
        line_no_type: $('#line_no_type').val(),
    };

    var poster = $.ajax({
        type: "POST",
        url: "/render",
        dataType: 'json',
        contentType: 'application/json',
        data: JSON.stringify(body),
        processData: false,
        success: function(data) {
          $('.result_space').empty().append(data.results);
          $('#output').val(data.results);
          $('#styles').val(data.styles);
          $('#code-style').html(data.styles);
        }
    });
});

$('.textarea').keyup(function() {
    delay(render, 1000);
});

$('select').change(render);
$('input').change(render);

// https://stackoverflow.com/questions/6140632/how-to-handle-tab-in-textarea
$(document).delegate('textarea', 'keydown', function(e) {
  var keyCode = e.keyCode || e.which;

  if (keyCode == 9) {
    e.preventDefault();
    var start = this.selectionStart;
    var end = this.selectionEnd;

    // set textarea value to: text before caret + tab + text after caret
    $(this).val($(this).val().substring(0, start)
                + "    "
                + $(this).val().substring(end));

    // put caret at right position again
    this.selectionStart =
    this.selectionEnd = start + 4;
  }
}); 