// Run with ts-node
// $ ts-node 1578/solution.ts

const inputString = 'bbbaaa';
const inputCost = [4, 9, 3, 8, 8, 9];

function minCost(s: string, cost: number[]): number {
    let minCost = 0;
    for (let i = 0; i < s.length; i++) {
        const subCostArray: number[] = [];
        let currentMax = -Number.MAX_VALUE;
        let removalSum = 0;
        let cursor = i + 1;

        while (s[i] === s[cursor] && cursor < s.length) {
            const removalCost = cost[cursor];
            subCostArray.push(removalCost);
            removalSum += removalCost;
            if (removalCost > currentMax) {
                currentMax = removalCost;
            }
            cursor += 1;
        }

        subCostArray.push(cost[i]);
        removalSum += cost[i];
        if (cost[i] > currentMax) {
            currentMax = cost[i];
        }

        if (subCostArray.length > 1) {
            minCost += (removalSum - currentMax);
            i = cursor - 1;
        }
    }

    return minCost;
};

console.log(minCost(inputString, inputCost));
