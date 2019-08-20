const LIFE_SPAN = 600; // How long do flies live
const POP_SIZE = 500; // How many flies do we want
const REWARD_MULT = 10; // What is the reward for finding food
const PUNISH_DIV = 3; // What is the punishment for hitting something
const MUTATION_RATE = 0.1; // What is the rate at which flies mutate

let count = 0;

let fly, food, wall;

function setup() {
    console.log('Hello');

    createCanvas(640, 480);

    fly = new Fly(LIFE_SPAN);
    food = new Food(width/2, 50, 30);
    wall = new Wall(width/2, height - height/3, 300, 30);
}

function draw() {
    background(3, 161, 252);
    
    fly.update(count);
    fly.show();

    food.show();
    wall.show();
    
    count++;

    if (count == LIFE_SPAN) {
        count = 0;
    }
}