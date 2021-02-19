// created by Sean on Oct 9 2020
<template>
  <div class="ec-container">
    <div class="container">
      <div class="login-container">
        <div class="title">
          <span class="text-h6">New InnerVue</span>
        </div>
        <v-form
          ref="form"
          v-model="valid"
          lazy-validation
        >
          <div class="email-container">
            <v-text-field
              v-model="dataItems.email"
              :rules="rules.emailRules"
              label="E-mail"
              color="accent"
              class="email-input"
              required
            >
            </v-text-field>
            <v-btn
              :disabled="!captchaEnable"
              color="accent"
              outlined
              @click="sendCaptcha"
              class="send-capture-btn"
              small
            >
              {{ captchaBtnText }}
            </v-btn>
          </div>

          <v-text-field
            v-show="showCaptchaInput"
            v-model="dataItems.captcha"
            :rules="rules.captchaRules"
            label="Verification code"
            color="accent"
            class="captcha-input"
            required
          ></v-text-field>

          <v-text-field
            v-model="dataItems.username"
            :rules="rules.usernameRules"
            label="Username"
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

          <v-text-field
            v-model="dataItems.confirmPassword"
            :rules="[(dataItems.password === dataItems.confirmPassword) || 'Password must match']"
            label="Confirm Password"
            :append-icon="showConfirmPassword ? 'mdi-eye' : 'mdi-eye-off'"
            :type="showConfirmPassword ? 'text' : 'password'"
            color="accent"
            required
            @click:append="showConfirmPassword = !showConfirmPassword"
          ></v-text-field>

          <div class="action-btns text-caption">
            <v-btn
              @click="submit"
              class="mr-2 login-btn"
              outlined
              color="accent"
            >
              Register
            </v-btn>
            <span class="register"><router-link to="/login">Log in InnerVue</router-link></span>
          </div>
        </v-form>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Register",
  components: {},
  data: () => ({
    valid: true,
    showPassword: false,
    showConfirmPassword: false,
    captchaEnable: true,
    showCaptchaInput: false,
    captchaBtnText: "Send Code",
    dataItems: {
      email: "",
      captcha: "",
      username: "",
      password: "",
      confirmPassword: "",
    },
    rules: {
      emailRules: [
        v => !!v || "E-mail is required",
        v => /.+@.+\..+/.test(v) || "Please enter a valid E-mail address",
      ],
      usernameRules: [
        v => !!v || "username is required",
        v => /^([A-Za-z0-9])\w+$/.test(v) || "Please enter a valid username. Only letters, numbers, _ will be accepted.",
      ],
      passwordRules: [
        v => !!v || "Password is required",
        v => (v && v.length >= 8) || "Password has to be at least 8 Characters."
      ],
      captchaRules: [
        v => /^([0-9])+$/.test(v) || "Numbers only, check your email for verification code."
      ]
    }
  }),
  methods: {
    countDown() {
      let count = 60;
      this.captchaEnable = false;
      const countDownTimer = setInterval(() => {
        if (count <= 0) {
          this.captchaBtnText = "Resend";
          this.captchaEnable = true
          clearInterval(countDownTimer)
          return
        }
        this.captchaBtnText = "Enable in " + count + "s"
        count -= 1
      }, 1000)
    },
    sendCaptcha() {
      if (this.dataItems.email) {
        const email_validated = /.+@.+\..+/.test(this.dataItems.email)
        if (email_validated) {
          const params = {
            email: this.dataItems.email
          }
          this.$http.sendCaptcha(params).then(response => {
            this.countDown();
            this.showCaptchaInput = true;
            this.$message.success(response.data.message);
          }).catch(error => {
            if (error.response.data) {
              this.$message.error(error.response.data.message.email[0])
            } else {
              this.$message.error("Something went wrong, please try it again later")
            }
          })
        } else {
          this.$message.error("Invalid email address.")
        }
      } else {
        this.$message.error("Please enter a email address first.")
      }
    },
    submit() {
      if (!this.$refs.form.validate()) {
        this.$message.error("Please input valid data.")
        return
      }
      this.$loading.show()
      const data = {
        email: this.dataItems.email,
        username: this.dataItems.username,
        captcha: this.dataItems.captcha,
        password: this.dataItems.password,
        confirmPassword: this.dataItems.confirmPassword,
      }
      this.$http.register(data).then(response => {
        this.$message.success("Welcome " + response.data.user.username)
        const user = response.data.user
        const token = response.data.token
        this.$auth.setUserToken(user, token)
        this.$loading.close()
        this.$router.replace("/")
      }).catch(error => {
        if (error.response.data.message) {
          if (error.response.data.message["non_field_errors"]) {
            this.$message.error(error.response.data.message["non_field_errors"][0])
          } else {
            this.$message.error(error.response.data.message)
          }
        } else {
          this.$message.error("Something went wrong, please try it again later")
        }
        this.$loading.close()
      })
    }
  },
}
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
      margin-bottom: 20px;
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
      .email-container{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        flex-wrap: wrap;
        .email-input{
          max-width: 400px;
        }
        .captcha-input{
          flex: 0 0 120px;
          box-sizing: border-box;
          height: 100%;
          align-self: center;
        }
        .send-capture-btn{
          flex: 0 0 120px;
          align-self: center;
        }
      }
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