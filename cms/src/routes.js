import Vue from "vue"
import VueRouter from "vue-router"
import Index from "@/components/Index";
import Login from "@/components/Login"
import MainFrame from "@/components/MainFrame";
import auth from "@/utils/auth";
import message from "@/utils/message"
import NewProduct from "@/components/NewProduct";

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    component: MainFrame,
    children: [
      {path: "", component: Index, name: "index"},
      {path: "/new-product", component: NewProduct, name: "new-product"}
    ],
    meta: {requireAuth: true}
  },
  {
    path: "/login",
    component: Login,
    name: "login"
  }
]

const router = new VueRouter({
  routes: routes
})
router.beforeEach(function(to, from, next){
  const is_loggedin = auth.is_authenticated;
  if(to.matched.some(m => m.meta.requireAuth) && !is_loggedin){
    next({
      path: "/login",
      query: {redirect: to.fullPath}
    })
    message.error("Please log in first.")
  }else if(to.name == "login"){
    if(is_loggedin){
      next("/")
      message.info("You have already logged in.")
    }else{
      next()
    }
  }else{
    next()
  }
})
export default router;