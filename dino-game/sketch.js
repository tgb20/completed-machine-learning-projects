let ground;
let selection;

const DINO_COUNT = 100;

let dinos = [];
let cacti = [];

let spawnCactusFrame;

let score = 0;
let highScore = 0;

function setup() {
    tf.setBackend('cpu');
    createCanvas(640, 480);

    ground = new Ground();

    spawnCactusFrame = int(random(40, 100));

    cacti.push(new Cactus());

    selection = new Selection();

    firstGeneration();
}

function draw() {
    background(255);

    score += 1;

    if (score > highScore) {
        highScore = score.toFixed(0)
    }

    push();
    fill(0);
    textSize(20);
    textAlign(RIGHT);
    text(score.toFixed(0), width, 30);
    text("HI " + highScore, width, 55);
    pop();

    ground.show();

    if (frameCount == spawnCactusFrame) {
        cacti.push(new Cactus());
        spawnCactusFrame += int(random(40, 100));
    }

    for (let i = 0; i < cacti.length; i++) {

        if (cacti[i].pos.x < -cacti[i].width) {
            cacti.shift(); // Shift removes the first element in a list
        }

        cacti[i].update();
        cacti[i].show();
    }

    let allDead = true;

    for (let i = 0; i < dinos.length; i++) {
        if (dinos[i].playerControlled) {
            if (keyIsDown(DOWN_ARROW)) {
                dinos[i].duck();
            } else {
                dinos[i].unDuck();
            }

            if (keyIsDown(UP_ARROW)) {
                dinos[i].jump();
            }
        }

        if (dinos[i].isAlive) {
            allDead = false;
            dinos[i].update(getClosestCactus(dinos[i]), score);
            dinos[i].show();
        }
    }

    if(allDead || score == 2000){
        nextGeneration();
    }
}

function getClosestCactus(dino) {

    let closestIndex = 0;

    while (cacti[closestIndex].pos.x + cacti[closestIndex].fullWidth / 2 < dino.pos.x - dino.width / 2) {
        closestIndex++;
    }

    return cacti[closestIndex];
}

function firstGeneration() {
    dinos = [];

    for (let i = 0; i < DINO_COUNT; i++) {
        dinos.push(new Dino(false, new NeuralNetwork(2, 4, 3)));
    }

    // dinos.push(new Dino(true)); // Our Player
}

function nextGeneration() {

    dinos = selection.createNewGeneration(DINO_COUNT, dinos, 0.99); // 0.99 is mutation rate

    // dinos.push(new Dino(true)); // Our Player

    spawnCactusFrame = frameCount + int(random(40, 100));
    cacti = [];
    cacti.push(new Cactus());

    score = 0;
}