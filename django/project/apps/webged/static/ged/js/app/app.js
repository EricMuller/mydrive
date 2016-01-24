
var app = angular.module('myApp', ['ngRoute','mdr.file','ui.tree']);

app.config(['$routeProvider',
    function($routeProvider) { 
        // Système de routage
        $routeProvider
        .when('/home', {
            templateUrl: 'partials/home.html',
            controller: 'appCtrl'
        })
        .when('/contact', {
            templateUrl: 'partials/contact.html',
            controller: 'contactCtrl'
        })
        .when('/about', {
            templateUrl: 'partials/about.html',
            controller: 'aboutCtrl'
        })
        .when('/archives', {
            templateUrl: 'partials/archives.html',
            controller: 'archivesCtrl'
        }).when('/upload', {
            templateUrl: 'partials/upload.html',
            controller: 'uploadCtrl'
        }).when('/fileplan', {
            templateUrl: 'partials/fileplan.html',
            controller: 'fileplanCtrl'
        })
        .otherwise({
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

function InstantSearchCtrl($scope){

	// The data model. These items would normally be requested via AJAX,
	// but are hardcoded here for simplicity. See the next example for
	// tips on using AJAX.

	$scope.items = [
		{
			url: 'http://tutorialzine.com/2013/07/50-must-have-plugins-for-extending-twitter-bootstrap/',
			title: '50 Must-have plugins for extending Twitter Bootstrap',
			image: 'http://cdn.tutorialzine.com/wp-content/uploads/2013/07/featured_4-100x100.jpg'
		},
		{
			url: 'http://tutorialzine.com/2013/08/simple-registration-system-php-mysql/',
			title: 'Making a Super Simple Registration System With PHP and MySQL',
			image: 'http://cdn.tutorialzine.com/wp-content/uploads/2013/08/simple_registration_system-100x100.jpg'
		},
		{
			url: 'http://tutorialzine.com/2013/08/slideout-footer-css/',
			title: 'Create a slide-out footer with this neat z-index trick',
			image: 'http://cdn.tutorialzine.com/wp-content/uploads/2013/08/slide-out-footer-100x100.jpg'
		},
		{
			url: 'http://tutorialzine.com/2013/06/digital-clock/',
			title: 'How to Make a Digital Clock with jQuery and CSS3',
			image: 'http://cdn.tutorialzine.com/wp-content/uploads/2013/06/digital_clock-100x100.jpg'
		},
		{
			url: 'http://tutorialzine.com/2013/05/diagonal-fade-gallery/',
			title: 'Smooth Diagonal Fade Gallery with CSS3 Transitions',
			image: 'http://cdn.tutorialzine.com/wp-content/uploads/2013/05/featured-100x100.jpg'
		},
		{
			url: 'http://tutorialzine.com/2013/05/mini-ajax-file-upload-form/',
			title: 'Mini AJAX File Upload Form',
			image: 'http://cdn.tutorialzine.com/wp-content/uploads/2013/05/ajax-file-upload-form-100x100.jpg'
		},
		{
			url: 'http://tutorialzine.com/2013/04/services-chooser-backbone-js/',
			title: 'Your First Backbone.js App – Service Chooser',
			image: 'http://cdn.tutorialzine.com/wp-content/uploads/2013/04/service_chooser_form-100x100.jpg'
		}
	];

}

function archivesCtrl($scope, $http, $rootScope) {
  	
  //	$rootScope.selectedMenu='Archives';
  $scope.showIt=true;

	$rootScope.selectedMenuName('Archives');

	var d = new Date();
  	console.log(d);
  	$http.get("apis/documents/")
  		.success(function(response) {
  			$scope.names = response;
  			$scope.text=d;
  		});
}	

function textCtrl($scope) {
  					
	var d = new Date();
  	console.log(d);
  					
}

function  uploadCtrl($scope, $rootScope,$window) {
  					
	$rootScope.selectedMenuName('Upload');
	
	
	$scope.$on('transferComplete', function(event,data) { 
		
		console.log(data);
		if (data.status == '200' ) {
			console.log(data.response);
			var json = JSON.parse(data.response);
			console.log(json); 
			$scope.uploadFiles.push(json); 
		}else{
			//alert(data);
			$window.alert(data.response);
		}
	}
	);
}

function  fileplanCtrl($scope, $rootScope) {
            
  $rootScope.selectedMenuName('File Plan');
  
  
  $scope.data=
    [
      {
        "id": 1,
        "title": "Travail",
        "items": [
          {
            "id": 11,
            "title": "Contrat",
            "items": []
          },
          {
            "id": 12,
            "title": "Fiches de paie",
            "items": []
          }
        ]
      }
      ,
      {
        "id": 2,
        "title": "Vie courante",
        "items": [
          {
            "id": 21,
            "title": "Factures",
            "items": []
          }
         ]
      },
      {
        "id": 3,
        "title": "Sante",
        "items": [
            {
              "id": 31,
              "title": "Medecin",
              "items": []
            },
            {
              "id": 32,
              "title": "Ophtalmo",
              "items": []
            }
         ]
      }
    ];

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


function appCtrl($scope, $rootScope) {

	$rootScope.selectedMenuName= function(title){
			$rootScope.selectedMenu=title;
			$('#title').text(title);
	};

	$rootScope.selectedMenuName('Welcome');
	$scope.uploadFiles = [];


}

app.controller('appCtrl', ['$scope','$rootScope',appCtrl]);

app.controller('archivesCtrl', archivesCtrl);
app.controller('InstantSearchCtrl', InstantSearchCtrl);

app.controller('notesCtrl', notesCtrl);
app.controller('textCtrl', textCtrl);

app.controller('uploadCtrl', ['$scope','$rootScope','$window',uploadCtrl]);
app.controller('aboutCtrl', aboutCtrl);
app.controller('contactCtrl', contactCtrl);

app.controller('fileplanCtrl', fileplanCtrl);


app.directive('myDirective', function (httpPostFactory) {
    return {
        restrict: 'A',
        scope: true,
        link: function (scope, element, attr) {
            element.bind('change', function () {
                var formData = new FormData();
                formData.append('file', element[0].files[0]);
                httpPostFactory('/ged/upload/', formData, function (callback) {
                    console.log(callback);
                });
            });

        }
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


app.filter('bytesToSize', function() {

  // In the return function, we must pass in a single parameter which will be the data we will work on.
  // We have the ability to support multiple other parameters that can be passed into the filter optionally
  return function(input, optional1, optional2) {


 	var sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
    if (input === 0) return 'n/a';
    var i = parseInt(Math.floor(Math.log(input) / Math.log(1024)));
    if (i === 0) return input + ' ' + sizes[i];
    var output= (input / Math.pow(1024, i)).toFixed(1) + ' ' + sizes[i];
    // Do filter work here
    return output;

  }

});
