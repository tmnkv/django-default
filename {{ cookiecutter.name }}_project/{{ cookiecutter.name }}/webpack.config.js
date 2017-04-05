const path = require('path');
const webpack = require("webpack");
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const BrowserSyncPlugin = require('browser-sync-webpack-plugin');
const styleLintPlugin = require('stylelint-webpack-plugin');

module.exports = {
    context: path.resolve(__dirname, 'static/src'),
    entry: {
        main: './main.js',
    },
    output: {
        path: path.resolve(__dirname, 'static/build'),
        filename: 'js/[name].js',
        publicPath: '/static/',
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: [
                    "babel-loader",
                    "eslint-loader",
                ],
            },
            {
                test: /\.scss$/,
                use: ExtractTextPlugin.extract({
                    fallback: 'style-loader',
                    //resolve-url-loader may be chained before sass-loader if necessary
                    use: [
                        'css-loader',
                        {
                            loader: 'postcss-loader',
                            options: {
                                plugins: function () {
                                    return [
                                        require('autoprefixer')
                                    ];
                                }
                            }
                        },
                        'sass-loader'
                    ]
                })
            },
            {
                test: /(\.jpg|\.png|\.ico|.gif|\.tif|\.svg)\??.*$/,
                use: 'url-loader?limit=30000&name=images/[name].[ext]?v=[hash]'
            },
            {
                test: /\.(woff|woff2|eot|ttf)$/,
                loader: 'file-loader?name=fonts/[name].[ext]?v=[hash]'
            },
        ]
    },
    plugins: [
        new ExtractTextPlugin({
            filename: 'css/styles.css',
            allChunks: true,
        }),
        new styleLintPlugin({
            configFile: 'stylelint.',
            context: path.resolve(__dirname, 'static/src'),
            files: '**/*.scss',
            failOnError: false,
            quiet: false,
        }),
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery",
            "window.jQuery": "jquery"
        }),
        new BrowserSyncPlugin({
            host: 'localhost',
            port: 8000,
            proxy: 'http://localhost:8000/',
            open: false,
        }),

        // uncomment following plugin if you are going to make few entry points on your website
        // it will separate modules required in few entry points in one file for use on every page

        // new webpack.optimize.CommonsChunkPlugin({
        //     name: 'commons',
        //     filename: 'js/common.js',
        //     minChunks: 2,
        // }),
    ],
    devServer: {
        proxy: {
            "*": {
                target: "http://localhost:8000",
                changeOrigin: true,
                secure: false,
            }
        }
    }
};
