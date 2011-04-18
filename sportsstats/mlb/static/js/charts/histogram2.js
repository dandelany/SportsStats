
makeHistogram2 = function() {
	var r = Raphael("fig"),
                    fin = function () {
                        this.flag = r.g.popup(this.bar.x, this.bar.y, this.bar.value || "0").insertBefore(this);
                    },
                    fout = function () {
                        this.flag.animate({opacity: 0}, 300, function () {this.remove();});
                    },
                    fin2 = function () {
                        var y = [], res = [];
                        for (var i = this.bars.length; i--;) {
                            y.push(this.bars[i].y);
                            res.push(this.bars[i].value || "0");
                        }
                        this.flag = r.g.popup(this.bars[0].x, Math.min.apply(Math, y), res.join(", ")).insertBefore(this);
                    },
                    fout2 = function () {
                        this.flag.animate({opacity: 0}, 300, function () {this.remove();});
                    };
                r.g.txtattr.font = "12px 'Fontin Sans', Fontin-Sans, sans-serif";
                
                r.g.text(160, 10, "Single Series Chart");
                
                r.g.barchart(10, 10, 300, 220, [[55, 20, 13, 32, 5, 1, 2, 10]], {type:'soft', axis: '0 0 1 1'}).hover(fin, fout);

                // c.bars[1].attr({stroke: "#000"});

}

$(document).ready(function(){
		
	makeHistogram2();
});