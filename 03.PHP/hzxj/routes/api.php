<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:sanctum')->get('/user', function (Request $request) {
    return $request->user();
});

Route::namespace('App\Http\Controllers\Api')->prefix('v1')->group(function () {
    Route::get('/get-form/{form_id}', 'InspectionForm@get_form');
    Route::get('/get-inspector/{department_id}', 'InspectorApi@get_inspectors');
    Route::post("save-inspection", 'InspectionForm@save_inspection');
    Route::post('/upload-image', 'UploadFile@upload_image');
    Route::post('/upload-video', 'UploadFile@upload_video');
});


