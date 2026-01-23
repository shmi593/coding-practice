const directions = [
  [-1, 0],
  [0, -1],
  [1, 0],
  [0, 1],
];

const findNextSpaces = (y, x, board) =>
  directions
    .map(([dy, dx]) => [y + dy, x + dx])
    .filter(([ny, nx]) => !!board[ny - 1] && board[ny - 1][nx - 1] === ".");

const main = (input) => {
  const [_, start, goal, ...board] = input
    .split("\n")
    .map((l, i) =>
      i >= 3 ? Array.from(l) : l.split(" ").map((n) => parseInt(n))
    );

  const equalsToGoal =
    ([gy, gx]) =>
    ([y, x]) =>
      y == gy && x == gx;

  const bfs = (spaces, moves) => {
    if (spaces.length == 0 || spaces.some(equalsToGoal(goal))) return moves;
    const nSpaces = spaces.flatMap(([y, x]) => {
      board[y - 1][x - 1] = "";
      return findNextSpaces(y, x, board);
    });
    return bfs(nSpaces, moves + 1);
  };

  console.log(bfs([start], 0));
};

main(require("fs").readFileSync("/dev/stdin", "utf8"));
