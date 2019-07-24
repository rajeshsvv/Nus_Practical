
//creating a variable to store SVG attributes
var graphic=d3.select("#circle")
    .append("svg")              //apply svg attribute
    .attr("width",500)           //initialise the width of object pane
    .attr("height",500)          //initialise the height of object pane

graphic.append("circle")
    .style('stroke',"pink")     //outline color attribute set to purple
    .style('fill','meroon')        //fill color attribute set to red
    .attr("r",100)              //radius attribute set to 100
    .attr("cx",300)             //x co ordinate set to 300
    .attr("cy",100)             // y co oridnate set to 100

//applying action when the mouse pointer hovers over the circle

    .on("mouseover",function(){
        d3.select(this).style("fill","green");
    })
    .on("mouseout",function(){
    d3.select(this).style("fill","yellow");
});
