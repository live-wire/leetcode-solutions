// Run with ts-node
// $ ts-node 130/solution.ts

const input = [
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'O', 'X'],
    ['X', 'X', 'O', 'X'],
    ['X', 'O', 'X', 'X'],
];

const output = [
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'X', 'X', 'X'],
    ['X', 'O', 'X', 'X'],
];

class Neighbour {
    public row: number;
    public column: number;

    constructor(row: number, column: number) {
        this.row = row;
        this.column = column;
    }
}

function solve(board: string[][]): void {
    const rows = board.length;
    if (rows <= 2) {
        return;
    }

    const columns = board[0].length;
    if (columns <= 2) {
        return;
    }

    const isValidPosition = (row: number, column: number): boolean => {
        if (row < 0 || row > rows - 1) {
            return false;
        }
        if (column < 0 || column > columns - 1) {
            return false;
        }
        return true;
    }

    const getNeighbours = (row: number, column: number): Neighbour[] => {
        const result: Neighbour[] = [];
        const upperNeighbour = new Neighbour(row - 1, column);
        if (isValidPosition(upperNeighbour.row, upperNeighbour.column)) {
            result.push(upperNeighbour);
        }

        const rightNeighbour = new Neighbour(row, column + 1);
        if (isValidPosition(rightNeighbour.row, rightNeighbour.column)) {
            result.push(rightNeighbour);
        }

        const bottomNeighbour = new Neighbour(row + 1, column);
        if (isValidPosition(bottomNeighbour.row, bottomNeighbour.column)) {
            result.push(bottomNeighbour);
        }

        const leftNeighbour = new Neighbour(row, column - 1);
        if (isValidPosition(leftNeighbour.row, leftNeighbour.column)) {
            result.push(leftNeighbour);
        }

        return result;
    }

    const markSafe = (row: number, column: number): void => {
        board[row][column] = '1';
        const neighbours = getNeighbours(row, column);
        for (let i = 0; i < neighbours.length; i++) {
            const neighbour = neighbours[i];
            if (board[neighbour.row][neighbour.column] === 'O') {
                markSafe(neighbour.row, neighbour.column);
            }
        }
    }

    for (let i = 0; i < rows; i++) {

        if (board[i][0] === 'O') {
            markSafe(i, 0);
        }
        if (board[i][columns - 1] === 'O') {
            markSafe(i, columns - 1);
        }
    }

    for (let i = 0; i < columns; i++) {
        if (board[0][i] === 'O') {
            markSafe(0, i);
        }
        if (board[rows - 1][i] === 'O') {
            markSafe(rows - 1, i);
        }
    }

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < columns; j++) {
            if (board[i][j] === 'O') {
                board[i][j] = 'X';
            }
            if (board[i][j] === '1') {
                board[i][j] = 'O';
            }
        }
    }
};

solve(input);

let isCorrect = true;
for (let i = 0; i < input.length; i++) {
    for (let j = 0; j < input[i].length; j++) {
        if (input[i][j] !== output[i][j]) {
            isCorrect = false;
            break;
        }
    }
    if (!isCorrect) {
        break;
    }
}

if (isCorrect) {
    console.log('Correct');
} else {
    console.log('Wrong');
    console.log('Result:', input);
}
