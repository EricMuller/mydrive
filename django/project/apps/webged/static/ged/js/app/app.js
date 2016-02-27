  
var app = angular.module('my-ged', ['ngRoute','mdr.file','ui.tree','my-ged.home','my-ged.archives'
  ,'my-ged.upload','my-ged.plan']);

app.config(['$routeProvider',
    function($routeProvider) { 
        // Système de routage
        $routeProvider
        .when('/contact', {
            templateUrl: 'partials/contact.html',
            controller: 'contactCtrl'
        })
        .when('/about', {
            templateUrl: 'partials/about.html',
            controller: 'aboutCtrl'
        }).otherwise({
            redirectTo: '/home'
        });

        //$locationProvider.html5Mode(true);
    }
]);


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

// The controller


function textCtrl($scope) {
	var d = new Date();
  	console.log(d);
}
function  aboutCtrl($scope, $rootScope) {
	 $rootScope.selectedMenuName('About');
}

function  contactCtrl($scope, $rootScope) {
	 $rootScope.selectedMenuName('Contact');
}


function notesCtrl($scope, $http, $rootScope){
  
  $rootScope.selectedMenuName('Notes');

  $scope.data = [
   {id:1, title:'Foo', desc:'More stuff about this here', category_name:'Category 1'},
   {id:2, title:'Goo', desc:'More stuff about this here', category_name:'Category 2'},
   {id:3, title:'Roo', desc:'Blah details on Roo are here', category_name:'Category 1'},
   {id:4, title:'Hoo', desc:'More stuff about Hoo here', category_name:'Category 2'},
   {id:5, title:'Woo', desc:'More stuff about this here', category_name:'Category 3'}
  ];
  
  $scope.setSelectedItem = function(i){
    $scope.selectedItem = i;
  }
  
  $scope.deleteItem = function(){
    if ($scope.selectedItem >= 0) {
    	$scope.data.splice($scope.selectedItem,1);
    }
  }
  
}


app.controller('notesCtrl', notesCtrl);
app.controller('textCtrl', textCtrl);
app.controller('aboutCtrl', aboutCtrl);
app.controller('contactCtrl', contactCtrl);


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


