//새로 추가할 plugin은 plugins에 추가해서 사용!
// @babel/plugin-transform-runtime 를 사용하여 상시 babel로 번역해준다!
module.exports = {
  presets: ["@babel/preset-env"],
  plugins: [["@babel/plugin-transform-runtime"]],
};
