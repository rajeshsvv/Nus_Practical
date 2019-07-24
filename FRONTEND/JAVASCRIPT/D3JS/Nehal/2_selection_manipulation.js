
// 2 Selection and Manipulation

d3.select();
d3.selectAll();

d3.select('h1').style('color',"purple")
.attr('class',"heading")
.text('updated h1 tag');

d3.select("body").append("p").text("First Paragraph");
d3.select("body").append("p").text("Second Paragraph");
d3.select("body").append("p").text("Third Paragraph");

d3.selectAll('p').style('color','blue');
