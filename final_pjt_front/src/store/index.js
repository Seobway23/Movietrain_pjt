import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from "vuex-persistedstate"
import router from '@/router'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    // 로그인
    token: null,

    // 게시글
    articles: [],
  },
  getters: {
    isLogin(state){
      return state.token ? true : false
    }
  },
  mutations: {
    SAVE_TOKEN(state, token){
      state.token = token
      router.push({name: 'ArticleView'})
    }
  },
  actions: {

    // 회원 가입 구현
    signUp(context, payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2

      axios({
        method:'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        }
      })
      .then((res)=> {
        console.log(res)
        context.commit('SAVE_TOKEN', res.data.key)
      })
      // 400 bad_request가 나오면, 다시 입력하라는 문구를 보여줘야 함
      .catch((err) => {
        console.log(err)})
    },
    // 로그인 구현
    login(context, payload){
      const username = payload.username
      const password = payload.password

      axios({
        method: 'post',
        url: `${API_URL}/accounts/login/`,
        data: {
          username, password
        }
      })
      .then((res)=> {
        context.commit("SAVE_TOKEN", res.data.key)
      })
      .catch((err)=> console.log(err))
    }
  },
  modules: {
  }
})
