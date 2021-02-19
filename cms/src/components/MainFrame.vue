// created by Sean Li on Nov 3, 2020
<template>
  <v-app>
    <v-app-bar app dense color="primary">
      <v-img
        src="@/assets/logos/logo-dark.png"
        max-width="150"
        contain
      ></v-img>
      <v-spacer></v-spacer>
      <div class="action-btns">
        <v-icon
          medium
        >
          mdi-account
        </v-icon>
      </div>
    </v-app-bar>
    <v-navigation-drawer app hide-overlay :expand-on-hover="is_mini_variant" permanent color="secondary">
      <v-list>
        <v-list-item color="accent">
          <v-list-item-icon>
            <v-icon>mdi-home</v-icon>
          </v-list-item-icon>

          <v-list-item-title class="text-body-2">Home</v-list-item-title>
        </v-list-item>
        <v-divider></v-divider>
        <!-- User Management Group -->
        <v-list-group
          :value="false"
          prepend-icon="mdi-account-box-outline"
          color="accent"
        >
          <template v-slot:activator>
            <v-list-item-title class="text-body-2">Users</v-list-item-title>
          </template>

          <v-list-group
            :value="true"
            no-action
            sub-group
            color="accent"
          >
            <template v-slot:activator>
              <v-list-item-content>
                <v-list-item-title class="text-body-2">Admin</v-list-item-title>
              </v-list-item-content>
            </template>

            <v-list-item
              v-for="([title, icon], i) in admins"
              :key="i"
              link
            >
              <v-list-item-title class="text-body-2" v-text="title"></v-list-item-title>

              <v-list-item-icon>
                <v-icon v-text="icon"></v-icon>
              </v-list-item-icon>
            </v-list-item>
          </v-list-group>

          <v-list-group
            no-action
            sub-group
            color="accent"
          >
            <template v-slot:activator>
              <v-list-item-content>
                <v-list-item-title class="text-body-2">Actions</v-list-item-title>
              </v-list-item-content>
            </template>

            <v-list-item
              v-for="([title, icon], i) in cruds"
              :key="i"
              link
            >
              <v-list-item-title class="text-body-2" v-text="title"></v-list-item-title>

              <v-list-item-icon>
                <v-icon v-text="icon"></v-icon>
              </v-list-item-icon>
            </v-list-item>
          </v-list-group>
        </v-list-group>
        <v-divider></v-divider>
        <!-- Product Management Group -->
        <v-list-group
          :value="true"
          prepend-icon="mdi-store"
          no-action
          color="accent"
        >
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title class="text-body-2">Products</v-list-item-title>
            </v-list-item-content>
          </template>

          <v-list-item link to="/new-product">
            <v-list-item-content>
              <v-list-item-title class="text-body-2">New Product</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item link>
            <v-list-item-content>
              <v-list-item-title class="text-body-2">Edit Product</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item link>
            <v-list-item-content>
              <v-list-item-title class="text-body-2">Delete Product</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-group>
      </v-list>
    </v-navigation-drawer>
    <v-main app>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-main>
    <v-footer app color="primary">
      <div class="footer-container">
        <span class="text-caption">Copyright © 2020 InnerVue Sports. All rights reserved.</span>
      </div>
    </v-footer>
  </v-app>
</template>
<script>
export default {
  name: "MainFrame",
  components: {
  },
  data: () => ({
    admins: [
      ['Management', 'mdi-account-multiple-outline'],
      ['Settings', 'mdi-cog-outline'],
    ],
    cruds: [
      ['Create', 'mdi-plus-outline'],
      ['Read', 'mdi-file-outline'],
      ['Update', 'mdi-update'],
      ['Delete', 'mdi-delete'],
    ],
  }),
  computed: {
    is_mini_variant(){
      if(this.$vuetify.breakpoint.width <= 1280){
        return true
      }else{
        return false
      }
    },
    customThemeColor(){
      if(this.$vuetify.theme.dark){
        console.log(this.$vuetify.theme.dark)
        console.log(this.$vuetify.theme.themes.dark.anchor)
        return this.$vuetify.theme.themes.dark.anchor
      }else{
        console.log(this.$vuetify.theme.dark)
        console.log(this.$vuetify.theme.themes.light.anchor)
        return this.$vuetify.theme.themes.light.anchor
      }
    }
  },
};
</script>
<style scoped>
.v-application >>> .primary--text{
  /*color: white !important;*/
}

</style>
<style scoped lang="scss">
.footer-container{
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  width: 100%;
}
</style>