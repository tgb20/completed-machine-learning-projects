class Selection {
    constructor() { }

    getSelectionPool(lastGeneration) {

        let maxScore = 0;
        let selectionPool = [];

        for (let i = 0; i < lastGeneration.length; i++) {
            if (lastGeneration[i].score > maxScore && !lastGeneration[i].playerControlled) {
                maxScore = lastGeneration[i].score;
            }
        }

        for (let i = 0; i < lastGeneration.length; i++) {
            if (!lastGeneration[i].playerControlled) {

                let selectionCount = (lastGeneration[i].score/maxScore) * 10;

                for (let j = 0; j < selectionCount; j++) {
                    selectionPool.push(lastGeneration[i]);
                }
            }
        }

        return selectionPool;
    }

    createNewGeneration(numDinos, lastGeneration, mutationRate) {

        let newDinos = [];

        let selectionPool = this.getSelectionPool(lastGeneration);

        for (let i = 0; i < numDinos; i++) {

            let dinoToPick = int(random(0, selectionPool.length));

            let pickedDinoBrain = selectionPool[dinoToPick].brain.copy();
            pickedDinoBrain.mutate(mutationRate);

            let newDino = new Dino(false, pickedDinoBrain);

            newDinos.push(newDino);
        }

        return newDinos;
    }
}