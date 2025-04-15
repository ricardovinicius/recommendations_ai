<template>
  <v-container class="my-8" max-width="900">
    <v-row class="mb-5">
      <MainTitle></MainTitle>
    </v-row>
    <v-row>
      <v-col>
        <SearchBar @update:selected="onSelectedChange"></SearchBar>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <MovieInfo :title="selected"/>
      </v-col>
    </v-row>
    <v-row>
      <SuggestedMovies class="mt-4" :title="selected" @select="handleSelect"></SuggestedMovies>
    </v-row>
  </v-container>
</template>

<script setup>
import { ref } from 'vue';

import SearchBar from "@/components/SearchBar.vue";
import MainTitle from "@/components/MainTitle.vue";
import MovieInfo from "@/components/MovieInfo.vue";
import SuggestedMovies from "@/components/SuggestedMovies.vue";

const selected = ref(null);

const onSelectedChange = (value) => {
  selected.value = value;
}

const handleSelect = (title) => {
  selected.value = title;
}
</script>
