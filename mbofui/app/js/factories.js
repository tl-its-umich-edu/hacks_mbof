'use strict';
/* global mbofuiApp */
mbofuiApp.factory('Bof', function($q, $timeout, $window, $http) {
  return {
    PostBof : function(url) {
      return $http.post(url, {
        cache : false
      }).then(
          function success(result) {
            // we will get a response;
            // what to do with it
            return result;
          },
          function error(result) {
            // do some error things
          });
    }
  };
});