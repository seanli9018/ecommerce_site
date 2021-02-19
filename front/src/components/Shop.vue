// created by Sean on Oct. 16 2020
<template>
  <div class="ec-container">
    <div class="yoga-pattern-container">
      <img src="../../src/assets/images/yoga-pattern-reverse.png" alt="yoga-pattern" class="yoga-pattern">
    </div>
    <div class="main-container">
      <div class="product-row">
        <div class="left-container">
            <v-img src="@/assets/images/yoga-wheel-origin-series.png" :width="yogaWheelWidth"></v-img>
        </div>
        <div class="right-container">
          <div class="title">
            <h1 class = "text-h5 text-md-h4 font-weight-medium">Origin Series</h1>
            <div class="detail text-body-2 text-md-body-1">
              <ul class="gap">
                <li><strong>Material:</strong> Cork (outer circle) + ABS (inner circle)</li>
                <li><strong>Color:</strong> Cork</li>
                <li><strong>Size:</strong> 13 x 5 Inch</li>
              </ul>
              <p class="gap">Our Yoga Body Wheel is a new therapeutic tool to deepen your yoga practice and take it to the next level. It helps in muscle stretching to improve muscle flexibility, relieve back pain, and make you stronger.
                <br /><br /> Whether you’re a serious yoga enthusiast or just want to relieve back pain, our spine roller tool will allow you to stretch your back and avoid pain and discomfort.
              </p>
            </div>
          </div>
          <v-btn
            outlined
            color="accent"
            to="/product-detail"
          >
            Details
          </v-btn>
        </div>
      </div>
      <v-card class="mixin-container" flat>
        <v-img src="@/assets/images/yoga-wheel-lover.jpg"></v-img>
      </v-card>
      <div class="product-row-reverse">
        <div class="left-container">
          <v-img src="@/assets/images/yoga-wheel-pink-passion-series.png" :width="yogaWheelWidth"></v-img>
        </div>
        <div class="right-container">
          <div class="title">
            <h1 class = "text-h5 text-md-h4 font-weight-medium">Passion Series</h1>
            <div class="detail text-body-2 text-md-body-1">
              <ul class="gap">
                <li><strong>Material:</strong> PU (outer circle) + ABS (inner circle)</li>
                <li><strong>Color:</strong> Pink</li>
                <li><strong>Size:</strong> 13 x 5 Inch</li>
              </ul>
              <p class="gap">Our Yoga Body Wheel is a new therapeutic tool to deepen your yoga practice and take it to the next level. It helps in muscle stretching to improve muscle flexibility, relieve back pain, and make you stronger.
                <br /><br />Whether you’re a serious yoga enthusiast or just want to relieve back pain, our spine roller tool will allow you to stretch your back and avoid pain and discomfort.
              </p>
            </div>
          </div>
          <v-btn
            outlined
            color="accent"
          >
            Details
          </v-btn>
        </div>
      </div>
      <v-card class="mixin-container" flat>
        <v-img src="@/assets/images/yoga-wheel-lover-2.jpg"></v-img>
      </v-card>
      <div class="product-row">
        <div class="left-container">
          <v-img src="@/assets/images/yoga-wheel-blue-passion-series.png" :width="yogaWheelWidth"></v-img>
        </div>
        <div class="right-container">
          <div class="title">
            <h1 class = "text-h5 text-md-h4 font-weight-medium">Passion Series</h1>
            <div class="detail text-body-2 text-md-body-1">
              <ul class="gap">
                <li><strong>Material:</strong> Cork (outer circle) + ABS (inner circle)</li>
                <li><strong>Color:</strong> Blue</li>
                <li><strong>Size:</strong> 13 x 5 Inch</li>
              </ul>
              <p class="gap">Our Yoga Body Wheel is a new therapeutic tool to deepen your yoga practice and take it to the next level. It helps in muscle stretching to improve muscle flexibility, relieve back pain, and make you stronger.
                <br /><br /> Whether you’re a serious yoga enthusiast or just want to relieve back pain, our spine roller tool will allow you to stretch your back and avoid pain and discomfort.
              </p>
            </div>
          </div>
          <v-btn
            outlined
            color="accent"
          >
            Details
          </v-btn>
        </div>
      </div>
      <div class="compare-title text-h5 text-md-h4 font-weight-medium">
        <span>Which InnerVue yoga wheel do you like?</span>
      </div>
      <div class="compare-container">
        <div class="item">
          <v-img contain height="150" src="@/assets/images/yoga-wheel-origin-series.png"></v-img>
          <span><strong>Origin Series</strong></span>
          <ul class="bullet-points">
            <li class="text-caption"><strong>Outer Circle: </strong>Cork</li>
            <li class="text-caption"><strong>Inner Circle: </strong>ABS</li>
            <li class="text-caption"><strong>Color: </strong>Cork</li>
            <li class="text-caption"><strong>Size: </strong>13 x 5 inch</li>
            <li class="text-caption"><strong>Include: </strong>a high-quality, well-designed yoga wheel and a posture guide</li>
          </ul>
          <div class="compare-description">
            <span class="text-caption">Nature style, eco-printed yoga ring with its elegant design. Cork material is eco friendly. Overall, it is a nature looking yoga wheel.</span>
          </div>
          <div class="compare-btn">
            <v-btn small outlined>Buy</v-btn>
          </div>
        </div>
        <div class="item">
          <v-img contain height="150" src="@/assets/images/yoga-wheel-pink-passion-series.png"></v-img>
          <span><strong>Passion Series</strong></span>
          <ul class="bullet-points">
            <li class="text-caption"><strong>Outer Circle: </strong>PU</li>
            <li class="text-caption"><strong>Inner Circle: </strong>ABS</li>
            <li class="text-caption"><strong>Color: </strong>Pink</li>
            <li class="text-caption"><strong>Size: </strong>13 x 5 inch</li>
            <li class="text-caption"><strong>Include: </strong>a high-quality, well-designed yoga wheel and a posture guide</li>
          </ul>
          <div class="compare-description">
            <span class="text-caption">Mandala style, eco-printed on nature material (PU) with its elegant design. A yoga wheel with a bright pink color impression.</span>
          </div>
          <div class="compare-btn">
            <v-btn small outlined>Buy</v-btn>
          </div>
        </div>
        <div class="item">
          <v-img contain height="150" src="@/assets/images/yoga-wheel-blue-passion-series.png"></v-img>
          <span><strong>Passion Series</strong></span>
          <ul class="bullet-points">
            <li class="text-caption"><strong>Outer Circle: </strong>Cork</li>
            <li class="text-caption"><strong>Inner Circle: </strong>ABS</li>
            <li class="text-caption"><strong>Color: </strong>Cork</li>
            <li class="text-caption"><strong>Size: </strong>13 x 5 inch</li>
            <li class="text-caption"><strong>Include: </strong>a high-quality, well-designed yoga wheel and a posture guide</li>
          </ul>
          <div class="compare-description">
            <span class="text-caption">Mandala style, eco-printed on nature material (PU) with its elegant design. A yoga wheel with a bright blue color impression.</span>
          </div>
          <div class="compare-btn">
            <v-btn small outlined>Buy</v-btn>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Shop",
  components: {
  },
  data: () => ({
    info: "Test Text",
  }),
  computed: {
    yogaWheelWidth(){
      if(this.$vuetify.breakpoint.name == "xs"){
        return 200;
      } else if(this.$vuetify.breakpoint.name == "sm"){
        return 300;
      } else {
        return 366
      }
    }
  }
};
</script>

