<script setup>
import { ref, watch } from 'vue';
import axios from 'axios';

const props = defineProps({
  title: String
});
const emit = defineEmits(['select']);

const API_URL = "http://localhost:8000";

const recommendations = ref(null);
const error = ref(null);
const loading = ref(false);

watch(() => props.title, async (newTitle) => {
  if (!newTitle) return;

  loading.value = true;
  error.value = null;

  try {
    const response = await axios.get(`${API_URL}/recommendations/${encodeURIComponent(newTitle)}`);
    recommendations.value = response.data;
  } catch (err) {
    error.value = err.response?.data?.error || 'Erro ao buscar recomendações.';
    recommendations.value = null;
  } finally {
    loading.value = false;
  }
}, { immediate: true });

const handleClick = (movieTitle) => {
  emit('select', movieTitle);
};
</script>

<template>
  <v-container>
    <div v-if="loading">Carregando recomendações...</div>
    <div v-else-if="error">{{ error }}</div>

    <template v-else-if="recommendations && recommendations.length">
      <h2 class="text-h5 mb-4">Filmes recomendados</h2>
      <v-row dense>
        <v-col
          v-for="(movie, i) in recommendations"
          :key="i"
          cols="12"
          sm="6"
          md="4"
          lg="3"
        >
          <v-card
            class="pa-2 hoverable"
            @click="handleClick(movie.title)"
            style="cursor: pointer;"
          >
            <v-img
              :src="movie.poster"
              :alt="movie.title"
              height="300px"
              cover
            />
            <v-card-title class="text-subtitle-1 mt-2">
              {{ movie.title }}
            </v-card-title>
          </v-card>
        </v-col>
      </v-row>
    </template>
  </v-container>
</template>

<style scoped>
h2 {
  font-weight: 500;
}
</style>
