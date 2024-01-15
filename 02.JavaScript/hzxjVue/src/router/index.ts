import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import FormAnt from "../views/FormAnt.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/form/:place_id?",
      name: "form",
      component: FormAnt,
    },
  ],
});

export default router;
