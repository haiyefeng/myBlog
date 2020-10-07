/**
 * @file event bus
 * @author 黄晓强[Fortune] <fortune@canway.net>
 */

import Vue from 'vue'

// Use a bus for components communication,
// see https://vuejs.org/v2/guide/components.html#Non-Parent-Child-Communication
export const bus = new Vue()
