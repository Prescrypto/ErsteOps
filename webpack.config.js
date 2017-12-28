const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,

  entry: {
    dashboard: './frontend/pages/dashboard',
    modal: ['./frontend/utils/global', './frontend/components/modal'],
    nav: ['./frontend/utils/global', './frontend/components/nav'],
  },

  output: {
    path: path.resolve(__dirname, './ersteops/static/bundles'),
    filename: '[name]-[hash].js',
  },

  plugins: [
    new webpack.optimize.CommonsChunkPlugin({
      name: 'common',
      filename: 'common.js',
    }),
    new BundleTracker({ filename: 'ersteops/static/webpack-stats.json' }),
  ],

  module: {
    loaders: [
      {
        test: /\.js?$/,
        exclude: [/node_modules/, /ersteops/],
        loader: 'babel-loader',
      },
    ],
  },

  resolve: {
    extensions: ['.js', '.json'],
    alias: {
      vue$: 'vue/dist/vue.esm.js',
      utils: path.resolve(__dirname, './frontend/utils/'),
      filters: path.resolve(__dirname, './frontend/filters/'),
      pages: path.resolve(__dirname, './frontend/pages/'),
      components: path.resolve(__dirname, './frontend/components/'),
    },
  },

  watchOptions: {
    poll: true,
  },
};

if (process.env.NODE_ENV === 'production') {
  // http://vue-loader.vuejs.org/en/workflow/production.html
  module.exports.plugins = (module.exports.plugins || []).concat([
    new webpack.DefinePlugin({
      'process.env': {
        NODE_ENV: JSON.stringify('production'),
      },
    }),
    new webpack.optimize.UglifyJsPlugin({
      sourceMap: true,
      compress: {
        warnings: false,
      },
    }),
    new webpack.LoaderOptionsPlugin({
      minimize: true,
    }),
  ]);
}
