// Factory Function

function createCircle(radius)
{
    return {
        radius,
        draw:function(){
            console.log('draw');
        }
    };
}
let circle=createCircle(2);

// constructor function

function Circle(radius)
{
    // console.log('this',this);
    this.radius=radius;
    this.draw=function()
    {
        console.log('draw');
    }
}

let another=new Circle(6);
