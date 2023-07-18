import { defineStore } from "pinia";

const useAuthStore = defineStore('auth', {
  state:()=>({
    isAuthenticated:false
  }),
  actions:{
    async checkAuth(){
      const res = await this.$http.get('check_auth/')
      this.isAuthenticated = res.data.isAuthenticated
    }
  }
})
export default useAuthStore;
