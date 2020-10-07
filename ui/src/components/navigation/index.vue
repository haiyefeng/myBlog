<template>
    <div class="monitor-navigation">
        <bk-navigation
            :header-title="nav.id"
            :side-title="nav.title"
            :default-open="false"
            :navigation-type="curNav.nav"
            :need-menu="curNav.needMenu"
            @toggle="handleToggle">
            <template slot="header">
                <div class="monitor-navigation-header">
                    <bk-popover theme="light navigation-message" :arrow="false" offset="-150, 5" trigger="mouseenter" :tippy-options="{ 'hideOnClick': false }">
                        <div class="header-mind" :class="{ 'is-left': curNav.nav === 'left-right' }">
                            <svg style="width: 1em; height: 1em;vertical-align: middle;fill: currentColor;overflow: hidden;" viewBox="0 0 64 64" version="1.1" xmlns="http://www.w3.org/2000/svg">
                                <path d="M32,56c-1.3,0-2.6-0.6-3.4-1.6h-4.5c0.5,1.5,1.4,2.7,2.6,3.7c3.1,2.5,7.5,2.5,10.6,0c1.2-1,2.1-2.3,2.6-3.7h-4.5C34.6,55.4,33.3,56,32,56z"></path>
                                <path d="M53.8,49.1L50,41.5V28c0-8.4-5.8-15.7-14-17.6V8c0-2.2-1.8-4-4-4s-4,1.8-4,4v2.4c-8.2,1.9-14,9.2-14,17.6v13.5l-3.8,7.6c-0.3,0.6-0.3,1.3,0.1,1.9c0.4,0.6,1,1,1.7,1h40c0.7,0,1.3-0.4,1.7-1C54,50.4,54.1,49.7,53.8,49.1z"></path>
                            </svg>
                            <span class="header-mind-mark" :class="{ 'is-left': curNav.nav === 'left-right' }"></span>
                        </div>
                        <template slot="content">
                            <div class="monitor-navigation-message">
                                <h5 class="message-title">消息中心</h5>
                                <ul class="message-list">
                                    <li class="message-list-item" v-for="(item,index) in message.list" :key="index">
                                        <span class="item-message">{{item.message}}</span>
                                        <span class="item-date">{{item.date}}</span>
                                    </li>
                                </ul>
                                <div class="message-footer">进入消息中心</div>
                            </div>
                        </template>
                    </bk-popover>
                    <div class="header-help" :class="{ 'is-left': curNav.nav === 'left-right' }">
                        <svg class="bk-icon" style="width: 1em; height: 1em;vertical-align: middle;fill: currentColor;overflow: hidden;" viewBox="0 0 64 64" version="1.1" xmlns="http://www.w3.org/2000/svg">
                            <path d="M32,4C16.5,4,4,16.5,4,32c0,3.6,0.7,7.1,2,10.4V56c0,1.1,0.9,2,2,2h13.6C36,63.7,52.3,56.8,58,42.4S56.8,11.7,42.4,6C39.1,4.7,35.6,4,32,4z M31.3,45.1c-1.7,0-3-1.3-3-3s1.3-3,3-3c1.7,0,3,1.3,3,3S33,45.1,31.3,45.1z M36.7,31.7c-2.3,1.3-3,2.2-3,3.9v0.9H29v-1c-0.2-2.8,0.7-4.4,3.2-5.8c2.3-1.4,3-2.2,3-3.8s-1.3-2.8-3.3-2.8c-1.8-0.1-3.3,1.2-3.5,3c0,0.1,0,0.1,0,0.2h-4.8c0.1-4.4,3.1-7.4,8.5-7.4c5,0,8.3,2.8,8.3,6.9C40.5,28.4,39.2,30.3,36.7,31.7z"></path>
                        </svg>
                    </div>
                    <bk-popover theme="light navigation-message" :arrow="false" offset="-20, 10" placement="bottom-start" :tippy-options="{ 'hideOnClick': false }">
                        <div class="header-user" :class="{ 'is-left': curNav.nav === 'left-right' }">
                            Admin
                            <i class="bk-icon icon-down-shape"></i>
                        </div>
                        <template slot="content">
                            <ul class="monitor-navigation-admin">
                                <li class="nav-item" v-for="userItem in user.list" :key="userItem">
                                    {{userItem}}
                                </li>
                            </ul>
                        </template>
                    </bk-popover>
                </div>
            </template>
            <template slot="menu">
                <bk-navigation-menu
                    ref="menu"
                    @select="handleSelect"
                    :default-active="nav.id"
                    :before-nav-change="beforeNavChange"
                    :toggle-active="nav.toggle">
                    <bk-navigation-menu-item
                        v-for="item in nav.list"
                        :key="item.name"
                        :has-child="item.children && !!item.children.length"
                        :group="item.group"
                        :icon="item.icon"
                        :disabled="item.disabled"
                        :url="item.url"
                        :id="item.name">
                        <span>{{item.name}}</span>
                        <div slot="child">
                            <bk-navigation-menu-item
                                :key="child.name"
                                v-for="child in item.children"
                                :id="child.name"
                                :disabled="child.disabled"
                                :icon="child.icon"
                                :url="child.url"
                                :default-active="child.active">
                                <span>{{child.name}}</span>
                            </bk-navigation-menu-item>
                        </div>
                    </bk-navigation-menu-item>
                </bk-navigation-menu>
            </template>
            <div class="monitor-navigation-content">
                <main class="main-content" v-bkloading="{ isLoading: mainContentLoading, opacity: 1 }">
                    <router-view :key="routerKey" v-show="!mainContentLoading" />
                </main>
            </div>
            <template slot="footer">
                <div class="monitor-navigation-footer">
                    Copyright © 2012-2020 Tencent BlueKing. All Rights Reserved. 腾讯蓝鲸 版权所有
                </div>
            </template>
        </bk-navigation>
    </div>
