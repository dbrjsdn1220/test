import "@/assets/scss/main.scss";
import { createApp } from "vue";
import piniaPluginPersistedstate from "pinia-plugin-persistedstate";
import App from "@/App.vue";
import router from "@/router";
import { createPinia } from "pinia";

const app = createApp(App);
const pinia = createPinia();
pinia.use(piniaPluginPersistedstate);

app.use(pinia);
app.use(router);

app.mount("#app");
