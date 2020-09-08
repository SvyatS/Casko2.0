new Vue({
  el: '#vue-table',
  data: {
    drivers: []
  },
  created: function(){
    axios.get('../policyholder/?format=json')
    .then(responce => (this.drivers = responce.data))
  },
  filters: {
    formatDate: function(value){
      if (value) {
        return moment(String(value)).format('DD.MM.YYYY  HH:mm')
      }
    }
  }
});