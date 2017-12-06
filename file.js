(function () {
    var c = document.getElementById("c"),
        ctx = c.getContext("2d"),
        w = c.width,
        h = c.height,
        st = 0.001,
        fx = function (x1, r) {
            return (1 + r) * x1 - r * x1 * x1;
        },
        it = function (r) {
            var idx = 0,
                x = 0.001,
                xc = w * ((r-1)/2);
            while (idx++ < 2000) {
                x = fx(x, r);
                ctx.fillRect(xc, (x * h) - 150, 1, 1);
            }
        };
    ctx.fillStyle = "rgba(32,64,128,0.01)";
    for (r = 1; r < 3; r += st) {
        (function (r1) {
            setTimeout(function () {
                it(r1);
            });
        })(r);
    }
})();