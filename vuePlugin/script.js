
import Vue from 'vue/dist/vue.js'
import VueMathPlugin from './VueMathPlugin.js'
import Vuex from 'vuex'


Vue.use(VueMathPlugin)
Vue.use(Vuex)

var store = new Vuex.store({
    state:{message:'hello'},
    mutations:{},
    actions:{},
    getters:{},
})



new Vue({
    el:'#app',
    data:{
        item:90
    },
    store:store
})
