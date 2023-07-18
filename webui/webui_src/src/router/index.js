// Composables
import { createRouter, createWebHashHistory } from "vue-router";
import useAuthStore  from "@/apps/auth/store/auth.store";
import authRoutes from "@/apps/auth/auth.routes"
const routes = [
  {
    path: "/",
    component: () => import(/* webpackChunkName: "home" */ "@/views/HomePage.vue"),
  },
  ...authRoutes,
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});
router.beforeEach(async (from, to, next) => {
  const store = useAuthStore();
  await store.checkAuth();
  next();
});

export default router;
