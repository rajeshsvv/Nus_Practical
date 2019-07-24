var data=[
    [300,150],
    [240,90],
    [320,400],
    [120,120],
    [400,200],
    [30,360],
    [250,200],
    [390,100]
]

var barchart_width=800;
var barchart_height=400;

var svg=d3.select("#barchart")
            .append("svg")
            .attr("height",barchart_height)
            .attr("width",barchart_width)


// create a circle

svg.selectAll("circle")
            .data(data)
            .enter()
            .append("circle")
            .attr("cx",function(d)
            {
                return d[0];
            })
            .attr("cy",function(d)
            {
                return d[1];
            })
            .attr("r",function(d)
            {
                return d[1];
            })
            .attr("fill","grey");