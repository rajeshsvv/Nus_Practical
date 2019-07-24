// 6 Creating a Sample Bar Chart with scaling


var dataset=[1,2,3,4,5]

var svgWidth=500,svgHeight=300,barPadding=5;
var barWidth=(svgWidth/dataset.length);

var svg=d3.select('svg')
    .attr("width",svgWidth)
    .attr("height",svgHeight);


var yscale=d3.scaleLinear()
.domain([0,d3.max(dataset)])
.range([0,svgHeight]);


var barChart=svg.selectAll("rect")
    .data(dataset)
    .enter()
    .append("rect")
    .attr("y",function(d)
    {
        return svgHeight-yscale(d)
    })
    .attr("height",function(d)
    {
        return yscale(d);
    })
    .attr("width",barWidth-barPadding)
    .attr("transform",function(d,i)
    {
        var translate=[barWidth*i,0];
        return "translate("+translate+")";

});


  // 5 Creating Labels to barchart

  var text=svg.selectAll("text")
  .data(dataset)
  .enter()
  .append("text")
  .text(function(d)
  {
      return d;
  })
  .attr("y",function(d,i)
  {
      return svgHeight-d-10;
  })
  .attr("x",function(d,i)
  {
      return barWidth*i;
  })
  .attr("fill","#B64C39");