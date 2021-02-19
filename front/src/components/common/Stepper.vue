// created by Sean Li on Oct 31, 2020
<template>
  <div class="ec-container">
    <span class="substract-icon stepper-icon" @click.stop="substractClick"></span>
    <input type="number" class="count-input" v-model="count">
    <span class="add-icon stepper-icon" @click.stop="addClick"></span>
  </div>
</template>
<script>
export default {
  name: "ec-stepper",
  components: {
  },
  data: () => ({
    count: 1
  }),
  methods: {
    substractClick(){
      let value = parseInt(this.count)
      if(value > 0){
        this.count = value - 1
      }
    },
    addClick(){
      let value = parseInt(this.count)
      this.count = value + 1
    },
  }
};
</script>
<style scoped lang="scss">
.ec-container{
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  .stepper-icon{
    display: inline-block;
    width: 25px;
    height: 25px;
    border-radius: 50%;
    background-size: 100%;
    cursor: pointer;
  }
  .substract-icon{
    background-image: url("../../assets/icons/stepper-substract-icon.png");
    margin-right:10px;
  }
  .add-icon{
    background-image: url("../../assets/icons/stepper-add-icon.jpg");
    margin-left:10px;
  }
  .count-input{
    width: 40px;
    text-align: center;
    //hide spin arrow for firefox
    -moz-appearance: textfield;
    //hide spin arrow for other browsers
    &::-webkit-outer-spin-button,
    &::-webkit-inner-spin-button {
      -webkit-appearance: none;
      margin: 0;
    }
  }
}
</style>