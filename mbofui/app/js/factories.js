'use strict';
/* global projectMigrationApp, errorDisplay */
mbofuiApp.factory('Bof', function($q, $timeout, $window, $http) {
  return {
    PostBof : function(url) {
      return $http.post(url, {
        cache : false
      }).then(
          function success(result) {
            // we will get a response;
            return result;
          },
          function error(result) {
            errorDisplay(url, result.status,
                'Unable to post new BOF');
            result.errors.failure = true;
            return result;
          });
    }
  };
});