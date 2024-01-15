<?php

namespace App\Http\Controllers\Api;

use App\Models\Department;
use App\Models\InspectionResult;
use App\Models\Place;
use App\Models\Project;
use App\Models\PlaceScheduling;
use App\Models\ProjectResult;
use App\Models\Scheduling;
use Illuminate\Http\Request;
use App\Http\Controllers\Controller;


class InspectionForm extends Controller
{

    public function get_form($place_id)
    {
        $place = Place::all()->where("id", $place_id)->first();
        $department = Department::all()->where('id', $place->department_id)->first();
        $project = Project::all()->where('place_id', $place_id);
        $place_scheduling = PlaceScheduling::all()->where('place_id', $place_id);
        $scheduling = [];
        foreach($place_scheduling as $item ){
            $scheduling[] = Scheduling::all()->where('id', $item->scheduling_id)->first();
        }

        return array('place'=> $place, 'department'=>$department, 'scheduling'=>$scheduling, 'project'=>$project, 'test'=>"");
    }

    public function save_inspection(Request $request){
        $inspectionResult = new InspectionResult;
        $inspectionResult->name = $request->post('name');
        $inspectionResult->inspection_status = $request->post('inspection_status');
        $inspectionResult->department_id = $request->post('department_id');
        $inspectionResult->place_id = $request->post('place_id');
        $inspectionResult->scheduling_id = $request->post('scheduling');
        $inspectionResult->inspector = $request->post('inspector');
        $inspectionResult->save();

        $projectList = $request->post("projectList");
        foreach ($projectList as $project){
            $projectResult = new ProjectResult;
            $projectResult->name = $project['name'];
            $projectResult->inspection_datetime = new \DateTime();
            $projectResult->project_status = $project['project_status'];
            $projectResult->photo_url = $project['photo_url'];
            $projectResult->photo_path = $project['photo_path'];
            $projectResult->video_url = $project['video_url'];
            $projectResult->video_path = $project['video_path'];
            $projectResult->note = $project['note'];
            $inspectionResult->projects_result()->save($projectResult);
        }

        return "success";

    }
}
