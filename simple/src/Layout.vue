<template>
  <div id="app">
    <div class="app-head">
      <div class="app-head-inner">
        <img src="./assets/logo.png" alt=""><span class="app-title">3c产品商城</span>
        <div class="head-nav">
          <ul class="nav-list">
            <li v-on:click="showLogin">登录</li>
            <li class="nav-pile">|</li>
            <li>注册</li>
            <li class="nav-pile">|</li>
            <li>关于</li>
          </ul>
        </div>
      </div>
    </div>
    <div class="app-content">
      <router-view></router-view>
    </div>
    <div class="app-footer">
    <p>&copy;1903c - 2020</p>
    </div>
    <my-login v-show="isShowLogin"></my-login>
  </div>
</template>

<script>
import MyLogin from './components/myLogin'
export default {
  components:{
    MyLogin
  },
  data() {
    return {
      isShowLogin:false
    }
  },
  methods: {
    showLogin(){
      this.isShowLogin = true
    }
  },
}
</script>
<!---->
//全局样式<style></style>,非全局样式<style scoped></style>
<style>

  /* reset样式 */
  html, body, div, span, applet, object, iframe,
  h1, h2, h3, h4, h5, h6, p, blockquote, pre,
  a, abbr, acronym, address, big, cite, code,
  del, dfn, em, img, ins, kbd, q, s, samp,
  small, strike, strong, sub, sup, tt, var,
  b, u, i, center,
  dl, dt, dd, ol, ul, li,
  fieldset, form, label, legend,
  table, caption, tbody, tfoot, thead, tr, th, td,
  article, aside, canvas, details, embed, 
  figure, figcaption, footer, header, hgroup, 
  menu, nav, output, ruby, section, summary,
  time, mark, audio, video {
    margin: 0;
    padding: 0;
    border: 0;
    font-size: 100%;
    font: inherit;
    vertical-align: baseline;
  }
  .app-title{
    color: #ffffff;
    font-size: 30px;
    font-weight: bolder;
    margin-left: 30px;
  }
  /* HTML5 display-role reset for older browsers */
  article, aside, details, figcaption, figure, 
  footer, header, hgroup, menu, nav, section {
    display: block;
  }
  body {
    line-height: 1;
  }
  ol, ul {
    list-style: none;
  }
  blockquote, q {
    quotes: none;
  }
  blockquote:before, blockquote:after,
  q:before, q:after {
    content: '';
    content: none;
  }
  table {
    border-collapse: collapse;
    border-spacing: 0;
  }
  /*自己写的style样式*/
  .app-head{
    background: #363636;
    color:#b2b2b2;
    height: 90px;
    line-height: 90px;
    width:100% ;
  }
  .app-head-inner{
    width: 1200px;
    margin: 0 auto;
  }
  .app-head-inner img{
    float: left;
    width: 50px;
    margin-top: 20px;
  }
  .head-nav{
    float: right;
  }
  .head-nav li{
    float:left;
    cursor:pointer;
  }
  .nav-pile{
    padding: 0 10px;
  }
  .app-footer{
    text-align: center;
    height: 80px;
    line-height: 80px;
    width: 100%;
    background: #262626;
    margin-top: 20px;
  }
  .app-content{
    width: 1200px;
    margin: 0 0 0 200px;
    
  }
</style>
