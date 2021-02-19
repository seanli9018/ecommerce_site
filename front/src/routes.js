import Vue from "vue"
import VueRouter from "vue-router"
import MainFrame from "@/components/MainFrame";
import Home from "@/components/Home";
import Login from "@/components/Login";
import Register from "@/components/Register";
import Cart from "@/components/Cart";
import auth from "@/utils/auth";
import message from "@/utils/message";
import Shop from "@/components/Shop";
import ProductDetail from "@/components/ProductDetail";


Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    component: MainFrame,
    children: [
      {path: "", component: Home, name: "index"},
      {path: "login", component: Login, name: "login"},
      {path: "register", component: Register, name: "register"},
      {path: "cart", component: Cart, name: "cart", meta: {requireAuth: true}},
      {path: "shop", component: Shop, name: "shop"},
      {path: "product-detail", component: ProductDetail, name: "product-detail"}
    ]
  }
]

const router = new VueRouter({
  routes: routes
})

router.beforeEach(function(to, from, next){
  const is_loggedin = auth.is_authenticated;
  if(to.meta.requireAuth && !is_loggedin){
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
export default router