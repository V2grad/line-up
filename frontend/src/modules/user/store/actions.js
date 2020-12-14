//import firebase from 'firebase'

export default {
  updateUser ({ commit, rootGetters }) {
    commit('updateUsername', "john")
  },
  updateUsername ({ commit, rootGetters }, name) {
    return firebase
      .database()
      .ref('users/' + rootGetters['auth/getUserId'])
      .set({
        username: name
      }).then(r => {
        commit('updateUsername', name)
        return true
      })
  }
}
