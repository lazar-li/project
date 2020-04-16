<template>
  <div class="index-wrapper">
    <div class="index-left">
      <!-- 全部产品 -->
      <div class="index-left-block">
        <h2>全部产品</h2>
        <template v-for="product in productList">
          <h3>{{ product.title }}</h3>
          <ul>
            <li v-for="item in product.list">
                <a v-bind:href="item.url">{{ item.title }}</a>
                <span v-if="item.hot" class="hot-tag">HOT</span>
            </li>
          </ul>
          <div v-if="!product.last" class="hr"></div>
        </template>
      </div>
      <!-- 最新消息 -->
      <div class="index-left-block lastest-news">
        <h2>最新消息</h2>
        <ul>
          <li v-for="item in newlist">
            <a v-bind:href="item.url">{{ item.title }}</a>
          </li>
        </ul>
      </div>
    </div>
    <div class="index-right">
      <slider-component></slider-component>
      <div class="index-boader-list">
        <div class="index-boader-item" v-for="item in applist">
          <div class="index-board-item-inner">
          <h2>{{item.title}}</h2>
            <p>{{item.decoration}}</p >
          <div class="index-boader-button">立即购买</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
//第一步需要引入
import axios from 'axios'
import SliderComponent from '../components/sliderComponent'
export default {
  components:{
    SliderComponent
  },
  mounted(){
    //newlist 里面的两种请求 指定结果
    axios.get('api/getNewsList')
    //请求成功下面的结果
    .then((res) =>{
      console.log(res)
      this.newlist = res.data.list
    })
    //请求失败下面的结果
    .catch((error) =>{
      console.log(error)
    })
    axios.get('api/getproductlist')
    .then((res) =>{
      console.log(res)
      this.productList = res.data
    })
    //请求失败下面的结果
    .catch((error) =>{
      console.log(error)
    });
    axios.get('api/getapplist')
    //请求成功下面的结果
    .then((res) =>{
      console.log(res)
      this.applist = res.data
    })
    //请求失败下面的结果
    .catch((error) =>{
      console.log(error)
    });
  },
  data() {
    return {
      newlist: [],
      productList: null,
      boardList:null
  }
}
};
</script>

<style scoped>
body{
  background: #f0f2f5;
  font-size: 14px;
  color: #444;
}
.index-wrapper {
  width: 1200px;
  display: flex;
}
.index-left {
  width: 300px;
}
.index-right {
  width: 900px;
  margin-top: 16px;
}
.index-left-block {
  margin: 15px;
  background: #ffffff;
  border-radius: 10px;
  box-shadow: 0 0 1px #dddddd;
}
.index-left-block .hr {
  border-bottom: 1px solid black;
  margin: 20px 0;
}
.index-left-block h2 {
  background: #4fc08d;
  color: #ffffff;
  padding: 10px 15px;
  margin-bottom: 20px;
}
.index-left-block h3 {
  color: #222;
  font-weight: bolder;
  padding: 0 15px 5px 15px;
}
.index-left-block ul {
  padding: 10px 15px;
}
.index-left-block li {
  padding: 5px;
}
.index-boader-list {
  display: flex;
  flex-wrap: wrap;
  justify-content:space-between;
  margin-top: 15px;
}
.index-boader-item {
  width: 400px;
  background:whitesmoke;
  box-shadow: 0 0 1px #ddd;
  border-radius: 0 0 10px 10px;
  margin-bottom: 20px;
} 
.index-board-item-inner{
  height: 125px;
  padding-left: 180px;
  background-image: url(../assets/logo.png);
  background-repeat: no-repeat;
  background-size: 30%;
}

.index-board-item-inner h2{
  font-size: 18px;
  font-weight: bolder;
  color: #000;
  margin-bottom: 15px;
}
.index-board-item-inner p{
  margin-bottom: 15px;
}
.index-boader-button{
  width: 80px;
  height: 40px;
  background: rgb(1,77,1);
  color: #ffffff;
  border-radius: 5px;
  text-align: center;
  line-height: 40px;
}
.hot-tag{
  color:#ffffff;
  background: purple;
  font-size:12px;
}
</style>