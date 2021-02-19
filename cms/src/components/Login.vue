// created by Sean Li on Nov 3, 2020
<template>
  <div class="ec-container">
    <div class="login-box">
      <v-card style="background-color: rgba(255,255,255, 0.5)">
        <v-card-title style="background-image: linear-gradient(90deg, #fff 0%, #ddd 70%, #ccc 90%, #bbb 100%);">
          InnerVue CMS
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text>
          <v-form
            ref="form"
          >
            <v-text-field
              v-model="dataItems.email"
              :rules="rules.emailRules"
              label="E-mail"
              required
            >
            </v-text-field>
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
            <div class="action-btns">
              <v-btn
                outlined
                text
                @click="submitLogin"
              >
                Login
              </v-btn>
            </div>
          </v-form>
        </v-card-text>
      </v-card>
    </div>
  </div>
</template>
<script>
export default {
  name: "Login",
  components: {
  },
  data: () => ({
    dataItems: {
      email: "",
      password: "",
    },
    rules: {
      emailRules: [
        v => !!v || "Email is required",
        v => /.+@.+\..+/.test(v) || "Please enter a valid E-mail address",
      ],
      passwordRules: [
        v => !!v || "Password is required"
      ]
    },
    showPassword: false,
  }),
  methods:{
    submitLogin(){
      if(!this.$refs.form.validate()){
        this.$message.error("Email or password is not valid")
        return
      }
      this.$loading.show()
      const params = {
        username: this.dataItems.email,
        password: this.dataItems.password
      }
      this.$http.login(params).then(response => {
        this.$message.success("Welcome! InnerVue Staff")
        const user = response.data.user
        const token = response.data.token
        this.$auth.setUserToken(user, token)
        this.$loading.close()
        // record from page, once user successfully logged in, redirect to the redirect page
        const redirect = this.$route.query["redirect"]
        if(redirect){
          this.$router.push(redirect)
          console.log(redirect)
        }else{
          this.$router.replace("/")
        }
      }).catch(error => {
        console.log(error.response.data.message)
        if(error.response.data.message["non_field_errors"]){
          this.$message.error(error.response.data.message["non_field_errors"][0])
        } else {
          this.$message.error(error.response.data.message)
        }
        this.$loading.close()
      })
    }
  }
};
</script>
<style scoped lang="scss">
.ec-container{
  background-image: url("../assets/images/landscape_cms_login.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  background-position: 50% 100%;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  .login-box{
    max-width: 500px;
    width: 100%;
    padding: 0 10px;
    .action-btns{
      margin-top: 30px;
    }
  }
}
</style>