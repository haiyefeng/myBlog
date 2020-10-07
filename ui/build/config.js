/**
 * @file config
 * @author 黄晓强[Fortune] <fortune@canway.net>
 */

import path from 'path'
import prodEnv from './prod.env'
import devEnv from './dev.env'

export default {
    build: {
        // env 会通过 webpack.DefinePlugin 注入到前端代码里
        env: prodEnv,
        assetsRoot: path.resolve(__dirname, '../../static'),
        assetsSubDirectory: 'assets',
        assetsPublicPath: '{{BK_STATIC_URL}}',
        productionSourceMap: true,
        productionGzip: false,
        productionGzipExtensions: ['js', 'css'],
        bundleAnalyzerReport: process.env.npm_config_report
    },
    dev: {
        // env 会通过 webpack.DefinePlugin 注入到前端代码里
        env: devEnv,
        // 这里用 JSON.parse 是因为 dev.env.js 里有一次 JSON.stringify，dev.env.js 里的 JSON.stringify 不能去掉
        localDevUrl: JSON.parse(devEnv.LOCAL_DEV_URL),
        localDevPort: JSON.parse(devEnv.LOCAL_DEV_PORT),
        assetsSubDirectory: 'static',
        assetsPublicPath: '/',
        proxyTable: {
            '/api/': {
                // 自定义部分：后端项目url
                target: 'http://127.0.0.1:8000',
                changeOrigin: true
              }
        },
        cssSourceMap: false,
        autoOpenBrowser: false
    }
}
