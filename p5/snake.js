//if loop, multiple conditions (&&), variables, and interactivity
var lastpontX
var lastpointY;
function setup(){
  createCanvas(600, 400);
  starting = true
}
function draw(){
  strokeWeight(1)
  newpointX = mouseX;
  newpointY = mouseY;
  if(starting == true){
    lastpointX = newpointX;
    lastpointY = newpointY;
    starting = false;
  }
  line(lastpointX, lastpointY, newpointX, newpointY);
  lastpointX = newpointX;
  lastpointY = newpointY;

}
