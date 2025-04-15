<script setup>
import { ref, watch } from 'vue';
import axios from 'axios';

// Define a prop chamada title
const props = defineProps({
  title: String
});

const API_URL = "http://localhost:8000";

const movie = ref(null);
const error = ref(null);
const loading = ref(false);

// Watch para reagir quando a prop "title" mudar
watch(() => props.title, async (newTitle) => {
  if (!newTitle) return;

  loading.value = true;
  error.value = null;

  try {
    const response = await axios.get(`${API_URL}/movie/${encodeURIComponent(newTitle)}`);
    movie.value = response.data;
  } catch (err) {
    error.value = err.response?.data?.error || 'Erro ao buscar filme.';
    movie.value = null;
  } finally {
    loading.value = false;
  }
}, { immediate: true }); // chama na primeira vez também
</script>

<template>
  <v-container>
    <div v-if="loading">Carregando...</div>
    <div v-else-if="error">{{ error }}</div>
      <v-row v-else-if="movie">
        <v-card>
          <v-container class="ma-3">
            <v-row class="mb-4">
              <h1 class="text-h4">{{ movie.title }} ({{ movie.year }})</h1>
            </v-row>
            <v-row>
              <v-col>
                <img :src="movie.poster" alt="Poster" style="max-width: 200px; margin-bottom: 1rem" />
              </v-col>
              <v-col>
                <p><strong>Nota IMDb:</strong> {{ movie.imdbRating }} ({{ movie.imdbVotes }} votos)</p>
                <p><strong>Duração:</strong> {{ movie.runtime }} minutos</p>
                <p><strong>Orçamento:</strong> ${{ movie.budget.toLocaleString() }}</p>
                <p><strong>Receita:</strong> ${{ movie.revenue.toLocaleString() }}</p>
                <p><strong>Lançado em:</strong> {{ movie.released }}</p>
                <p><strong>Idiomas:</strong> {{ movie.languages.join(', ') }}</p>
                <p><strong>Países:</strong> {{ movie.countries.join(', ') }}</p>
                <p><strong>Sinopse:</strong> {{ movie.plot }}</p>
                <a :href="movie.url" target="_blank">Ver no TMDb</a>
              </v-col>
            </v-row>
          </v-container>
        </v-card>
      </v-row>
  </v-container>
</template>

<style scoped>
p {
  margin: 0.5rem 0;
}
</style>
