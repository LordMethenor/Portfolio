function setup(){
  createCanvas(600, 400);

}

function draw(){
  background("#ccc");
  fill("#000");
  strokeWeight(20);
  ellipse(100, 100, 50, 100);
  stroke("#f0fa");
  fill("#f004");
  arc(100, 300, 80, 80, 0, 30);
  fill("#0f0");
  noStroke();
  rect(170, 170, 180, 180);
  fill("#00f");
  quad(180, 180, 230, 55, 310, 310, 160, 200);
  triangle(190, 190, 240, 65, 300, 300);
  line(200, 200, 250, 75);

}
