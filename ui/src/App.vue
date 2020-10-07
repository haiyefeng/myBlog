<template>
    <div id="app" :class="systemCls">
        <navigation></navigation>
    </div>
</template>
<script>
    import Navigation from '@/components/navigation'
    // import { bus } from '@/common/bus'

    export default {
        name: 'app',
        components: {
            Navigation
        },
        data () {
            return {
                systemCls: 'mac'
            }
        },
        computed: {},
        watch: {
        },
        created () {
            const platform = window.navigator.platform.toLowerCase()
            if (platform.indexOf('win') === 0) {
                this.systemCls = 'win'
            }
        },
        mounted () {
            // const self = this
            // bus.$on('show-login-modal', data => {
            //     self.$refs.bkAuth.showLoginModal(data)
            // })
            // bus.$on('close-login-modal', () => {
            //     self.$refs.bkAuth.hideLoginModal()
            //     setTimeout(() => {
            //         window.location.reload()
            //     }, 0)
            // })
        },
        methods: {
        }
    }
</script>

<style lang="postcss">
    @import './css/reset.css';
    @import './css/app.css';

    #app {
        font-size: 14px;
        color: #737987;
    }
    .header {
        margin-bottom: 20px;
        li {
            margin: 0 10px 0 0;
        }
    }
    .main-content {
        padding: 5px 15px 15px 15px;
    }
    h1,
    h2 {
        font-weight: normal;
    }
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        display: inline-block;
        margin: 0 10px;
    }
    a {
        color: #737987;
    }
    .split {
        margin-bottom: 15px;
    }
    .iModue-container .iModule-target .bk-collapse-item-header {
        background: #fafbfd;
        border: 1px solid #dcdee6;
    }
    .iModue-container .iModule-source li {
        margin: 0;
    }
    .iModue-container .iModule-source .bk-tab-label-list {
        width: 100%;
    }
    .iModue-container .iModule-source .bk-tab-label-item {
        width: 50%;
    }
    .iModue-container .iModule-source .bk-tab .bk-tab-section {
        padding: 0;
    }
    .dialog-btn {
        .bk-button.bk-primary {
            margin-left: 10px;
            float: right;

        }
    }
</style>
