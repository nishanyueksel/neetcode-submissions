class Solution {
    /**
     * @param {number[]} piles
     * @param {number} h
     * @return {number}
     */
    minEatingSpeed(piles, h) {
        let speed = 1;
        while (true) {
            let totalTime = 0;
            for (let p of piles) {
                totalTime = totalTime + Math.ceil(p / speed);
            }
            if (totalTime <= h) {
                return speed;
            }
            speed++;
        }
    }
}
