/** @type {import('jest').Config} */
module.exports = {
  roots: ['tests'],
  transform: {
    "\\.[jt]sx?$": "babel-jest",
  }
};
