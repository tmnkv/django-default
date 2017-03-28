const path = require('path');
const webpack = require("webpack");
const ExtractTextPlugin = require('extract-text-webpack-plugin');

module.exports = {
    context: path.resolve(__dirname, 'static/src'),
    entry: {
        index: './index.js',
    },
    output: {
        path: path.resolve(__dirname, 'static/build'),
        filename: 'js/[name].bundle.js',
        publicPath: '/static/',
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: [{loader: "babel-loader",
                    options: { presets: ['es2015'] }
                }],

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
        new webpack.optimize.CommonsChunkPlugin({
            name: 'commons',
            filename: 'js/common.js',
            minChunks: 2,
        }),
        new ExtractTextPlugin({
            filename: 'css/styles.css',
            allChunks: true,
        }),
        new webpack.ProvidePlugin({
            $: "jquery",
            jQuery: "jquery",
            "window.jQuery": "jquery"
        }),
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