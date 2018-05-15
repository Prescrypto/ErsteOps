const path = require('path');
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
  context: __dirname,

  entry: {
    dashboard: ['babel-polyfill', './frontend/entry/dashboard'],
    modal: ['./frontend/utils/global', './frontend/entry/modal'],
    nav: ['./frontend/utils/global', './frontend/entry/nav'],
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
    rules: [
      // javascript
      {
        test: /\.js?$/,
        exclude: [/node_modules/, /ersteops/],
        loader: 'babel-loader',
      },
      // vue styles
      {
        test: /\.css$/,
        use: ['vue-style-loader', 'css-loader', 'postcss-loader'],
      },
      {
        test: /\.scss$/,
        exclude: [
          /node_modules/,
          path.resolve(__dirname, './frontend/styles/'),
        ],
        use: [
          'vue-style-loader',
          'css-loader',
          'postcss-loader',
          'sass-loader',
        ],
      },
      {
        test: /\.vue$/,
        loader: 'vue-loader',
        options: {},
      },
      // global styles
      {
        test: /\.scss$/,
        include: [path.resolve(__dirname, './frontend/styles/')],
        use: ['style-loader', 'css-loader', 'postcss-loader', 'sass-loader'],
      },
      // images
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file-loader',
        options: {
          name: '[name].[ext]?[hash]',
        },
      },
    ],
  },

  resolve: {
    alias: {
      vue$: 'vue/dist/vue.esm.js',
      utils: path.resolve(__dirname, './frontend/utils/'),
      filters: path.resolve(__dirname, './frontend/filters/'),
      entry: path.resolve(__dirname, './frontend/entry/'),
      components: path.resolve(__dirname, './frontend/components/'),
      store: path.resolve(__dirname, './frontend/store/'),
      styles: path.resolve(__dirname, './frontend/styles/'),
    },
    extensions: ['*', '.js', '.vue', '.json'],
  },

  performance: {
    hints: false,
  },

  devtool: '#eval-source-map',

  watchOptions: {
    poll: true,
  },
};

if (process.env.NODE_ENV === 'production') {
  module.exports.devtool = '#source-map';

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
