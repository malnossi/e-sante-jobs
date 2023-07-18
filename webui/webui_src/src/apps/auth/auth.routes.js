export default [
  {
    path:'/auth/login',
    name:"Login",
    component:()=>import("@/apps/auth/views/LoginView.vue")
  },
  {
    path:'/reset_password_confirm/:uid/:token',
    component:()=>import("@/apps/auth/views/ResetPasswordConfirm.vue")
  }
]
