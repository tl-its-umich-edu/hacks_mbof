'use strict';
/* global mbofuiApp */

mbofuiApp.controller('mbofuiAppController', ['$scope', 'Bof', '$log', '$window', function($scope, Bof, $log, $window) {

    $scope.postBof = function() {
        var pos = $window.navigator.geolocation.getCurrentPosition(posSuccess, posError);

        function posSuccess(pos) {
            $scope.coords = pos.coords;
            // serialize the inputs to create a URL
            var url = '/messages?messageText=' + $scope.newMessageText +
                '&startTime=' + $scope.newStartTime +
                '&endTime=' + $scope.newEndTime +
                '&latitude=' + $scope.coords.latitude +
                '&longitude=' + $scope.coords.longitude +
                '&altitudeMeters=' + $scope.coords.accuracy;
            $log.info(url);
            Bof.PostBof(url).then(function(result) {
                //

            });
        }

        function posError(err) {
            $log.info('ERROR(' + err.code + '): ' + err.message);
        }
    };
}]);
