<template>
  <div class="ec-container">
    <div class="top-container">
      <div class="text-caption font-weight-regular top-box">
        <div class="top-text">
          <p>InnerVue’s Promise</p>
          <span>We are 100% sure that you'll be satisfied with the quality of InnerVue sports Yoga Wheel. But in any case, if you have any issues with your yoga wheel, let us know, we will refund you in full or send you a new one.</span>
        </div>
        <div class="top-inner-container d-none d-md-flex">
          <div class="box top-left">
            <span>Shop</span>
            <ul class="item-list">
              <li>Yoga Wheel - Origin Series</li>
              <li>Yoga Wheel - Passion Series</li>
            </ul>
          </div>
          <div class="box top-middle">
            <span>InnerVue’s Promise</span>
            <ul class="item-list">
              <li>Yoga Wheel - Origin Series</li>
              <li>Yoga Wheel - Passion Series</li>
            </ul>
          </div>
          <div class="box top-middle">
            <span>Shop</span>
            <ul class="item-list">
              <li>Yoga Wheel - Origin Series</li>
              <li>Yoga Wheel - Passion Series</li>
            </ul>
          </div>
          <div class="box top-right">
            <span>Contact</span>
            <ul class="item-list">
              <li>Email: innervue.sport@gmail.com</li>
              <li>Phone: 312-825-9982</li>
            </ul>
          </div>
        </div>
      </div>
    </div>
    <v-footer color="secondary">
      <div class="footer-container">
        <div class="text-caption font-weight-regular bottom-container">
          <div class="bottom-left">
            <span>Copyright © 2020 InnerVue Sports. All rights reserved.</span>
          </div>
          <div class="bottom-right">
            <span>Warranty | Legal</span>
          </div>
        </div>
      </div>
    </v-footer>
  </div>
</template>
<script>
export default {
  name: "ec-footer",
  components: {
  },
  data: () => ({
    info: "Test Text"
  }),
};
</script>

<style scoped lang="scss">
@use "../../styles/common";
.ec-container{
  .top-container {
    background-color: #faebd7;
    width: 100vw;
    .top-box{
      margin: 0 auto;
      max-width: common.$containerWidth;
      .top-text{
        //background-color: blue;
        padding: 30px;
        box-sizing: border-box;
      }
      .top-inner-container{
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        .box{
          padding: 10px;
          .item-list {
            color: #616161;
            list-style: none;
            padding: 0;
          }
        }
      }
    }
  }
  .footer-container{
    margin: 0 auto;
    width: common.$containerWidth;
    color: #616161;
    .bottom-container{
      display: flex;
      margin: 10px 0 10px 0;
      flex-direction: row;
      justify-content: space-around;
      flex-wrap: wrap;
      .bottom-left{
      }
      .bottom-right{
      }
    }
  }
}
</style>