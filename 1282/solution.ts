// Run with ts-node
// $ ts-node 1282/solution.ts

const input = [3, 3, 3, 3, 3, 1, 3];

function groupThePeople(groupSizes: number[]): number[][] {
  const groupAccumulatorMap: { [key: number]: number[] } = {};
  const groups: number[][] = [];
  for (let i = 0; i < groupSizes.length; i++) {
    const groupSize = groupSizes[i];
    if (groupAccumulatorMap[groupSize] == null) {
      groupAccumulatorMap[groupSize] = [];
    }

    groupAccumulatorMap[groupSize].push(i);

    if (groupAccumulatorMap[groupSize].length === groupSize) {
      groups.push(groupAccumulatorMap[groupSize]);
      groupAccumulatorMap[groupSize] = [];
    }
  }
  return groups;
};

console.log(groupThePeople(input));


