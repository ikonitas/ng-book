angular.module('myApp.services', [])

.factory('HitService', function($q, $http) {
  var service={
    count:function() {
      var d = $q.defer();
      $http.get('http://192.168.1.29:8001/angular/')
      .success(function(data, status) {
        d.resolve(data.hits);
      }).error(function(data, status) {
        d.reject(data);
      });
      return d.promise;
    },
    registerHit: function() {
      var d=$q.defer();
      $http.post('http://192.168.1.29:8001/angular/', {})
      .success(function(data, status) {
        d.resolve(data.hits);
      }).error(function(data, status) {
        d.reject(data);
      });
      return d.promise;
    }
  }
  return service;
});