<style scoped lang="scss">
@use "../styles/common";
.yoga-pattern-container{
  width: 100vw;
  border-top: solid 1px #000;
  img{
    width: 320px;
    display: block;
    margin: 0 auto;
  }
}
.main-container{
  display: flex;
  flex-direction: column;
  align-items: center;
  .product-row{
    display: flex;
    flex-direction: row;
    justify-content: center;
    margin-top: 50px;
    flex-wrap: wrap;
    max-width: common.$containerWidth;
    .right-container{
      flex: 1;
      min-width: 360px;
      padding: 0 30px 0 30px;
      box-sizing: border-box;
      margin-bottom: 30px;
      .title{
        .detail{
          .gap{
            margin-top: 30px;
          }
        }
      }
    }
  }
  .product-row-reverse{
    display: flex;
    flex-direction: row-reverse;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 50px;
    max-width: common.$containerWidth;
    .right-container{
      flex: 1;
      min-width: 360px;
      padding: 0 30px 0 30px;
      margin-bottom: 30px;
      box-sizing: border-box;
      .title{
        .detail{
          .gap{
            margin-top: 30px;
          }
        }
      }
    }
  }
  .compare-title{
    text-align: center;
    margin: 50px 20px 0 20px;
  }
  .compare-container{
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    flex-wrap: wrap;
    width: 100%;
    max-width: common.$containerWidth;
    margin: 50px 0 50px 0;

    .item{
      width: 250px;
      margin: 0 0 30px 0;

      .bullet-points{
        list-style: none;
        padding-left: 10px;
        margin-top: 10px;
      }
      .compare-description{
        margin-top: 10px;
      }
      .compare-btn{
        margin-top: 20px;
      }
    }
  }
}
</style>