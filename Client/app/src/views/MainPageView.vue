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
        Timeout in Minutes:
        <InputNumber v-model="currentTimeoutInMinutes" :min="60" />
      </div>
    </div>
    <div style="padding-top: 5px;">
      <DataTable :value="data">
        <Column field="name" header="Name"></Column>
        <Column field="link" header="Link"></Column>
        <Column field="timeout" header="Timeout"></Column>
        <Column field="timeOfLastCheck" header="Time of last check"></Column>
        <Column>
          <template #body>
            <Button type="button" icon="pi pi-pencil"></Button>
          </template>
        </Column>
      </DataTable>
    </div>
  </div>
</template>

<script>
/* eslint-disable */
const minimalTimeoutInMinutes = 60
const defaultOptions = {
  year: 'numeric',
  month: 'numeric',
  day: 'numeric',
  hour: 'numeric',
  minute: 'numeric',
  hour12: false,
  timeZone: 'Europe/Moscow',
}
export default {
  data() {
    return {
      data: null,
      options: defaultOptions,
      currentLink: '',
      currentName: '',
      currentTimeoutInMinutes: minimalTimeoutInMinutes,
    }
  },
  created() {
    this.data = [
      {
        name: 'Кронштейн под моники',
        link:
          'https://www.dns-shop.ru/product/88150834b7af2eb1/kreplenie-dla-monitorov-nb-f160/',
        timeout: 60,
        timeOfLastCheck: new Intl.DateTimeFormat('ru-RU', this.options).format(
          new Date(),
        ),
      },
    ]
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
