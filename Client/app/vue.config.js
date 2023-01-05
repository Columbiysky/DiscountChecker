const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  configureWebpack: {
    devtool: 'source-map'
  }
})
// module.exports = {
//   configureWebpack: {
//     devtool: 'source-map',
//   },
// }