<template>
  <v-container class="fill-height d-flex justify-content-center">
    <v-row justify="center" align="center">
      <v-col cols="12" md="6">
        <div>
          <v-card class="mx-auto px-8 pb-8" elevation="8" max-width="448" rounded="lg">
            <v-img class="mx-auto my-6" max-width="228" src="/logo.png"></v-img>
            <v-divider class="my-6"></v-divider>
            <div class="text-subtitle-1 text-medium-emphasis">Account</div>

            <v-form v-model="isValid" @submit.prevent="doLogin">
              <v-text-field type="email"  density="compact" placeholder="Email address" prepend-inner-icon="mdi-email-outline"
                variant="outlined"></v-text-field>

              <div class="text-subtitle-1 text-medium-emphasis d-flex align-center justify-space-between">
                Password

                <a class="text-caption text-decoration-none text-blue" href="#" rel="noopener noreferrer" target="_blank">
                  Forgot login password?</a>
              </div>

              <v-text-field :rules="passwordRules" :append-inner-icon="visible ? 'mdi-eye-off' : 'mdi-eye'" :type="visible ? 'text' : 'password'"
                density="compact" placeholder="Enter your password" prepend-inner-icon="mdi-lock-outline"
                variant="outlined" @click:append-inner="visible = !visible"></v-text-field>

              <v-btn type="submit" :disabled="!isValid" block class="mb-8" color="blue" size="large" variant="tonal">
                Log In
              </v-btn>
            </v-form>

            <v-card-text class="text-center">
              <a class="text-blue text-decoration-none" href="#" rel="noopener noreferrer" target="_blank">
                Sign up now <v-icon icon="mdi-chevron-right"></v-icon>
              </a>
            </v-card-text>
          </v-card>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>
<script setup>
import { ref, computed } from 'vue';
const regex = /.+@.+\..+/;
const email = ref('')
const password = ref('')
const isValid = ref(false)
const visible = ref(false)
const doLogin = () => {
  console.log(email.value, password.value)
}
const emailRules = [
  v => !!v || "Email is required",
  v => regex.test(v) || "Pleas provide a valid Email"
]
const passwordRules = [
  v => !!v || "Password is required",
]
</script>
