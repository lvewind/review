import { createRouter, createWebHistory } from "vue-router";
import type { RouteRecordRaw } from "vue-router";

import HomeView from "../views/HomeView.vue";
import FileView from "../views/FileView.vue";
import LoginView from "../views/LoginView.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "home",
    component: HomeView,
    props: true,
  },
  {
    path: "/login",
    name: "登录",
    component: LoginView,
    props: true,
  },
  {
    path: "/upload",
    name: "upload",
    component: HomeView,
    props: true,
  },

  {
    path: "/read",
    name: "read",
    component: FileView,
    props: true,
  },
  {
    path: "/upload_files",
    name: "upload_files",
    component: FileView,
    props: true,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
