class Population {
    constructor(lifeSpan, popSize, reward, punishment, newPopulation) {
        this.lifeSpan = lifeSpan;
        this.popSize = popSize;
        this.reward = reward;
        this.punishment = punishment;

        this.food = new Food(width / 2, 50, 30);
        this.wall = new Wall(width / 2, height - height / 3, 300, 30);

        this.flies = [];
        this.pool = [];

        if (newPopulation === undefined) {
            for (let i = 0; i < this.popSize; i++) {
                this.flies[i] = new Fly(this.lifeSpan, this.reward, this.punishment, this.food);
            }
        } else {
            this.flies = newPopulation;
        }
    }

    run(count){
        this.food.show();
        this.wall.show();
        for(let i = 0; i < this.popSize; i++){
            this.flies[i].update(count, this.wall);
            this.flies[i].show();
        }
    }
}