</template>

<script>
    import { mapGetters } from 'vuex'

    export default {
        name: 'monitor-navigation',
        data () {
            return {
                navActive: 1,
                navMap: [
                    {
                        nav: 'left-right',
                        needMenu: true,
                        name: '左右结构导航'
                    },
                    {
                        nav: 'top-bottom',
                        needMenu: true,
                        name: '上下结构导航'
                    },
                    {
                        nav: 'top-bottom',
                        needMenu: false,
                        name: '上下结构无侧栏导航'
                    }
                ],
                nav: {
                    list: [
                        {
                            name: '首页',
                            icon: 'icon-tree-application-shape',
                            url: '/home/'
                        }
                        // {
                        //     name: '健康画像',
                        //     icon: 'icon-tree-group-shape',
                        //     open: true,
                        //     children: [
                        //         {
                        //             name: '系统画像',
                        //             url: '/system_portrait/'
                        //         },
                        //         {
                        //             name: '服务器画像',
                        //             url: '/server_portrait/'
                        //         }
                        //     ]
                        // },
                        // {
                        //     name: '应用系统管理',
                        //     icon: 'icon-tree-process-shape',
                        //     url: '/application_management/'
                        // },
                        // {
                        //     name: '健康维度',
                        //     icon: 'icon-tree-group-shape',
                        //     open: true,
                        //     children: [
                        //         {
                        //             name: '指标列表',
                        //             url: '/metric_management/'
                        //         },
                        //         {
                        //             name: '维度列表',
                        //             url: '/dimension_management/'
                        //         },
                        //         {
                        //             name: '评分规则',
                        //             url: '/rule_management/'
                        //         }
                        //     ]
                        // }
                    ],
                    id: '首页',
                    toggle: false,
                    submenuActive: false,
                    title: '系统健康画像'
                },
                message: {
                    list: [
                        {
                            message: '你的“20181212112308”单据已通过',
                            date: '刚刚'
                        }
                    ]
                },
                user: {
                    list: [
                        '项目管理',
                        '权限中心',
                        '退出'
                    ]
                },
                routerKey: +new Date()
            }
        },
        computed: {
            ...mapGetters(['mainContentLoading']),
            curNav () {
                return this.navMap[this.navActive]
            }
        },
        beforeUpdate () {
            this.initNav()
        },
        methods: {
            initNav () {
                switch (this.$router.currentRoute.name) {
                    case 'home':
                        this.nav.id = '首页'
                        break
                    case 'system_portrait':
                        this.nav.id = '系统画像'
                        break
                    case 'server_portrait':
                        this.nav.id = '服务器画像'
                        break
                    case 'application_management':
                        this.nav.id = '应用系统管理'
                        break
                    case 'metric_management':
                        this.nav.id = '指标列表'
                        break
                    case 'dimension_management':
                        this.nav.id = '维度列表'
                        break
                    case 'rule_management':
                        this.nav.id = '评分规则'
                        break
                    default:
                        this.nav.id = '首页'
                }
            },
            handleSelect (id, item) {
                this.nav.id = id
                this.$router.push({
                    path: item.url
                })
            },
            handleToggle (v) {
                this.nav.toggle = v
            },
            beforeNavChange (newId, oldId) {
                return true
            },
            handleChangeNav () {
                this.navActive = (this.navActive + 1) % 3
            },
            /**
             * router 跳转
             *
             * @param {string} idx 页面指示
             */
            goPage (idx) {
                this.$router.push({
                    name: idx
                })
            }
        }
    }
</script>

<style>
    @import './index.scss'
</style>
