mbofuiApp.controller('mbofuiAppController', ['$scope', 'Bof', function($scope, Bof) {  
  $scope.postBof = function() {
  // serialize the inputs to create a URL
    url = '/?messageText=' + $scope.newMessageText 
    console.log(url)
   //Bof.PostBof(url).then(function(result) {
   //});
  }
}]);