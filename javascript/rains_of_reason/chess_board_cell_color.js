const chessBoardCellColor = (c1, c2) => {
    const sum = s => s.charCodeAt(0)-64 + ~~s[1];
    return sum(c1)%2 === sum(c2)%2;
};