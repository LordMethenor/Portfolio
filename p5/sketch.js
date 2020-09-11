//if loop, multiple conditions (&&), variables, and interactivity
xList = []
oldPixels = []
timePixels = []
timeChange = []
over = false
var start1;
var cursor1;
var click1;
var starting1;
var starting2;
function setup(){
  createCanvas(400, 400);
  starting1 = true;
  starting2 = true;
  frameRate(100);
  background('#fff')
  loadPixels();
  for (var i = 0; i < pixels.length; i = i + 4) {
    timePixels[i] = 0;
  }
  strokeCap(SQUARE);
  cursor1 = loadImage("images/cursor.png");
  click1 = loadImage("images/click.png");
  start1 = loadImage("images/start.png");
  strokeWeight(3);
  stroke('rgba(10,10,10,.75)');
}
function draw(){
  if(over == true){
    var score = xList.length;
    var restartText = "The game is over. Your score is " + score + ".";
    alert(restartText);
    noLoop()
  }else{
    if  (starting1 == true){
      image(start1, 0, 0);
      if  (mouseX >= 154 && mouseX <= 254 && mouseY >= 154 && mouseY <= 254)  {
        image(click1, mouseX-20, mouseY-20);
        if  (mouseIsPressed)  {
          starting1 = false;
          background('#fff');
        }
      }else {
        image(cursor1, mouseX-10, mouseY-10);
      }
    }else if (starting2 == true) {
      lastpointX = mouseX;
      lastpointY = mouseY;
      starting2 = false;
    }else {
      loadPixels();
      for (var i = 0; i < pixels.length; i = i + 4) {
        oldPixels[i] = pixels[i];
      }
      var i;
      xList[xList.length] = mouseX
      newpointX = mouseX;
      newpointY = mouseY;
      line(lastpointX, lastpointY, newpointX, newpointY);
      lastpointX = newpointX;
      lastpointY = newpointY;
      loadPixels();
      timeChange[timeChange.length] = new Date();
      for (var i = 0; i < pixels.length; i = i + 4) {
        if (pixels[i] !== oldPixels[i]) {
          if (timePixels[i] == 0) {
            timePixels[i] = timeChange.length-1;
          }else{
            var changeTime = timePixels[i];
            var prevTime = timeChange[changeTime];
            var endTime = timeChange[timeChange.length-1];
            var timeDiff = endTime - prevTime;
            timeDiff /= 1000;
            if (timeDiff >= .75) {
              over = true;
              i = i + pixels.length;
            }
          }
        }
      }
    }




  }

}
