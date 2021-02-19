// created by Sean Li on Oct 29 2020
<template>
  <div class="ec-container">
    <div class="main-container">
      <div class="product-container">
        <div class="product-image" :style="{ width: productImageWidth + 'px'}">
          <agile class="main" ref="main" :fade="true" :as-nav-for="mainNavController" :options="mainOption">
            <div class="slide" v-for="(slide, index) in slides" :key="index">
              <img :src="slide"/>
            </div>
          </agile>
          <agile class="thumbnails" ref="thumbnails" :as-nav-for="thumbNavController" :slides-to-show="1" :options="thumbOption">
            <div class="slide slide-thumbnail" v-for="(slide, index) in slides" :key="index" @click="$refs.thumbnails.goTo(index)">
              <img :src="slide"/>
            </div>
          </agile>
        </div>
        <div class="product-action">
          <div class="product-title text-center">
            <h1 class="text-h6 font-weight-medium">Origin Series Yoga Wheel</h1>
          </div>
          <div class="product-price text-center">
            <span class="text-body-2 text-md-body-1">$49.99</span>
          </div>
          <div class="divider">
            <v-divider></v-divider>
          </div>
          <div class="product-color">
            <div class="color-value text-center">
              <span class="text-body-2 text-md-body-1">COLOR - {{colorOption}}</span>
            </div>
            <div class="color-selector text-center">
              <input type="radio" v-model="colorOption" id="cork-yoga-wheel" class="yoga-wheel-checkbox" value="cork" hidden>
              <label class="out-circle" for="cork-yoga-wheel"><div class="cork"></div></label>
              <input type="radio" v-model="colorOption" id="blue-yoga-wheel" class="yoga-wheel-checkbox" value="blue" hidden>
              <label class="out-circle" for="blue-yoga-wheel"><div class="blue"></div></label>
              <input type="radio" v-model="colorOption" id="pink-yoga-wheel" class="yoga-wheel-checkbox" value="pink" hidden>
              <label class="out-circle" for="pink-yoga-wheel"><div class="pink"></div></label>
            </div>
          </div>
          <div class="product-stepper">
            <ec-stepper></ec-stepper>
          </div>
          <div class="add-to-cart action-btn">
            <v-btn
              class="text-caption"
              outlined
              text
              block
              color="accent"
            >
              Add to Cart
            </v-btn>
          </div>
          <div class="place-order action-btn">
            <v-btn
              class="text-caption"
              outlined
              block
              color="accent"
            >
              Place Order
            </v-btn>
          </div>
          <div class="product-description">
            <v-expansion-panels flat focusable class="text-caption">
              <v-expansion-panel>
                <v-expansion-panel-header class="text-body-2">
                  Features
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                </v-expansion-panel-content>
              </v-expansion-panel>
              <v-expansion-panel>
                <v-expansion-panel-header class="text-body-2">
                  Description
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                </v-expansion-panel-content>
              </v-expansion-panel>
              <v-expansion-panel>
                <v-expansion-panel-header class="text-body-2">
                  Dimension
                </v-expansion-panel-header>
                <v-expansion-panel-content>
                  Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
                </v-expansion-panel-content>
              </v-expansion-panel>
            </v-expansion-panels>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { VueAgile } from "vue-agile";
import Stepper from "../components/common/Stepper";

