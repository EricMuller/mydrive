angular.module('my-ged.documents', [ 'ui.router' ]).config(
		function($stateProvider) {
			 $stateProvider
        		.state('upload', {
                    url:'/upload',
            		templateUrl: 'partials/upload.html',
            		controller: 'uploadCtrl',
                    resolve:{
                     plan : function(planSvc){
                                return planSvc.getPlan();
                            }
                    }
        		})
				.state('documents', {
                    url: '/documents',
            		templateUrl: 'partials/documents.html',
            		controller: 'plandocumentCtrl',
                    resolve:{
                        plan : function(planSvc){
                                return planSvc.getPlan();
                            }
                    }
            		
        		})
                .state('documents.upload', {
                    url:'/documents/upload',
                    templateUrl: 'partials/documents/upload.html',
                    controller: 'uploadCtrl'
                    
                })
                .state('documents.documents', {
                    url:'/documents/documents',
                    templateUrl: 'partials/documents/documents.html',
                    controller: 'documentsCtrl',
                    resolve:{
                        documents : function(TokenRestangular) {
                            return TokenRestangular.one("documents").get()  ;
                        }
                    }
                })
                .state('documents.history', {
                    url:'/documents/history',
                    templateUrl: 'partials/documents/history.html',
                    controller: 'documentsCtrl',
                    resolve:{
                        documents : function(TokenRestangular) {
                            return TokenRestangular.one("documents").get()  ;
                        }
                    }
                })

        		;
		});