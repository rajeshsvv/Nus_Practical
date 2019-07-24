function Circle(radius)
{
    // console.log('this',this);
    this.radius=radius;
    this.draw=function()
    {
        console.log('draw');
    }
}

Circle.call({},1);
Circle.apply({},[1,2,3]);
// const Circle1=new Circle('radius',`
// this.radius=radius;
// this.draw=function(){
//     console.log('draw')
// }
// `);

const circle=new Circle(1);
const another=new Circle(1);

// circle.location={x:1};
// let propertyName='center location';
// circle[propertyName]={x:1};

// delete circle[location];

for (let key in circle){
    if(typeof circle[key]!=='function')
    console.log(key,circle[key]);
}

const keys=Object.keys(circle);
console.log(keys);

if ('radius' in circle)
    console.log("Circle has a radius.");