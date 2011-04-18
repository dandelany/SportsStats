
makeHistogram = function() {
	var experiment = {
	  trials: 5000, // number of trials
	  variables: 5 // number of random variables
	};
	
	experiment.values = pv.range(experiment.trials).map(function() {
	  return pv.sum(pv.range(experiment.variables), Math.random);
	});
	
	/*
	bins = []
	numBins = pv.max(MarginList)*2 + 1
	for(var i=0; i<numBins; i++) {
	    bins.push([])
	}
	for(var i=0; i<MarginList.length; i++) {
	    bins[MarginList[i]+55].push(MarginList[i])
	}
	*/
	
	
	
	var w = 420,
	    h = 300,
	    //x = pv.Scale.linear(0, experiment.variables).range(0, w),
	    x = pv.Scale.linear(0, pv.max(MarginList)).range(0, w),
	    //bins = pv.histogram(experiment.values).bins(x.ticks(60)),
	    bins = pv.histogram(MarginList).bins(x.ticks(60)),
	    y = pv.Scale.linear(0, pv.max(bins, function(d){return d.y})).range(0, h);
	
	var vis = new pv.Panel()
	    .width(w)
	    .height(h)
	    .margin(20)
	    .canvas("fig");
	
	vis.add(pv.Bar)
	    .data(bins)
	    .bottom(0)
	    .left(function(d) x(d.x))
	    .width(function(d) x(d.dx))
	    .height(function(d) y(d.y))
	    .fillStyle("#aaa")
	    .strokeStyle("rgba(255, 255, 255, .2)")
	    .lineWidth(1)
	    .antialias(false);
	
	vis.add(pv.Rule)
	    .data(y.ticks(5))
	    .bottom(y)
	    .strokeStyle("#fff")
	  .anchor("left").add(pv.Label)
	    .text(y.tickFormat);
	
	vis.add(pv.Rule)
	    .data(x.ticks())
	    .left(x)
	    .bottom(-5)
	    .height(5)
	  .anchor("bottom").add(pv.Label)
	    .text(x.tickFormat);
	
	vis.add(pv.Rule)
	    .bottom(0);
	
	vis.render();
}

$(document).ready(function(){
		
	makeHistogram();
});