<template>
  <v-app-bar app flat color="transparent" extended>
    <template #prepend>
      <router-link to="/"><img src="/logo.png" width="250"/></router-link>
    </template>
    <template #append>
      <template v-if="store.isAuthenticated">
        <v-btn text color="error">Logout</v-btn>
      </template>
      <template v-else>
        <v-btn text color="axxent" :to="{name:'Login'}">Login</v-btn>
        <v-btn text color="primary">Register</v-btn>
      </template>
    </template>
  </v-app-bar>
</template>

<script setup>
import useAuthStore from '@/apps/auth/store/auth.store';
const store = useAuthStore()
</script>
