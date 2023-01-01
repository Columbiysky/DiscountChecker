<template>
  <div class="container">
    <div class="newValue">
      <div class="item">
        name:
        <InputText id="name" type="text" v-model="currentName" />
      </div>
      <div class="wideItem">
        link:
        <InputText id="link" type="text" v-model="currentLink" />
      </div>
      <div class="item" style="padding-left: 3px;">
        Minimal timeout (Minutes):
        <InputNumber v-model="currentTimeoutInMinutes" :min="60" />
      </div>
    </div>
    <div style="background-color: green;">green</div>
  </div>
</template>

<script>
/* eslint-disable */
const minimalTimeoutInMinutes = 60

export default {
  data() {
    return {
      data: {},
      currentLink: '',
      currentName: '',
      currentTimeoutInMinutes: minimalTimeoutInMinutes,
    }
  },
  name: 'MainPage',
  props: {},
  methods: {},
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-content: center;
  margin-top: 30px;
}

.newValue {
  display: grid;
  grid-template-columns: auto 2fr 1fr;
}

.item {
  flex-basis: 100px;
  flex-grow: 0;
}

.wideItem {
  flex-basis: 250px;
  flex-grow: 2;
  padding-left: 3px;
  display: grid;
  grid-template-columns: auto 1fr;
}
</style>
