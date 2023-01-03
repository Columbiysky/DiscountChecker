<template>
  <div class="container">
    <div class="newValue">
      <div class="item">
        Your items
      </div>
      <Button style="margin-top: 5px;" class="p-button-outlined" label="New item" @click="handleNewLine()" />

    </div>
    <div style="padding-top: 5px;">
      <DataTable :value="data" editMode="cell" :showAddButton=true @cell-edit-complete="onCellEditComplete">
        <Column field="name" header="Name">
          <template #editor="slotProps">
            <InputText v-model="slotProps.data[slotProps.field]" />
          </template>
        </Column>
        <Column field="link" header="Link">
          <template #editor="slotProps">
            <InputText v-model="slotProps.data[slotProps.field]" />
          </template>
        </Column>
        <Column field="timeout" header="Timeout">
          <template #editor="slotProps">
            <InputNumber v-model="slotProps.data[slotProps.field]" showButtons :min=60 />
          </template>
        </Column>
        <Column field="timeOfLastCheck" header="Time of last check"></Column>
        <Column header="Delete"><template #editor="slotProps">
            <Button v-model="slotProps.data" @click="handleDelete(slotProps.data)" />
          </template></Column>
      </DataTable>
    </div>
  </div>
</template>

<script>
import * as _ from 'lodash'
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
      data: [],
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
  methods: {
    onCellEditComplete(event) {
      let { data, newValue, field } = event;

      switch (event.field) {
        case 'year':
          if (this.isPositiveInteger(newValue))
            data[field] = newValue;
          else
            event.preventDefault();
          break;

        default:
          if ((typeof (newValue) === "string" && newValue.trim().length > 0) || typeof (newValue) !== "string")
            data[field] = newValue;
          else
            event.preventDefault();
          break;
      }
    },
    handleDelete(event) {
      _.remove(this.data, function (value) {
        return value.link === event.link
          && value.name === event.name;
      })
    },
    handleNewLine() {
      this.data.push({ undefined, undefined, undefined, undefined });
    }
  },
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
  grid-template-columns: 1fr auto;
}
</style>
