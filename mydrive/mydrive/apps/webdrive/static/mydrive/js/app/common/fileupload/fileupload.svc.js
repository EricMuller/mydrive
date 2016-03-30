(function(){
    'use strict';

    angular
        .module('my-ged.common')
        .service('uploaderSvc', UploaderSvc);

    function UploaderSvc(FileUploader, postman, $rootScope, $q, Restangular) {
        var self = this;

        var service = {
            afterLoadSuccessFunction: null,
            getUploader: getUploader,
            uploadAttachments: uploadAttachments,
            deleteAttachments: deleteAttachments
        };


        return service;

        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        function getUploader(url, formData, queueLimit, afterLoadSuccessFunction, modalInstance, uploadOnAdd) {
            var Uploader = new FileUploader({
                url: url,
                /*headers: {
                    'X-CSRF-Token': $rootScope.user.token
                },*/
                removeAfterUpload: true,
                formData: [],
                filters: [{
                    name: 'mimeType',
                    fn: function(item) {
                        //TODO White lister les mimes-types authorisés
                        //['application/pdf','application/x-pdf', 'application/vnd.ms-excel', 'application/vnd.ms-powerpoint', 'application/vnd.ms-word']
                        return item.type !== 'application/x-msdownload';
                    }
                }, {
                    name: 'fileSize',
                    fn: function(item) {
                        // max size 10Mb => 10240000 octets
                        return item.size < 10240000;
                    }
                }, {
                    name: 'emptyFile',
                    fn: function(item) {
                        return item.size > 0;
                    }
                }]
            });
            if (queueLimit) {
                Uploader.queueLimit = queueLimit;
            }
            if (formData) {
                Uploader.formData = formData;
            }

            /* Fonctions qui gèrent l'upload */
            Uploader.uploadFile = function(fileItem) {
                fileItem.upload();
            };

            Uploader.uploadAllFiles = function(formData) {
                for (var i = 0; i < Uploader.queue.length; i++) {
                    Uploader.queue[i].formData = formData;
                    Uploader.queue[i].upload();
                }
            };

            Uploader.onAfterAddingFile = function(fileItem) {
                if (Uploader.url && uploadOnAdd) {
                    this.uploadFile(fileItem);
                }
                if (self.uploadDisallowed) {
                    fileItem.remove();
                }
            };

            Uploader.onSuccessItem = function(fileItem) {
                if (fileItem.formData) {
                    var uploadData = {
                        url: url,
                        formData: fileItem.formData
                    };
                    $rootScope.$broadcast('uploadSuccess', uploadData);
                }
                if (afterLoadSuccessFunction) {
                    afterLoadSuccessFunction(this);
                }
                if (modalInstance) {
                    modalInstance.close();
                }
                postman.success('Fichier enregistré', 'Le fichier "' + fileItem.file.name + '" a bien été ajouté');
            };

            Uploader.onCompleteAll = function(){
                $rootScope.$broadcast('completeAll');
            };

            /* Fonctions qui gèrent les erreurs */
            Uploader.onErrorItem = function(fileItem) {
                postman.error('Erreur enregistrement', 'Le fichier "' + fileItem.file.name + '" n\'a pas été ajouté');
                fileItem.isUploaded = false;
            };

            Uploader.onWhenAddingFileFailed = function(fileItem, error) {
                debugger
                if (error && error.name) {
                    switch (error.name) {
                        case 'mimeType':
                            postman.error('Type de fichier non autorisé', '"' + fileItem.name + '" non pris en compte');
                            break;
                        case 'fileSize':
                            postman.error('Taille maximale dépassée (10 Mo)', '"' + fileItem.name + '" non pris en compte');
                            break;
                        case 'queueLimit':
                            postman.error('Limite de fichiers dépassée', '"' + fileItem.name + '" non pris en compte');
                            break;
                        case 'emptyFile':
                            postman.error('Fichier vide', '"' + fileItem.name + '" non pris en compte');
                            break;
                        default:
                            postman.error('Erreur lors de l\'ajout du fichier' + fileItem.name);
                            break;
                    }
                }
            };

            return Uploader;
        }

        // upload one item with formData
        function _uploadAttachment(uploader, key) {
            var formData = [{
                idInfoCle: key
            }];
            uploader.uploadAllFiles(formData);
        }

        function uploadAttachments(uploader) {
            var key, deferred = $q.defer(),
                uploads = [];
            for (key in uploader) {
                if (uploader[key].queue.length > 0) {
                    uploads[key] = _uploadAttachment(uploader[key], key);
                }
            }
            $q.all(uploads);

            if (uploads.length == 0) {
                // no files to upload
                deferred.resolve();
            }
            $rootScope.$on('completeAll', function(){
                deferred.resolve();
            });

            return deferred.promise;
        }

        function deleteAttachments(ids) {
            var deferred = $q.defer();
            if (ids.length > 0) {
                var uploads = [];
                for (var i = 0, j = ids.length; i < j; i++) {
                    uploads[i] = Restangular.one('pieceJointe', ids[i]).all('delete').post();
                }
                $q.all(uploads).then(function() {
                    // all delete all done
                    deferred.resolve();
                })
            } else {
                deferred.resolve();
            }
            return deferred.promise;
        }
    }

})();
