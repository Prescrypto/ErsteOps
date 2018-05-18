const path = require('path');
const webpack = require('webpack');
const VueLoaderPlugin = require('vue-loader/lib/plugin');
const BundleTracker = require('webpack-bundle-tracker');
const UglifyJSPlugin = require('uglifyjs-webpack-plugin');

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
    new VueLoaderPlugin(),
    new BundleTracker({ filename: 'ersteops/static/webpack-stats.json' }),
  ],

  optimization: {
    splitChunks: {
      cacheGroups: {
        commons: {
          name: 'common',
          chunks: 'initial',
          minChunks: 2,
        },
      },
    },
  },

  module: {
    rules: [
      // javascript
      {
        test: /\.js?$/,
        use: 'babel-loader',
        exclude: [
          /ersteops/,
          file => /node_modules/.test(file) && !/\.vue\.js/.test(file),
        ],
      },
      // vue styles
      {
        test: /\.css$/,
        use: [
          { loader: 'vue-style-loader' },
          {
            loader: 'css-loader',
            query: {
              modules: true,
              localIdentName: '[local]_[hash:base64:8]',
            },
          },
          { loader: 'postcss-loader', query: { sourceMap: true } },
        ],
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
        use: 'vue-loader',
      },
      // global styles
      {
        test: /\.scss$/,
        use: ['style-loader', 'css-loader', 'postcss-loader', 'sass-loader'],
        include: [path.resolve(__dirname, './frontend/styles/')],
      },
      // images
      {
        test: /\.(png|jpg|gif|svg)$/,
        loader: 'file-loader',
        query: {
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
  ]);

  module.exports.optimization = {
    ...module.exports.optimization,
    minimize: true,
    minimizer: [
      new UglifyJSPlugin({
        sourceMap: true,
        uglifyOptions: {
          compress: { warnings: false },
        },
      }),
    ],
    concatenateModules: true,
  };
}
