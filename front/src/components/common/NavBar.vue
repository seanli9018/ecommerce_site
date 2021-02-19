<template>
  <div class="ec-container">
    <v-app-bar
      app
      color="primary"
      flat
      height="40px"
    >
      <div class="bar-container">
        <div class="logo-container">
          <img alt="InnerVue Sports Logo" src="../../assets/logos/logo-dark.png"/>
        </div>
        <v-spacer></v-spacer>
        <ul class="nav-container d-none d-md-flex text-md-body-2 font-weight-thin">
          <li>
            <div class="nav-title"><router-link to="/">Home</router-link></div>
          </li>
          <li><div class="nav-title"><router-link to="/shop">Shop</router-link></div></li>
          <li><div class="nav-title">About</div></li>
          <li><div class="nav-title">Contact</div></li>
          <li v-click-outside="onClickOutsideCart">
            <div class="nav-title" @click="cartToggle = !cartToggle"><v-icon medium color="accent">mdi-cart-outline</v-icon></div>
            <ul v-show="cartToggle">
              <li class="text-caption"><router-link to="cart">InnerCart</router-link></li>
              <li class="text-caption">History</li>
            </ul>
          </li>
          <li v-click-outside="onClickOutsideUser">
            <div class="nav-title" v-if="!is_loggedin" @click.stop="profileToggle = !profileToggle"><v-icon medium color="accent">mdi-account-circle-outline</v-icon></div>
            <div class="nav-title" v-else @click.stop="profileToggle = !profileToggle">{{$auth.user.username}}</div>
            <ul v-if="!is_loggedin" v-show="profileToggle" >
              <li class="text-caption"><router-link to="login">Log in</router-link></li>
              <li class="text-caption"><router-link to="register">Register</router-link></li>
            </ul>
            <ul v-else v-show="profileToggle">
              <li class="text-caption">My Account</li>
              <li class="text-caption"><a href="#" @click.prevent="onLogOut">Log Out</a></li>
            </ul>
          </li>
        </ul>
        <div class="mobile-container d-md-none" v-click-outside="onClickOutsideSidebar">
            <section><v-icon medium @click.prevent="showSidebar = !showSidebar">mdi-centos</v-icon></section>
            <section class="d-md-none sidebar text-caption" v-show="showSidebar">
              <ul class="list-ul">
                <li><router-link to="/">Home</router-link></li>
                <li><router-link to="/shop">Shop</router-link></li>
                <li>About</li>
                <li>Contact</li>
                <li><router-link to="login">Log in</router-link></li>
                <li><router-link to="register">Register</router-link></li>
              </ul>
            </section>
        </div>
      </div>
    </v-app-bar>
  </div>
</template>

<script>
export default {
  name: "ec-navbar",
  components: {
  },
  data: () => ({
    profileToggle: false,
    cartToggle: false,
    showSidebar: false,
    is_loggedin: false
  }),
  mounted(){
    this.is_loggedin = this.$auth.is_authenticated;
  },
  methods: {
    onLogOut(){
      this.$auth.clearUserToken();
      this.$router.replace({name: "login"});
    },
    onClickOutsideSidebar(){
      this.showSidebar = false;
    },
    onClickOutsideUser(){
      this.profileToggle = false;
    },
    onClickOutsideCart(){
      this.cartToggle = false;
    }
  },
  watch:{
    "$route"(){
      this.profileToggle = false;
      this.cartToggle = false;
      this.showSidebar = false;
      this.is_loggedin = this.$auth.is_authenticated;
    }
  }
};
</script>

<style scoped lang="scss">
@use "../../styles/common";

.ec-container{
  .bar-container{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    width: common.$containerWidth;
    margin: 0 auto;
    height: common.$headerHeight;
    .logo-container{
      height: 18px;
      img{
        width: 150px;
      }
    }
    .nav-container{
      list-style: none;
      display: flex;
      flex-direction: row;
      align-items: center;
      width: 560px;
      height: common.$headerHeight;
      padding-left: 0;

      li{
        flex: 1;
        height: 100%;
        display: flex;
        flex-direction: column;
        a{
          text-decoration: none;
        }
        .nav-title {
          flex: 0 0 common.$headerHeight;
          display: flex;
          flex-direction: column;
          justify-content: center;
          text-align: center;
          cursor: pointer;
        }
        ul {
          display: flex;
          flex-direction: column;
          background-color: rgba(250,235,215, 0.3);
          padding: 0;
          margin-top: 3px;
          li{
            flex: 1 0 30px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            border: solid 1px #ccc;
          }
        }
      }
    }
    .mobile-container{
      line-height: common.$headerHeight;

      .sidebar{
        height: 100vh;
        width: 150px;
        position: fixed;
        right: 0;
        top: common.$headerHeight;
        background-color: rgba(0, 0, 0, 0.8);
        color: #fff;
        .list-ul{
          list-style: none;
          padding-left: 0;
          li{
            padding: 20px 0 20px 10px;
            border-bottom: solid 1px #ccc;
            a{
              color: #fff;
              text-decoration: none;
            }
          }
        }
      }
    }
  }
}
</style>

