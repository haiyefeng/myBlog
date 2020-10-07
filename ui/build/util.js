/**
 * @file util
 * @author 黄晓强[Fortune] <fortune@canway.net>
 */

import path from 'path'

export function resolve (dir) {
    return path.join(__dirname, '..', dir)
}

export function assetsPath (_path) {
    const assetsSubDirectory = 'assets'
    return path.posix.join(assetsSubDirectory, _path)
}
