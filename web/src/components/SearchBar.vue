<script setup>
import { ref, watch, defineEmits } from 'vue';
import axios from 'axios';

const API_URL = "http://localhost:8000"

const search = ref('');
const items = ref([]);
const selected = ref(null);

watch(search, async (newSearch) => {
  if (newSearch.length < 2) {
    items.value = [];
    return;
  }

  try {
    const response = await axios.get(`${API_URL}/search?query=${encodeURIComponent(newSearch)}`);
    items.value = response.data.reverse();
  } catch (error) {
    console.log("Erro na busca:", error);
    items.value = [];
  }
});

const emit = defineEmits(['update:selected']);

watch(selected, (val) => {
  emit('update:selected', val);
});
</script>

<template>
  <v-autocomplete
    v-model="selected"
    v-model:search="search"
    :items="items"
    label="Search"
    variant="outlined"
    item-title="name"
    item-value="name"
    no-filter
  />
</template>

<style scoped>

</style>
