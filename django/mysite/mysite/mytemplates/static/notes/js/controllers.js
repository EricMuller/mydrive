

var myApp = angular.module('notesApp',[]);

myApp.controller('notesController', notesController);
myApp.controller('textController', textController);

function notesController($scope,$http) {
  					
					var d = new Date();
  					console.log(d);
  					$http.get("/notes/servicesrestnotes/")
  						.success(function(response) {
  							$scope.names = response;
  					
  							$scope.text=d;
  						});
}	

function textController($scope) {
  					
					var d = new Date();
  					console.log(d);
  					
}	

