// Run with ts-node
// $ ts-node 519/solution.ts

class Solution {
    private rows: number;
    private cols: number;

    private rr: number = Math.random();
    private rc: number = Math.random();

    private flipped: number[][] = [];

    private i: number = 1_000_000;

    constructor(n_rows: number, n_cols: number) {
        this.rows = n_rows;
        this.cols = n_cols;
    }

    flip(): number[] {
        const row = Math.floor((this.rr * this.i)) % this.rows;
        const col = Math.floor((this.rc * this.i)) % this.cols;
        this.i--;

        for (let i = 0; i < this.flipped.length; i++) {
            const pair = this.flipped[i];
            if (pair[0] === row && pair[1] === col) {
                return this.flip();
            }
        }
        this.flipped.push([row, col]);
        return [row, col];
    }

    reset(): void {
        this.flipped = [];
        this.rr = Math.random();
        this.rc = Math.random();
        this.i = 1_000_000;
    }
}
