<template>
    <div class="slider-wrapper" @mouseover="clearInv" @mouseout="runInv">
        <!--四张轮播图-->
        <div class="slider-item item1">1</div>
        <div class="slider-item item2">2</div>
        <div class="slider-item item3">3</div>
        <div class="slider-item item4">4</div>


        <!--下方的四个小点-->
        <ul class="slider-dots">
            <li>&lt;</li>
            <li>1</li>
            <li>2</li>
            <li>3</li>
            <li>4</li>
            <li>&gt;</li>
        </ul>
    </div>
</template>



<script>
export default {
    props:{
        //inv  是定时器
        inv:{
            type:Number,
            default:1000,
        }
    },
    data(){
        return{

        }
    },
    methods:{
        runInv(){
            setInterval(()=>{},this.inv)

        },
        clearInv(){

        }
    }
}
</script>


<style scoped>
    .slider-wrapper{
        width: 900px;
        height: 300px;
        background: blue;
        position: relative;
    }
    .slider-item{
        width: 900px;
        height: 300px;
        text-align: center;
        line-height: 300px;
        font-size: 40px;
        position: absolute;
    }
    .item1{
        z-index:100;
    }
    .item2{
        z-index:99;
    }
    .item3{
        z-index:98;
    }
    .item4{
        z-index:97;
    }
    .slider-dots{
        position: absolute;
        right:20px;
        bottom: 20px;
    }
    .slider-dots li{
        width: 20px;
        height: 20px;
        border-radius: 50%;
        background: chocolate;
        text-align: center;
        line-height: 20px;
        float: left;
        margin: 0 10px;
        opacity: 0.6;
        color:#ffffff;
    }



</style>