//写出这句话才能暴露出去

export default{
    //在调用install 需要调用Vue
    install:function(Vue){
    //自定义指令   square  用的话指令需要是v-square
    // Vue.directive('square', function (el, binding) {
    //     el.innerHTML = Math.pow(binding.value,2)
    //     });
    // Vue.directive('sqrt',function(el,binding){
    //     el.innerHTML = Math.sqrt(binding.value)
    // });
    Vue.directive('sin',function(el,binding){
        el.innerHTML = Math.sin(Math.PI * binding.value / 180)
    });
    Vue.directive('cos',function(el,binding){
        el.innerHTML = Math.cos(Math.PI * binding.value / 180)
    });
    Vue.directive('tan',function(el,binding){
        el.innerHTML = Math.tan(Math.PI * binding.value / 180)
    });
    }
}       