import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import colors from 'vuetify/lib/util/colors';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    dark: false,
    themes: {
      light: {
        primary: "#faebd7",
        secondary: "#f2c993",
        anchor: "#000",
        accent: colors.shades.black,
        error: colors.red.lighten1,
      },
      dark: {
        primary: colors.grey,
        anchor: colors.grey.lighten3,
      },
    },
  },
  icons: {
    iconfont: 'mdi', // default - only for display purposes
  }
});
