<?php

use Illuminate\Routing\Router;
use Illuminate\Support\Facades\Route;
use Dcat\Admin\Admin;

Admin::routes();

Route::group([
    'prefix'     => config('admin.route.prefix'),
    'namespace'  => config('admin.route.namespace'),
    'middleware' => config('admin.route.middleware'),
], function (Router $router) {

    $router->get('/', 'HomeController@index');

    $router->get('inspection-form/{place}', 'InspectionFormController@form');

    $router->resource('users', 'UserController');

    $router->resource('inspection-result', 'InspectionResultController');

    $router->resource('scheduling', 'SchedulingController');

    $router->resource('place', 'PlaceController');

    $router->resource('project', 'ProjectController');

    $router->resource('inspector', 'InspectorController');

    $router->resource('department', 'DepartmentController');

});


