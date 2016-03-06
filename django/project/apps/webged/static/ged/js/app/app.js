  
var app = angular.module('my-ged', ['ngRoute','mdr.file','ui.tree','ngMaterial','material','my-ged.home','my-ged.archives'
  ,'my-ged.upload','my-ged.plan','my-ged.login','my-ged.common', 'restangular']);

app.config(['$routeProvider',
    function($routeProvider) { 
        // Système de routage
        $routeProvider.otherwise({
            redirectTo: '/home'
        });

        //$locationProvider.html5Mode(true);
    }
]);


app.config(function(RestangularProvider) {
      RestangularProvider.setBaseUrl('apis/');
      //RestangularProvider.setMethodOverriders(["put", "delete"]);
      RestangularProvider.setRequestSuffix('/?format=json');
      RestangularProvider.setDefaultHeaders({'Content-Type': 'application/json'});
});

app.filter('searchFor', function(){

	// All filters must return a function. The first parameter
	// is the data that is to be filtered, and the second is an
	// argument that may be passed with a colon (searchFor:searchString)

	return function(arr, searchString){

		if(!searchString){
			return arr;
		}

		var result = [];

		searchString = searchString.toLowerCase();

		// Using the forEach helper method to loop through the array
		angular.forEach(arr, function(item){

			if(item.title.toLowerCase().indexOf(searchString) !== -1){
				result.push(item);
			}

		});

		return result;
	};

});


app.factory('httpPostFactory', function ($http) {
    return function (file, data, callback) {
        $http({
            url: file,
            method: "POST",
            data: data,
            headers: {'Content-Type': undefined}
        }).success(function (response) {
            callback(response);
        });
    };
});




/*
http://docs.angularjs.org/api/ng.$interpolateProvider
app.config(function($interpolateProvider) {
$interpolateProvider.startSymbol('{[{');
$interpolateProvider.endSymbol('}]}');
});
*/

