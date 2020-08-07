const path = require("path");
const webpack = require('webpack');
const BundleTracker = require('webpack-bundle-tracker')
const HtmlWebpackPlugin = require('html-webpack-plugin');


module.exports = {
    context: __dirname,

    entry: './static/js/index',
    output: {
        path:
        path.resolve('./static/bundles'),
        filename:"[name]-[hash].js",
    },
    devtool:'inline-source-map',
    plugins:[
        new BundleTracker({filename:
        './webpack-stats.json'}),
    ],
    module:{
        rules:[
            {
                test:/\.js$/,
                exclude:/node_modules/,
                use:['babel-loader']
            },
            {
                test:/\.css$/,
                use: [
                    {
                        loader: 'style-loader'
                    },
                    {
                        loader: 'css-loader',
                        options:{
                            module:true,
                            localsConvention:'camelCase',
                            sourceMap: true
                        }
                    }
                ]
            }

        ]
    },
    resolve:{
        extensions:['*','.js','.jsx']
    }
};