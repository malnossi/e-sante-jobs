<template>
  <v-container>
    <v-row>
      <v-col cols="12" md="6">
        <v-form>
          <v-text-field :value="route.params.uid"></v-text-field>
          <v-text-field :value="route.params.token"></v-text-field>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>

<script setup>
import { useRoute } from 'vue-router';
const route = useRoute();
</script>
