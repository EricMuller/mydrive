angular
    .module('my-ged.common')
    .directive('myDirective', function (httpPostFactory) {
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
