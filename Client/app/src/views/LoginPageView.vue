<template>
  <div class="container">
    <span class="p-float-label">
      <InputText id="login" type="text" v-model="login" />
      <label for="login">Login</label>
    </span>

    <span class="p-float-label" style="margin-top: 25px;">
      <InputText id="password" type="password" v-model="pass" />
      <label for="password">Password</label>
    </span>

    <Button
      style="margin-top: 5px;"
      class="p-button-outlined"
      label="Login"
      @click="handleLogin()"
    />

    <p>
      {{ error }}
    </p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      login: '',
      pass: '',
      error: '',
    }
  },
  name: 'LoginPage',
  props: {},
  methods: {
    handleLogin() {
      if (this.login === 'admin' && this.pass === 'admin') {
        this.error = ''
        this.$router.push('main')
      } else {
        this.error = 'Invalid login / password'
      }
    },
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  margin-top: 15%;
  display: grid;
  justify-content: center;
}
</style>
