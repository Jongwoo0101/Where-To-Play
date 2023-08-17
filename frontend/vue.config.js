const fs = require('fs')

module.exports = {
    devServer: {
        https: true,
        allowedHosts: 'all',
        devMiddleware: {
            publicPath: ''
        },
    }
}