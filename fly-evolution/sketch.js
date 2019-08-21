const LIFE_SPAN = 600; // How long do flies live
const POP_SIZE = 500; // How many flies do we want
const REWARD_MULT = 10000; // What is the reward for finding food
const PUNISH_DIV = 3; // What is the punishment for hitting something
const MUTATION_RATE = 0.1; // What is the rate at which flies mutate

let count = 0;
let generation = 0;
let averageFit = 0;
let successRate = 0;

function setup() {

    createCanvas(640, 480);

    population = new Population(LIFE_SPAN, POP_SIZE, REWARD_MULT, PUNISH_DIV);
}

function draw() {
    background(0);

    population.run(count);

    textSize(32);
    fill(255);
    text("Generation: " + generation, 10, 35);
    text("Average Fitness: " + averageFit, 10, 75);
    text("Success Rate: " + successRate + "%", 10, 115);

    count++;

    if (count == LIFE_SPAN) {
        population.evaluate();

        averageFit = population.findAverageFitness();
        successRate = population.successRate;

        let newFlies = population.generateNewPopulation(MUTATION_RATE);

        population = new Population(LIFE_SPAN, POP_SIZE, REWARD_MULT, PUNISH_DIV, newFlies);

        count = 0;
        generation++;
    }
}