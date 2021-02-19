<template>
  <div class="ec-container">
    <ec-navbar></ec-navbar>
    <v-main>
      <router-view></router-view>
    </v-main>
    <ec-footer></ec-footer>
  </div>
</template>
<script>
import NavBar from "../components/common/NavBar";
import Footer from "../components/common/Footer";
export default {
  name: "MainFrame",
  components: {
    [NavBar.name]: NavBar,
    [Footer.name]: Footer,
  },
  data: () => ({
    info: "Test Text"
  }),
};
</script>

<style scoped lang="scss">

</style>