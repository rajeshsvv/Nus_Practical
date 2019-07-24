// console.log('Hello world');

//factory Fucntion  to create object
function createCircle(radius)
{
    return{
        radius,
         draw:function(){
             console.log("draw method");
         }     
    };
}

let circle=createCircle(2);
circle.draw();