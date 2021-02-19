// created by Sean on Oct 7 2020
<template>
  <div class="ec-container">
    <div class="container">
      <div class="login-container">
        <div class="title">
          <span class="text-h6">Login InnerVue</span>
        </div>
        <v-form
          ref="form"
          v-model="valid"
          lazy-validation
        >
          <v-text-field
            v-model="dataItems.email"
            :rules="rules.emailRules"
            label="E-mail"
            color="accent"
            required
          ></v-text-field>

          <v-text-field
            v-model="dataItems.password"
            :rules="rules.passwordRules"
            label="Password"
            :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
            :type="showPassword ? 'text' : 'password'"
            color="accent"
            required
            @click:append="showPassword = !showPassword"
          ></v-text-field>
          <div class="action-btns text-caption">
            <v-btn
              @click="submit"
              class="mr-2 login-btn"
              outlined
              color="accent"
            >
              Login
            </v-btn>
            <span class="register"><router-link to="/register">New InnerVue? Create account</router-link></span>
          </div>
        </v-form>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Login",
  components: {
  },
  data: () => ({
    valid: true,
    showPassword: false,
    dataItems: {
      email: "",
      password: "",
    },
    rules: {
      emailRules: [
        v => !!v || "E-mail is required",
        v => /.+@.+\..+/.test(v) || "Please enter a valid E-mail address",
      ],
      passwordRules: [
        v => !!v || "Password is required"
      ]
    }
  }),
  methods: {
    submit(){
      if(!this.$refs.form.validate()){
        this.$message.error("Please input valid data.")
        return
      }
      this.$loading.show()
      const params = {
        username: this.dataItems.email,
        password: this.dataItems.password
      }
      this.$http.login(params).then(response => {
        this.$message.success("Successfully logged in InnerVue.")
        const user = response.data.user
        const token = response.data.token
        this.$auth.setUserToken(user, token)
        this.$loading.close()
        // record from page, once user successfully logged in, redirect to the redirect page
        const redirect = this.$route.query["redirect"]
        if(redirect){
          this.$router.push(redirect)
        }else{
          this.$router.replace("/")
        }
      }).catch(error => {
        console.log(error)
        this.$message.error("Username or password is not correct.")
        this.$loading.close()
      })
    }
  }
};
</script>
<style scoped lang="scss">
@use "../styles/common";
.ec-container{
  padding: 0;
  display: flex;
  flex-direction: row;
  justify-content: center;

  .container{
    background-image: url("../assets/images/innervue-yoga-login.jpg");
    background-color: antiquewhite;
    background-position: 30% 30%;
    background-repeat: no-repeat;
    background-size: cover;
    height: 100vh;
    max-width: 1920px;
    padding: 0;
    margin: 0;
    display: flex;
    flex-direction: row;
    justify-content: flex-end;
    align-items: center;
    .title{
      // border: solid 1px #aaa;
      margin-bottom: 20px;
      //background-color: #ccc;
      background-image: linear-gradient(90deg, #ddd 0%, #bbb 50%, #aaa 100%);
      padding: 10px;
      border-radius: 10px;
    }
    .login-container{
      width: 600px;
      background-color: rgba(255,255,255, 0.6);
      padding: 30px;
      margin: -100px 20px 0px 20px;
      border-radius: 10px;
      .action-btns{
        height: 65px;
        display: flex;
        flex-direction: row;
        justify-content: flex-start;
        align-items: center;
      }
    }
  }
}

</style>