// 사용할 postcssrc 지정해주기.
//최초 1회에는 autoprefixer이 없기 때문에 설치해준다.
// npm i -d autoprefixer@9
const autoprefixer = require("autoprefixer");

module.exports = {
  plugins: [autoprefixer],
};
