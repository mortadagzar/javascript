class Rectangle {
    constructor(_width,_height,_color){
        console.log('the rectangle is being created');
        this.width=_width;
        this.height=_height;
        this.color=_color;
    }
}
let myRectangle= new Rectangle(3,4,'red');
let myRectangle1= new Rectangle(3,42,'gray');
