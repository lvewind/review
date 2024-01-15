<?php

namespace App\Http\Controllers\Api;

use App\Models\Department;
use App\Models\Inspector;
use App\Models\Project;
use App\Models\PlaceScheduling;
use App\Models\Scheduling;
use Illuminate\Http\Request;
use App\Http\Controllers\Controller;


class InspectorApi extends Controller
{

    public function get_inspectors($department_id)
    {
        return Inspector::all()->where("department_id", $department_id);
    }

}
