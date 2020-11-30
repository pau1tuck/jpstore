const path = require("path");
module.exports = {
	entry: "./src/index",

	output: {
		path: path.join(__dirname, "/static/client"),
		filename: "index.js"
	},

	resolve: {
		extensions: [ ".ts", ".tsx", ".js" ]
	},

	module: {
		rules: [
			{
				test: /\.(ts|js)x?$/,
				exclude: /node_modules/,
				use: {
					loader: "babel-loader"
				}
			},
			{
				test: /\.s[ac]ss$/i,
				use: [
					// Creates `style` nodes from JS strings
					"style-loader",
					// Translates CSS into CommonJS
					"css-loader",
					// Compiles Sass to CSS
					"sass-loader"
				]
			}
		]
	}
};
