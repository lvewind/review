<?php

namespace App\Http\Controllers\Api;

use App\Http\Controllers\Controller;
use App\Models\Project;
use Illuminate\Http\Request;
use Illuminate\Http\Response;
use Illuminate\Support\Facades\Storage;
use PhpParser\Node\Expr\Cast\Object_;

class UploadFile extends Controller
{
    /**
     * 更新用户头像
     *
     * @param Request $request
     * @return Response
     */

    public function upload_image(Request $request){
        $p_id = $request->post('p_id');
        $index = $request->post('index');
        $path = $request->file('photo_'.str($p_id))->store('public/images/'.str(date("Y-m-d")));

        return array('index'=>$index, 'photo_path'=>$path, 'photo_url'=> Storage::url($path));
    }

    public function upload_video(Request $request){
        $p_id = $request->post('p_id');
        $index = $request->post('index');
        $path = $request->file('video_'.str($p_id))->store('public/videos/'.str(date("Y-m-d")));


        return array('index'=>$index, 'video_path'=>$path,'video_url'=> Storage::url($path));
    }

    public function deleteFile(Request $request){
        $fileName = $request->post('file_name');
    }
}
