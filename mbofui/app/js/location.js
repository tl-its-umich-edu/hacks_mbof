'use strict';
/* global angular*/
(function() {

    var mapBoffLocation = ['$window', function($window) {
        var template = '<div class="alert alert-info status"><span id="status">Where are you?</span></div>' +
            '<div id="map"></div>',
            mapContainer = null,
            status = null;

        function link(scope, elem, attrs) {
            status = angular.element(document.getElementById('status'));
            mapContainer = angular.element(document.getElementById('map'));

            mapContainer.attr('style', 'height:' + scope.height + '%;width:' + scope.width + '%');

            $window.navigator.geolocation.getCurrentPosition(mapLocation, geoError);
            
        }

        function mapLocation(pos) {
            status.html('Ah - there you are!');
            var latlng = new google.maps.LatLng(pos.coords.latitude,
                pos.coords.longitude);
            var options = {
                zoom: 18,
                center: latlng,
                mapTypeControl: true,
                mapTypeId: google.maps.MapTypeId.HYBRID
            };

            var map = new google.maps.Map(mapContainer[0], options);

            var marker = new google.maps.Marker({
                position: latlng,
                map: map
            });
        }

        function geoError(error) {
            // either user does not want to share location
            // or there has been an error - send them to the Diag
            mapLocation({
                "coords": {
                    "latitude": 42.277237,
                    "longitude": -83.738202
                }
            })
            if (error.__proto__.PERMISSION_DENIED ===1){
                status.html('Lurker mode');
            } else {
                status.html('Failed lookup ' + error.message);
            }
        }

        return {
            scope: {
                height: '@',
                width: '@'
            },
            link: link,
            template: template
        }

    }];

    angular.module('bofFinder', [])
        .directive('mapBoff', mapBoffLocation);

}());
