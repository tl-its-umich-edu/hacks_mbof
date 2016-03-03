'use strict';
/* global mbofuiApp */

mbofuiApp.controller('mbofuiAppController', ['$scope', 'Bof', '$log', '$window', function($scope, Bof, $log, $window) {


    var pos = $window.navigator.geolocation.getCurrentPosition(posSuccess, posError);

    function posSuccess(pos) {
        var latlng = new google.maps.LatLng(pos.coords.latitude,
            pos.coords.longitude);
        var options = {
            zoom: 18,
            center: latlng,
            mapTypeControl: true,
            mapTypeId: google.maps.MapTypeId.HYBRID
        };
        var map = new google.maps.Map(document.getElementById('map'), options);

        var marker = new google.maps.Marker({
            position: latlng,
            map: map
        });
        getBofs(map);
    }

    function posError(map) {
        var map = new google.maps.Map(document.getElementById('map'), options);
        getBofs(map);
    }

    function getBofs(map) {
        var bofsUrl = '/api/messages/'
        Bof.GetBofs(bofsUrl).then(function(result) {
            $scope.totalBofs = result.data.results.length;
            angular.forEach(result.data.results, function(bof) {
                var marker = new google.maps.Marker({
                    position: { lat: bof.latitude, lng: bof.longitude },
                    map: map
                });
                var iconFile = 'http://maps.google.com/mapfiles/ms/icons/green-dot.png'; 
                marker.setIcon(iconFile) 
                
                google.maps.event.addListener(marker, 'click', function() {
                    var infowindow = new google.maps.InfoWindow({
                        content: bof.messageText
                    });
                    infowindow.open(map, marker);
                });



            });

        });
     }   
    
    $scope.postBof = function() {
        var pos = $window.navigator.geolocation.getCurrentPosition(posSuccess, posError);

        function posSuccess(pos) {
            $scope.coords = pos.coords;
            // serialize the inputs to create a URL
            var url = '/api/messages/?messageText=' + $scope.newMessageText +
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