export default {
  name: "ProductDetail",
  components: {
    agile: VueAgile,
    [Stepper.name]: Stepper
  },
  data: () => ({
    mainNavController: [],
    thumbNavController: [],
    mainOption: {
      dots: false,
      fade: true,
      navButtons: false
    },
    thumbOption: {
      autoplay: false,
      centerMode: true,
      dots: false,
      navButtons: false,
      slidesToShow: 3,
      responsive: [
        {
          breakpoint: 300,
          settings: {
            slidesToShow: 2,
          }
        },
        {
          breakpoint: 600,
          settings: {
            slidesToShow: 3
          }
        }
      ],
    },
    slides: [
      'https://images.unsplash.com/photo-1453831362806-3d5577f014a4?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ',
      'https://images.unsplash.com/photo-1496412705862-e0088f16f791?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ',
      'https://images.unsplash.com/photo-1506354666786-959d6d497f1a?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ',
      'https://images.unsplash.com/photo-1455619452474-d2be8b1e70cd?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ',
      'https://images.unsplash.com/photo-1504674900247-0877df9cc836?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ',
      'https://images.unsplash.com/photo-1472926373053-51b220987527?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ',
      'https://images.unsplash.com/photo-1497534547324-0ebb3f052e88?ixlib=rb-1.2.1&q=85&fm=jpg&crop=entropy&cs=srgb&w=1600&fit=max&ixid=eyJhcHBfaWQiOjE0NTg5fQ'
    ],
    colorOption: "cork"
  }),
  mounted () {
    this.mainNavController.push(this.$refs.thumbnails)
    this.thumbNavController.push(this.$refs.main)
  },
  computed: {
    productImageWidth(){
      if(this.$vuetify.breakpoint.width <= 964){
        return this.$vuetify.breakpoint.width - 20;
      } else {
        return 680
      }
    }
  }
};
</script>
<style scoped>
  .v-expansion-panel >>> .v-expansion-panel-header{
    border-top: solid 1px #ccc;
    border-left: solid 1px #ccc;
    border-right: solid 1px #ccc;
    padding: 10px 10px;
    color: #8d8d8d;
  }
  .v-expansion-panel:last-child >>> .v-expansion-panel-header{
    border-bottom: solid 1px #ccc;
  }
</style>
<style scoped lang="scss">
@use "../styles/common";
.main-container{
  display: flex;
  flex-direction: column;
  align-items: center;
  .product-container{
    max-width: common.$containerWidth;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    padding: 0;
    margin: 30px 0;
    .product-image{
      margin: -10px 10px 30px 10px;
      .main {
        margin-bottom: 10px;
      }
      .thumbnails {
        margin: 0 -5px;
        width: calc(100% + 10px);
        .slide-thumbnail {
          //background-color: antiquewhite;
          cursor: pointer;
          height: 100%;
          padding: 0 5px;
          -webkit-transition: opacity 0.3s;
          transition: opacity 0.3s;
        }
      }
      .slide {
        -webkit-box-align: center;
        align-items: center;
        box-sizing: border-box;
        color: #fff;
        display: -webkit-box;
        display: flex;
        width: 100%;
        -webkit-box-pack: center;
        justify-content: center;
      }
      .slide-thumbnail:hover {
        opacity: 0.75;
      }
      .slide img {
        -o-object-fit: contain;
        object-fit: contain;
        -o-object-position: center;
        object-position: center;
        width: 100%;
      }
    }
    .product-action{
      padding: 0 10px 0 10px;
      flex: 1;
      box-sizing: border-box;
      min-width: 265px;
      .product-title{
        margin-bottom: 10px;
      }
      .divider{
        margin: 20px 0;
      }
      .product-color{
        .color-value{
          height: 30px;
          line-height: 30px;
        }
        .color-selector{
          .out-circle{
            display: inline-block;
            width: 40px;
            height: 40px;
            border: solid 1px #cccccc;
            border-radius: 100%;
            box-sizing: border-box;
            margin: 10px;
          }
          .yoga-wheel-checkbox:checked + label{
            border: solid 1px black;
          }
          .cork{
            display: inline-block;
            width: 30px;
            height: 30px;
            border-radius: 100%;
            background-color: #d2b172;
            cursor: pointer;
            margin: 4px;
            box-sizing: border-box;
          }
          .blue{
            display: inline-block;
            width: 30px;
            height: 30px;
            border-radius: 100%;
            background-color: blue;
            cursor: pointer;
            margin: 4px;
            box-sizing: border-box;
          }
          .pink{
            display: inline-block;
            width: 30px;
            height: 30px;
            border-radius: 100%;
            background-color: pink;
            cursor: pointer;
            margin: 4px;
            box-sizing: border-box;
          }
        }
      }
      .product-stepper{
        //background-color: #cccccc;
        margin-bottom: 30px;
      }
      .action-btn{
        margin-bottom: 10px;
      }
      .product-description{
        margin-top: 30px;
      }
    }
  }
}

</style>