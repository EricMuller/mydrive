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
                        tree : function(planSvc){
                                return planSvc.getTree();
                            }
                    }
            		
        		})
                .state('documents.upload', {
                    url:'/upload/:id',
                    templateUrl: 'partials/documents/upload.html',
                    controller: 'uploadCtrl'
                    
                })
                .state('documents.documents', {
                    url:'/documents/:id',
                    templateUrl: 'partials/documents/documents.html',
                    controller: 'documentsCtrl',
                    resolve:{
                        documents :  function(documentSvc, $stateParams) {
                                return documentSvc.getDocumentsByFolder($stateParams.id)  ;
                        }
                        
                    }
                })
                .state('documents.history', {
                    url:'/history',
                    templateUrl: 'partials/documents/history.html',
                    controller: 'documentsCtrl',
                    resolve:{
                        documents : function(documentSvc) {
                            return documentSvc.getDocuments()  ;
                        }
                    }
                })

        		;
		});