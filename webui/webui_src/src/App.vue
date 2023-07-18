<template>
  <v-app>
    <the-nav-bar/>
    <v-main>
      <router-view />
    </v-main>
  </v-app>

</template>

<script setup>
import TheNavBar from './components/TheNavBar.vue';

</script>
