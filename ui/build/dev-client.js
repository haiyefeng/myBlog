/**
 * @file for hot-reload
 * @author 黄晓强[Fortune] <fortune@canway.net>
 */

/* eslint-disable */
import 'eventsource-polyfill'
import hotClient from 'webpack-hot-middleware/client?noInfo=true&reload=true'

hotClient.subscribe(event => {
    if (event.action === 'reload') {
        window.location.reload()
    }
})
