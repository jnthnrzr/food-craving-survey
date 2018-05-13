
function filter5(value, type) {
    return value % 10 ? 0 : 1;
}

var range = document.getElementById('range');

range.style.width = '40%';
range.style.margin = 'auto';

noUiSlider.create(range, {
    start: 0,                   // Start with handle at 50
    connect: [true, false],     // Display a colored bar between the handles
    direction: 'ltr',           // Left to Right
    orientation: 'horizontal',  // Orient the slider horizontally
    behaviour: 'tap-drag',      // Move handle on tap, bar is draggable
    step: 1,
    tooltips: true,
    format: {
        to: function (value) {
            return value;
        },
        from: function (value) {
            return value;
        }
    },
    range: {
        'min': 0,
        'max': 100
    },
    pips: {
        mode: 'steps',
        density: 1,
        filter: filter5,
        format: {
            to: function (value) {
                return value;
            },
            from: function (value) {
                return value;
            }
        }
    }
});

var btn = document.getElementById('next-btn');

range.noUiSlider.on('slide', function () {
    btn.classList.remove('invisible');
});

range.noUiSlider.on('update', function (values, handle) {
    $.ajax({
        type: "POST",
        contentType: "application/json; charset=utf-8",
        url: "/api",
        data: JSON.stringify({ rating: values[handle] }),
        success: function (data) {},
        dataType: "json"
    });
});
