// created by Sean on Oct 7 2020
<template>
  <div class="ec-container">
    <div class="top-image">
      <div class="image-container">
      </div>
    </div>
    <div class="yoga-pattern-container">
      <img src="../../src/assets/images/yoga-pattern-reverse.png" alt="yoga-pattern" class="yoga-pattern">
    </div>
    <div class="main-container">
      <div class="product-row">
        <div class="left-container">
          <img src="../../src/assets/images/yoga-wheel-origin-series.png" alt="yoga-wheel" class="yoga-wheel">
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
                <br /> Whether you’re a serious yoga enthusiast or just want to relieve back pain, our spine roller tool will allow you to stretch your back and avoid pain and discomfort.
              </p>
            </div>
          </div>
          <v-btn
            class="ma-2"
            outlined
            color="accent"
          >
            Details
          </v-btn>
        </div>
      </div>
      <div class="product-row-2">
        <div class="left-container">
          <div class="title">
            <h1 class = "text-h5 text-md-h4 font-weight-medium">Passion Series</h1>
            <div class="detail text-body-2 text-md-body-1">
              <ul class="gap">
                <li><strong>Material:</strong> PU (outer circle) + ABS (inner circle)</li>
                <li><strong>Color:</strong> Pink</li>
                <li><strong>Size:</strong> 13 x 5 Inch</li>
              </ul>
              <p class="gap">Our Yoga Body Wheel is a new therapeutic tool to deepen your yoga practice and take it to the next level. It helps in muscle stretching to improve muscle flexibility, relieve back pain, and make you stronger.
                <br /> Whether you’re a serious yoga enthusiast or just want to relieve back pain, our spine roller tool will allow you to stretch your back and avoid pain and discomfort.
              </p>
            </div>
          </div>
          <v-btn
            class="ma-2"
            outlined
            color="accent"
          >
            Details
          </v-btn>
        </div>
        <div class="right-container">
          <img src="../../src/assets/images/yoga-wheel-pink-passion-series.png" alt="yoga-wheel" class="yoga-wheel">
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Home",
  components: {
  },
  data: () => ({
    info: "Test Text"
  }),
};
</script>
<style scoped lang="scss">
@use "../styles/common";
.top-image{
  width: 100vw;
  display: flex;
  justify-content: center;
  .image-container{
    width: 1920px;
    height: 100vh;
    margin: - common.$headerHeight 0 0 0;
    background-image: url("../../src/assets/images/zen-landscape.jpg");
  }
}
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
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 50px;
    max-width: common.$containerWidth;
    .left-container{
      flex: 0 0 320;
    }
    .right-container{
      flex: 1;
      min-width: 320px;
      padding: 0 30px 0 30px;
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
  .product-row-2{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 50px;
    max-width: common.$containerWidth;
    .left-container{
      flex: 1;
      min-width: 320px;
      padding: 0 30px 0 30px;
      box-sizing: border-box;
      .title{
        .detail{
          .gap{
            margin-top: 30px;
          }
        }
      }
    }
    .right-container{
      flex: 0 0 320;
    }
  }
}
</style>