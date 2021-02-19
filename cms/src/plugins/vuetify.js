import Vue from 'vue';
import Vuetify from 'vuetify/lib';
import colors from 'vuetify/lib/util/colors';

Vue.use(Vuetify);

export default new Vuetify({
  theme: {
    dark: false,
    themes: {
      light: {
        primary: "#f2c993",
        secondary: "#faebd7",
        anchor: colors.shades.black,
        accent: colors.shades.black,
        error: colors.red.lighten1,
      },
      dark: {
        primary: "#f2c993",
        secondary: colors.grey.darken4,
        anchor: "#f2c993",
        accent: colors.shades.white,
      },
    },
  },
  icons: {
    iconfont: 'mdi', // default - only for display purposes
  }
});
